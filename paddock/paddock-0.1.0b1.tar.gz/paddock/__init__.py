import logging
from paddock.client import Paddock
import paddock.constants as constants
from .__version__ import (
    __title__,
    __description__,
    __url__,
    __version__,
    __author__,
    __author_email__,
    __license__,
    __copyright__,
)


__all__ = [
    "__title__",
    "__description__",
    "__url__",
    "__version__",
    "__author__",
    "__author_email__",
    "__license__",
    "__copyright__",
    "Paddock",
    "constants",
    "logger",
]


logger = logging.getLogger(__name__)
