# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import hashlib

import six


def force_bytes(s, encoding='utf-8', strings_only=False, errors='strict'):
    """
    Similar to smart_bytes, except that lazy instances are resolved to
    strings, rather than kept as lazy objects.

    If strings_only is True, don't convert (some) non-string-like objects.
    """
    if isinstance(s, bytes):
        if encoding == 'utf-8':
            return s
        else:
            return s.decode('utf-8', errors).encode(encoding, errors)
    if strings_only and (s is None or isinstance(s, int)):
        return s
    if not isinstance(s, six.string_types):
        try:
            if six.PY3:
                return six.text_type(s).encode(encoding)
            else:
                return bytes(s)
        except UnicodeEncodeError:
            if isinstance(s, Exception):
                # An Exception subclass containing non-ASCII data that doesn't
                # know how to print itself properly. We shouldn't raise a
                # further exception.
                return b' '.join([force_bytes(arg, encoding, strings_only,
                                              errors) for arg in s])
            return six.text_type(s).encode(encoding, errors)
    else:
        return s.encode(encoding, errors)


def calculate_signature(params, appsecret):
    """

    :param dict params: {"sid": "123213", "appkey":"aaaaa", "timestamp": 1527821390 }
    :param str appsecret:
    :return:
    """

    assert 'sid' in params
    assert 'appkey' in params
    assert 'timestamp' in params
    _params = list(params.items())
    _params.sort()
    attr = []
    for key, val in _params:
        bit = "%02d-%s:%04d-%s" % (len(force_bytes(key)), key,
                                   len(force_bytes(val)), val)
        attr.append(bit)

    s = force_bytes(";".join(attr) + appsecret)
    m = hashlib.md5(s)
    return m.hexdigest()