"""Instrumentation of subprocess

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
from ..util.wrapper import function_wrapper, wrap_object, wrap_function_wrapper_failsafe, wrap_function_generic
from ..receiver import receiver_instance

from ..errors import ThreatstackError, RequestBlockedError, ThreatstackStackError
from ..config import CONF

from wrapt import importer, wrap_function_wrapper

MODULE_NAME = 'subprocess'

def _on_import_factory(module, raise_errors=True):
    """Factory to create an import hook for the provided module name"""
    def on_import(hook):

        methodList = ['call', 'check_call', 'check_output', 'run']
        for i,val in enumerate(methodList):
            wrap_function_wrapper_failsafe(module, val, wrap_function_generic(MODULE_NAME, val, receiver_instance()))    
    return on_import

def patch_subprocess():
    """wrap the subprocess module """  

    module = MODULE_NAME
    try:
        importer.when_imported(module)(_on_import_factory(module))
    except Exception as exc:
        _logger.debug('failed to patch %s', module)
        raise
        return False

def wrap_subprocess():
    """Called during agent initialization to instrument subprocess library

    """    
    patch_subprocess()
