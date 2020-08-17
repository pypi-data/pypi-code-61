"""Instrumentation of os
"""

import six
import os

if six.PY2:
    import exceptions
    _exceptions_module = exceptions
elif six.PY3:
    import builtins
    _exceptions_module = builtins
else:
    _exceptions_module = None

from ..receiver import receiver_instance
from ..util.wrapper import queue_instrumentation_event
from ..util import logger
_logger = logger.getLogger(__name__)


def wrap_os_method(method_name, backup_name, receiver):
    def _wrapped_os_method(*args, **kwargs):
        _logger.debug('caught: %s', backup_name)
        # queue the event
        queue_instrumentation_event('os', method_name, args, receiver)
        # call the original method
        os_method = getattr(os, backup_name)
        os_method(*args, **kwargs)
    return _wrapped_os_method

def patch_os():
    """wrap the os module """

    method_list = ['execl', 'execle', 'execlp', 'execlpe', 'execv', 'execvp', 'execve', 'execvpe']
    for val in method_list:
        try:
            # check if method exists
            if not hasattr(os, val):
                continue
            backup_name = '_ts_' + val
            # check if already patched
            if hasattr(os, backup_name):
                continue

            # get original method that we're wrapping
            backup = getattr(os, val)
            # create wrapper method
            new_method = wrap_os_method(val, backup_name, receiver_instance())
            # backup original method to a new alias
            setattr(os, backup_name, backup)
            # override original method alias with wrapped method
            setattr(os, val, new_method)
        except Exception as exc:
            _logger.exception('Failed to patch os module')
            raise

def wrap_os():
    """Called during agent initialization to instrument os library
    """    
    patch_os()
