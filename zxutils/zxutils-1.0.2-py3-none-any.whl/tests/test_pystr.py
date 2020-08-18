#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <zxyful@gmail.com>
# Date: 2019/11/20
# Desc: 

from zxutils.pystr import bytes_to_str, str_to_bytes


def test_str_to_bytes():
    assert str_to_bytes("zx") == b'zx'
    assert str_to_bytes("一", encoding="gbk") == b'\xd2\xbb'
    assert str_to_bytes("一", encoding="gb2312") == b'\xd2\xbb'


def test_bytes_to_str():
    assert bytes_to_str(b'hello') == "hello"
    assert bytes_to_str(b'\xd2\xbb', encoding="gb2312") == "一"
