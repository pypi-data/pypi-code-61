#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <zxyful@gmail.com>
# Date: 2019/11/20
# Desc: 

from zxutils.pyurl import build_url, get_page, unpack_url


def test_get_page():
    test_url = "https://ss0.bdstatic.com/5aV1bjqh_Q23odCf/static/superlanding/img/logo_top.png"
    assert get_page(test_url) is not None


def test_build_url():
    base_url = "https://www.example.com"
    assert build_url(base_url, {"name": "zx"}) == "https://www.example.com?name=zx"


def test_unpack_url():
    test_url = "https://www.example.com?name=zx&age=11"
    assert unpack_url(test_url) == ("https://www.example.com", {"name": "zx", "age": 11})
