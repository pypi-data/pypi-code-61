"""Instrumentation of the Django Redis plugin

"""

import sys
import six
import inspect
import threading 
import imp
import urllib
import re
import json
import wrapt

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
from ..util.wrapper import function_wrapper, wrap_object
from ..receiver import receiver_instance

from ..errors import ThreatstackError, RequestBlockedError, ThreatstackStackError
from ..config import CONF

from wrapt import importer, wrap_function_wrapper

def wrapper_redis(wrapped, instance, args, kwargs):
    if kwargs is not None:
        config = {}
        for key, value in six.iteritems(kwargs):
            _logger.debug('wrapper_redis %s == %s', key, value)
            if key == 'connection_pool':
                if value.connection_kwargs is not None:
                    for kw, vw in six.iteritems(value.connection_kwargs):
                        if kw not in ['parser_class', 'password']:
                            _logger.debug('connection_pool %s == %s', kw, vw)
                            config[kw] = vw

        event_dict = {}
        event_dict['payload'] = {}
        event_dict['payload'] = {
            'config': config
        }
        event_dict['method_name'] = 'connect'
        event_dict['module_name'] = 'redis'
        
        _logger.debug('event_dict %s', event_dict)
        receiver_instance().set_event(event_dict)
    return wrapped(*args, **kwargs)

def _on_import_factory(module, raise_errors=True):
    """Factory to create an import hook for the provided module name"""
    def on_import(hook):

        wrap_function_wrapper(module, 'Redis.__init__', wrapper_redis)

    return on_import

def patch_django_redis():
    """wrap the redis module """  

    module = 'redis'
    try:
        importer.when_imported(module)(_on_import_factory(module))
    except Exception as exc:
        _logger.debug('failed to patch %s', module)
        raise
        return False

def wrap_django_redis():
    """Called during agent initialization to instrument the Django Redis plugin

    """    
    patch_django_redis()
