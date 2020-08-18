#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <zxyful@gmail.com>
# Date: 2019/11/20
# Desc: 

from zxutils.pyencrypt import str_to_md5, bytes_to_base64, base64_to_bytes


def test_build_hash():
    assert str_to_md5("hello") == "5d41402abc4b2a76b9719d911017c592"


def test_bytes_to_base64():
    assert bytes_to_base64(b'hello') == 'aGVsbG8='


def test_base64_to_bytes():
    assert base64_to_bytes("aGVsbG8=") == b'hello'