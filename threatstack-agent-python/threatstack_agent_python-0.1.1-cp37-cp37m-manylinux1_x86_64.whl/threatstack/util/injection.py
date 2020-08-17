"""Check for SQLi

"""

import urllib
import six

if six.PY2:
    import exceptions
    _exceptions_module = exceptions
    from urllib import unquote_plus
elif six.PY3:
    import builtins
    _exceptions_module = builtins
    from urllib.parse import unquote_plus
else:
    _exceptions_module = None

from . import logger
_logger = logger.getLogger(__name__)

from libinjection import sqli_state,sqli_init,is_sqli,is_xss,is_sqli_simple
# create the data object
_libinjection_state = sqli_state()

def check_sqli(in_str):
    "check for sqli"
    _logger.debug('logging.check_sqli')    
    return is_sqli_simple(unquote_plus(str(in_str)), len(in_str))

def check_xss(in_str):
    "check for xss"
    _logger.debug('logging.check_xss')
    return is_xss(unquote_plus(str(in_str)), len(in_str), 0)
