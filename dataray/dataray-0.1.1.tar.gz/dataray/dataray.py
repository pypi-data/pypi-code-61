import functools
from dataray.helper import structure_summary


class DataRay:
    def ray(self, request_func):
        @functools.wraps(request_func)
        def wrapper(*args, **kwargs):
            response = request_func(*args, **kwargs)
            structure_summary(response)
            return response
        return wrapper




