"""Instrumentation of the Django module

"""

import sys
import six
import re
import json
import traceback

if six.PY2:
    import exceptions
    _exceptions_module = exceptions
elif six.PY3:
    import builtins
    _exceptions_module = builtins
else:
    _exceptions_module = None

from ..util import logger
_logger = logger.getLogger(__name__)

from ..util.common import callable_name
from ..util.wrapper import PostFunctionWrapper

from ..errors import RequestBlockedError
from wrapt import importer, FunctionWrapper, wrap_object, wrap_function_wrapper

from ..receiver import receiver_instance
from .helper import check_for_attacks

# Django Middleware addition

def wrapper_django_setup(wrapped=None, *args, **kwargs):
    """Wrapper function for django.setup
    """    
    _logger.debug('wrapper_django_setup')
    try:
        settings_django = {}
        from django.conf import settings
        if settings.configured:
            _logger.debug('django.conf.settings were configured')
            keys_threatstack_django =  ['DATABASES', 'AUTHENTICATION_BACKENDS', 'CSRF_*', 'PASSWORD_*', 'AUTHENTICATION_*', 'SIGNING_*', 'SERVER_*', 'SECURE_*', 'EMAIL_USE_*', 'EMAIL_SSL_*', 'DEBUG', 'MIDDLEWARE']
            for key in dir(settings):            
                for keybf in keys_threatstack_django:
                    if re.match(keybf,key) is not None:
                        val = getattr(settings, key)
                        if val is not None:
                            _logger.debug('%s, %s', key, val)
                            settings_django[key] = val

            event_dict = {}
            event_dict['payload'] = {}
            event_dict['payload'] = settings_django
            event_dict['method_name'] = 'setup'
            event_dict['module_name'] = 'django_conf'

            receiver_instance().set_event(event_dict)            
        else:
            _logger.debug('django.conf.settings were not configured')
    except ImportError:
        _logger.debug('Could not get Django settings module')
        pass        

    def wrapper(wrapped, instance, args, kwargs):
        name = callable_name(wrapped)
        return wrapped(*args, **kwargs)

    return FunctionWrapper(wrapped, wrapper)


def get_django_settings(wrapped, instance, args, kwargs):
    """Wrapper function for django Settings
    """    
    _logger.debug('Try to get django settings %d', os.getpid())
    try:
        settings_django = {}
        from django.conf import settings
        if settings.configured:
            keys_threatstack_django =  ['DATABASES', 'AUTHENTICATION_BACKENDS', 'CSRF_*', 'PASSWORD_*', 'AUTHENTICATION_*', 'SIGNING_*', 'SERVER_*', 'SECURE_*', 'EMAIL_USE_*', 'EMAIL_SSL_*', 'DEBUG', 'MIDDLEWARE']
            for key in dir(settings):            
                for keybf in keys_threatstack_django:
                    if re.match(keybf,key) is not None:
                        val = getattr(settings, key)
                        if val is not None:
                            _logger.debug('%s, %s', key, val)
                            settings_django[key] = val

            event_dict = {}
            event_dict['payload'] = {}
            event_dict['payload'] = settings_django
            event_dict['method_name'] = 'setup'
            event_dict['module_name'] = 'django_conf'

            receiver_instance().set_event(event_dict)
        else:
            _logger.debug('django.conf.settings were not configured')
    except ImportError:
        _logger.debug('Could not get Django settings module')
        pass    

    wrapped(*args, **kwargs)

def wrap_rawsql(wrapped, instance, args, kwargs):
    """Wrapper function for query.raw()
    """    
    _logger.debug('intercepted raw sql')
    _logger.debug('kwargs %s, args %s', kwargs, args)

    config = {}
    if args is not None and args[0]:
        arg = args[0]
        if isinstance(arg, six.string_types) is True:
            _logger.debug('django raw_query %s', arg)
            config['sql'] = arg

    config['stack'] = traceback.format_stack(None,4)

    event_dict = {
        'payload': config,
        'method_name': 'raw',
        'module_name': 'django_queryset'
    }

    # _logger.debug('event_dict %s', event_dict)
    receiver_instance().set_event(event_dict)

    wrapped(*args, **kwargs)

def _on_import_factory(module, method_to_be_wrapped, wrapper, raise_errors=True):
    """Factory to create an import hook for the provided module name"""
    def on_import(hook):
        wrap_object(module, method_to_be_wrapped, PostFunctionWrapper, (wrapper,))

    return on_import

def _on_import_wrap_function(module, method_to_be_wrapped, wrapper, raise_errors=True):
    """Factory to create an import hook for the provided module name"""
    def on_import(hook):
        wrap_function_wrapper(module, method_to_be_wrapped, wrapper)

    return on_import

def _process_view(request, handler_func, handler_args, handler_kwargs):
    _logger.debug('Incoming request: %s %s -- remote_host=%s, user_agent=%s, path_info=%s', request.method,
                  request.path, request.META.get('REMOTE_ADDR',''), request.META.get('HTTP_USER_AGENT',''), request.META.get('PATH_INFO',''))

    def perform_checks(params, location):
        attacks = check_for_attacks(params)
        for attack in attacks:
            event = {'path': request.path, 'method': request.method, 'params': params, 'params_in': location,
                     'attack_details': {
                         'signature': attack['details']['signature'],
                         'value': attack['value']
                     }}
            receiver_instance().set_event_attack(event, attack['type'], attack['details']['blocked'], request)
            # raise exception if needed
            if attack['details']['blocked']:
                _logger.error('Blocked Request: %s', attack['details']['message'])
                raise RequestBlockedError(attack['details']['message'], attack['type'])

    # check query parameters for all requests
    if hasattr(request, 'GET'):
        _logger.debug('Checking query parameters')
        perform_checks(request.GET, 'query')

    # check body parameters for non GET requests (POST/PUT/PATCH...)
    if request.method != 'GET':
        # Parse request body - we need to do this because other Django middleware has not executed yet at this point
        if request.content_type != "application/json":
            try:
                _logger.debug('Detected a non JSON payload, parsing...')
                orig_method = request.method
                if hasattr(request, '_post'):
                    del request._post
                if hasattr(request, '_files'):
                    del request._files
                request.method = 'POST'
                request._load_post_and_files()
                request.method = orig_method
            except AttributeError:
                try:
                    _logger.debug('AttributeError while parsing, retrying with META tags')
                    request.META['REQUEST_METHOD'] = 'POST'
                    request._load_post_and_files()
                    request.META['REQUEST_METHOD'] = 'PUT'
                except:
                    _logger.exception('Could not parse request body')
            except:
                _logger.exception('Could not parse request body')
            finally:
                request._ts_body = request.POST
        else:
            try:
                _logger.debug('Detected a JSON payload, parsing...')
                request._ts_body = json.loads(request.body)
            except:
                _logger.exception('Could not parse JSON request body')
        # perform checks if parsing succeeded
        if hasattr(request, '_ts_body'):
            perform_checks(request._ts_body, 'body')


def wrapper_django(wrapped, instance, args, kwargs):
    """Wrapper function for query.raw()
    """
    _logger.debug('Django middleware instrumentation starting')
    # Call the original method we're wrapping to initialize the properties
    wrapped(*args, **kwargs)

    try:
        # Insert Threatstack middleware
        instance._view_middleware.insert(0, _process_view)
    except:
        _logger.error('Error while inserting TS middleware: %s', sys.exc_info()[0])
    else:
        _logger.debug('Django middleware instrumentation done')

def patch_django():
    """wrap the django module """

    module = 'django.core.handlers.base'
    try:
        importer.when_imported(module)(_on_import_wrap_function(module, 'BaseHandler.load_middleware', wrapper_django))
    except Exception:
        _logger.debug('failed to patch %s', module)

    # module = 'django'
    module = 'django.core.wsgi'
    try:
        importer.when_imported(module)(_on_import_factory(module, 'get_wsgi_application', wrapper_django_setup))
    except Exception as exc:
        _logger.debug('failed to patch %s', module)

    module = 'django.db.models.query'
    try:
        importer.when_imported(module)(_on_import_wrap_function(module, 'QuerySet.raw', wrap_rawsql))
    except Exception as exc:
        _logger.debug('failed to patch %s', module)



def wrap_django():
    """Called during agent initialization to instrument the Django framework

    """    
    patch_django()
