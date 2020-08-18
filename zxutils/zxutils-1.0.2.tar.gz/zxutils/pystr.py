#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <zxyful@gmail.com>
# Date: 2019/11/20
# Desc: 


def str_to_bytes(text, encoding='utf-8'):
    """
    String to bytes
    :param text:
    :param encoding:
    :return:
    """
    if not isinstance(text, str):
        raise ValueError("not string.")

    return text.encode(encoding=encoding)


def bytes_to_str(bytes_data, encoding='utf-8'):
    """

    :param bytes_data:
    :param encoding:
    :return:
    """
    if not isinstance(bytes_data, bytes):
        raise ValueError("not bytes.")

    return str(bytes_data, encoding=encoding)
