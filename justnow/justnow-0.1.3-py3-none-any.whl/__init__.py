from importlib.metadata import version

from justnow.parser import EventParser  # noqa

try:
    __version__ = version("justnow")
except ImportError:
    pass
