from functools import wraps
from .settings import logging

logger = logging.getLogger(__name__)


def Error_Log(func):
    """Decorator for logging Exception but not stop the program."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logger.warning(f'{func.__name__}:{e}', exc_info=True)
    return wrapper
