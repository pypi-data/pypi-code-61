"""Generic Wrapper

"""

import six

from wrapt import FunctionWrapper, resolve_path, apply_patch, wrap_object, wrap_function_wrapper, function_wrapper

if six.PY2:
    import exceptions
    _exceptions_module = exceptions
elif six.PY3:
    import builtins
    _exceptions_module = builtins
else:
    _exceptions_module = None

from . import logger
_logger = logger.getLogger(__name__)


def post_function(function):
    @function_wrapper
    def _wrapper(wrapped, instance, args, kwargs):
        result = wrapped(*args, **kwargs)
        if instance is not None:
            function(instance, *args, **kwargs)
        else:
            function(*args, **kwargs)
        return result
    return _wrapper

def PostFunctionWrapper(wrapped, function):
    _logger.debug('PostFunctionWrapper wrapped=%s,function=%s', wrapped, function)
    return post_function(function)(wrapped)

def pre_function(function):
    @function_wrapper
    def _wrapper(wrapped, instance, args, kwargs):
        if instance is not None:
            function(instance, *args, **kwargs)
        else:
            function(*args, **kwargs)
        return wrapped(*args, **kwargs)
    return _wrapper

def PreFunctionWrapper(wrapped, function):
    return pre_function(function)(wrapped)


def wrap_function_wrapper_failsafe(module, name, wrapper):
    try:
        wrap_function_wrapper(module, name, wrapper)    
    except AttributeError as error: 
        _logger.debug('Failed wrapping module=%s,name=%s', module, name)


def queue_instrumentation_event(module_name, method_name, args, receiver):
    config = list()
    if args is not None:
        for value in args:
            if isinstance(value, six.string_types) is True:
                _logger.debug('%s, Appending value %s to the config', method_name, value)
                config.append(value)
            elif isinstance(value, list) is True:
                for i, val in enumerate(value):
                    _logger.debug('%s, Appending list value %s to config', method_name, val)
                    config.append(val)

    event_dict = {
        'module_name': module_name,
        'method_name': method_name,
        'payload': {
            'arguments': config
        }
    }
    receiver.set_event(event_dict)


def wrap_function_generic(module_name, method_name, receiver_instance):
    def _wrapped(wrapped, instance, args, kwargs):
        _logger.debug('Inspecting %s, args=%s, kwargs=%s', method_name, args, kwargs)
        queue_instrumentation_event(module_name, method_name, args, receiver_instance)
        return wrapped(*args, **kwargs)
    return _wrapped
