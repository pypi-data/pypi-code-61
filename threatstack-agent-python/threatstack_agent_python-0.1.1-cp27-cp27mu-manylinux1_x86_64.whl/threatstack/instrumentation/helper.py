"""
Instrumentation helper file
"""

import sys
from ..config import CONF
from ..util.injection import check_sqli, check_xss
from ..util import logger

_logger = logger.getLogger(__name__)

if sys.version_info[0] < 3:
    ALL_STRINGS_CLASS = basestring  # noqa
    STRING_CLASS = str
    UNICODE_CLASS = unicode  # noqa
else:
    ALL_STRINGS_CLASS = str
    STRING_CLASS = str
    UNICODE_CLASS = str

def is_unicode(value):
    """ Check if a value is a unicode string
    """
    return isinstance(value, UNICODE_CLASS)

def to_unicode(value):
    """ Decode a value if it's a unicode string
    """

    if value is None:
        return value
    # If value is a byte string (string without encoding)
    # Try to decode it as unicode, this operation will
    # always succeed because non UTF-8 characters will
    # get replaced by the UTF-8 replacement character.
    if isinstance(value, bytes):
        return value.decode("utf-8", errors="replace")
    # If the value is not already a unicode string
    # Try to convert it to a string
    # by calling the standard Python __str__ method on
    # the value.
    elif not is_unicode(value):
        value = STRING_CLASS(value)
        # In Python 2.7, the returned value has no encoding
        if isinstance(value, bytes):
            return value.decode("utf-8", errors="replace")
    # Value is already a unicode string
    return value

def flatten_json(json_obj):
    out = {}

    def flatten(x, name=''):
        if x and hasattr(x, 'to_dict') and callable(x.to_dict):
            x = x.to_dict()
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '.')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + '.')
                i += 1
        elif hasattr(x, 'items') and callable(x.items):
            for a, b in x.items():
                flatten(b, name + a + '.')
        else:
            out[name[:-1]] = x

    flatten(json_obj)
    return out

def check_for_attacks(obj):
    attacks = []
    if not obj:
        return attacks
    # flatten the object in case it has multiple nested levels / arrays...
    flat = flatten_json(obj)
    _logger.debug('Flattened parameters: %s', flat)
    # loop through flattened parameters and check for attack payloads
    for key, val in flat.items():
        # to unicode
        value = to_unicode(val)
        # ignore non string values
        if not isinstance(value, ALL_STRINGS_CLASS):
            continue

        _logger.debug('Checking parameter: key=%s, value=%s', key, value)

        # check for SQL injections
        is_sqli = check_sqli(value)
        # check for XSS payloads
        is_xss = check_xss(value)

        if is_sqli:
            msg = 'SQLInjection attempt detected'
            _logger.warning(msg + ': ' + value)
            attacks.append({
                'key': key,
                'value': value,
                'type': 'sqli',
                'details': {
                    'blocked': CONF['BLOCK_SQLI'],
                    'signature': None,  # TODO: fill this out later
                    'message': msg
                }
            })

        if is_xss:
            msg = 'XSS attempt detected'
            _logger.warning(msg + ': ' + value)
            attacks.append({
                'key': key,
                'value': value,
                'type': 'xss',
                'details': {
                    'blocked': CONF['BLOCK_XSS'],
                    'signature': None,  # TODO: fill this out later
                    'message': msg
                }
            })
    # return results
    return attacks
