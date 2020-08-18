from inspect import iscoroutinefunction
from typing import Callable


async def run_func(func: Callable, *args, **kwargs):
    """Run a function which can be asynchronous or not."""
    result = func(*args, **kwargs)
    if iscoroutinefunction(func):
        # Await it
        return await result
    return result
