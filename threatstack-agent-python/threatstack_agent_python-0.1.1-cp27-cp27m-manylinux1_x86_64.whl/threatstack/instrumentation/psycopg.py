"""Instrumentation of postgres

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

def _w_pg_connect(wrapped, instance, args, kwargs):
    config = {}
    if kwargs is not None:
        for key, value in six.iteritems(kwargs):
            if key not in ['passwd'] and isinstance(value, six.string_types) is True:
                # _logger.debug('pg_connect %s == %s', key, value)
                config[key] = value

    event_dict = {}
    event_dict['payload'] = {}
    event_dict['payload'] = {
        'config': config
    }
    event_dict['method_name'] = 'connect'
    event_dict['module_name'] = 'postgres'
    
    receiver_instance().set_event(event_dict)
    return wrapped(*args, **kwargs)

def _on_import_factory(module, raise_errors=True):
    """Factory to create an import hook for the provided module name"""
    def on_import(hook):

        wrap_function_wrapper(module, 'connect', _w_pg_connect)

    return on_import

def patch_pg():
    """wrap the psycopg module """  

    module = 'psycopg2'
    try:
        importer.when_imported(module)(_on_import_factory(module))
    except Exception as exc:
        _logger.debug('failed to patch %s', module)
        raise
        return False

def wrap_pg():
    """Called during agent initialization to instrument the postgres

    """    
    patch_pg()
