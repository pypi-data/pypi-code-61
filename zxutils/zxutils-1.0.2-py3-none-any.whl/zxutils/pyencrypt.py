#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <zxyful@gmail.com>
# Date: 2019/11/20
# Desc: 


import base64
import hashlib

from zxutils.pystr import str_to_bytes


def str_to_md5(text):
    """

    :param text:
    :return:
    """
    m = hashlib.md5()
    m.update(str_to_bytes(text))
    return m.hexdigest()


def bytes_to_base64(bytes_data):
    """

    :return:
    """
    if not isinstance(bytes_data, bytes):
        raise ValueError("not bytes data.")

    base64_data = base64.b64encode(bytes_data)
    return base64_data.decode()


def base64_to_bytes(b64_data):
    """

    :param b64_data:
    :return:
    """
    if not isinstance(b64_data, str):
        raise ValueError("not b64 data.")

    return base64.b64decode(b64_data)
