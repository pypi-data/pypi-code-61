from functools import wraps
import time
import sys
import os


def TypePrints(func):
    """Print func.__doc__ like type prints."""
    @wraps(func)
    def wrappers(*args, **kwargs):
        for c in func.__doc__:
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(0.08)
        sys.stdout.flush()
        sys.stdout.write('\n')
        return func(*args, **kwargs)
    return wrappers
