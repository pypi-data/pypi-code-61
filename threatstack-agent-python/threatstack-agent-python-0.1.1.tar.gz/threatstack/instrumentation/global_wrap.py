"""Instrumentation of global

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
    MODULE_NAME = '__builtin__'
elif six.PY3:
    import builtins
    _exceptions_module = builtins
    MODULE_NAME = 'builtins'
else:
    _exceptions_module = None

from ..util import logger
_logger = logger.getLogger(__name__)

from ..util.common import callable_name
from ..util.wrapper import function_wrapper, wrap_object, wrap_function_wrapper_failsafe, wrap_function_generic
from ..receiver import receiver_instance

from ..errors import ThreatstackError, RequestBlockedError, ThreatstackStackError
from ..config import CONF

from wrapt import importer, wrap_function_wrapper

def _on_import_factory(module, raise_errors=True):
    """Factory to create an import hook for the provided module name"""
    def on_import(hook):

        methodList = ['eval']
        for i,val in enumerate(methodList):
            wrap_function_wrapper_failsafe(module, val, wrap_function_generic(MODULE_NAME, val, receiver_instance()))    
    return on_import

def patch_global():
    """wrap the global module """  

    module = MODULE_NAME
    try:
        importer.when_imported(module)(_on_import_factory(module))
    except Exception as exc:
        _logger.debug('failed to patch %s', module)
        raise
        return False

def wrap_global():
    """Called during agent initialization to instrument global library

    """    
    patch_global()
