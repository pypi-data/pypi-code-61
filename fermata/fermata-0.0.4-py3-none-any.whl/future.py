

class cached_property:
    '''A thread unsafe cached_property implementation.
    '''

    def __init__(self, func):
        self.func = func
        self.__doc__ = func.__doc__

    def __set_name__(self, _, name):
        self.__name__ = name

    def __get__(self, instance, _=None):
        if instance is None:
            return self
        instance.__dict__[self.__name__] = self.func(instance)

        return instance.__dict__[self.__name__]


class singledispatchmethod:
    '''A poor implementation for type dispatch.
       WARNING: this is not an equivalent `singledispatchmethod` in python 3.8
    '''

    def __init__(self, func):
        self.func = func
        self.dispatcher = {}

    def register(self, cls):
        def wrap(method):
            self.dispatcher[cls] = method
            return method

        return wrap

    def __get__(self, obj, cls=None):
        def _method(*args, **kwargs):
            method = self.dispatcher.get(args[0].__class__, self.func)
            return method.__get__(obj, cls)(*args, **kwargs)

        _method.__name__ = self.func.__name__
        _method.__doc__ = self.func.__doc__

        return _method
