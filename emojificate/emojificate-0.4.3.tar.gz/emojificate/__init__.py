__version__ = "0.4.1"

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
