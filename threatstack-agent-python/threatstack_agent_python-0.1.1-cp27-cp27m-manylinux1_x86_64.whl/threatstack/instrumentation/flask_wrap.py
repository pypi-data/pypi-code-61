"""Instrumentation of Flask
"""

import six
import re
import os
from wrapt import importer, wrap_function_wrapper

if six.PY2:
    import exceptions # noqa

    _exceptions_module = exceptions
elif six.PY3:
    import builtins

    _exceptions_module = builtins
else:
    _exceptions_module = None

from .helper import check_for_attacks
from ..receiver import receiver_instance
from ..errors import RequestBlockedError
from ..util import logger

_logger = logger.getLogger(__name__)

def _w_flask_dispatch_request(wrapped, instance, args, kwargs):
    """wrap Flask dispatch_request"""
    _logger.info('Intercepted Flask dispatch_request')
    try:
        from flask import _request_ctx_stack # noqa
        request = _request_ctx_stack.top.request

        # configs must be loaded too by now
        if not hasattr(instance, '_threatstack_configs_read') and \
                hasattr(instance, 'config') and \
                instance.config.items():

            _logger.debug('Get Flask settings %d', os.getpid())
            try:
                settings_flask = {}

                keys_threatstack_flask = ['SECRET_KEY']
                for k, v in six.iteritems(instance.config):
                    _logger.debug('flask.config key=%s, value=%s', k, v)
                    for keybf in keys_threatstack_flask:
                        if re.match(keybf, k) is None:
                            settings_flask[k] = v

                event_dict = {'payload': settings_flask, 'method_name': 'setup', 'module_name': 'flask_conf'}
                receiver_instance().set_event(event_dict)
            except ImportError:
                _logger.debug('Could not get Flask settings module')
                pass

            setattr(instance, '_threatstack_configs_read', True)

        _logger.debug('Incoming request: %s %s -- remote_host=%s, user_agent=%s, path_info=%s', request.method,
                      request.path, request.headers.environ['REMOTE_ADDR'], request.headers.environ['HTTP_USER_AGENT'],
                      request.headers.environ['PATH_INFO'])

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

        if hasattr(request, 'args'):
            _logger.debug('Checking query parameters: %s', request.args)
            perform_checks(request.args, 'query')

        if hasattr(request, 'form'):
            _logger.debug('Checking form body parameters: %s', request.form)
            perform_checks(request.form, 'body')

        if hasattr(request, 'json'):
            _logger.debug('Checking json body parameters: %s', request.json)
            perform_checks(request.json, 'body')

    except RequestBlockedError:
        raise
    except:
        _logger.exception('Caught exception in flask dispatch_request')

    return wrapped(*args, **kwargs)

def _on_import_factory(module, raise_errors=True):
    """Factory to create an import hook for the provided module name"""

    def on_import(hook):
        wrap_function_wrapper(module, 'Flask.full_dispatch_request', _w_flask_dispatch_request)
        _logger.info('Flask instrumentation done')

    return on_import

def _on_import_wrap_function(module, method_to_be_wrapped, wrapper, raise_errors=True):
    """Factory to create an import hook for the provided module name"""
    def on_import(hook):
        wrap_function_wrapper(module, method_to_be_wrapped, wrapper)

    return on_import

def patch_flask():
    """wrap flask middleware """

    module = 'flask.app'
    try:
        importer.when_imported(module)(_on_import_factory(module))
    except Exception as exc:
        _logger.exception('Failed to patch module: %s', module)

def wrap_flask():
    """Called during agent initialization to instrument flask

    """
    _logger.info('Instrumenting Flask framework')
    patch_flask()
