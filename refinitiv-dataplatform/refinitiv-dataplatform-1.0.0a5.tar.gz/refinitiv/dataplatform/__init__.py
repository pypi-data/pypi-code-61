# coding: utf-8
__version__ = '1.0.0a5'

"""
    refinitiv-dataplatform is a Python library to access Refinitiv Data Platform with Python.
"""

from .errors import *
from .core import *  # noqa
from .content import *  # noqa
from .delivery import *  # noqa
from .factory import *  # noqa
from .pricing import *  # noqa
from .content import ipa  # noqa
from .tools import _module_helper  # noqa
from .legacy.tools import get_default_session, close_session  # noqa

_module_helper.delete_reference_from_module(__name__, 'get_chain_async')
_module_helper.delete_reference_from_module(__name__, 'get_headlines')
_module_helper.delete_reference_from_module(__name__, 'get_headlines_async')
_module_helper.delete_reference_from_module(__name__, 'get_story')
_module_helper.delete_reference_from_module(__name__, 'get_story_async')
_module_helper.delete_reference_from_module(__name__, 'get_news_story_async')
_module_helper.delete_reference_from_module(__name__, 'News')
_module_helper.delete_reference_from_module(__name__, 'tools')
_module_helper.delete_reference_from_module(__name__, '_module_helper')
