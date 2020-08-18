#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <zxyful@gmail.com>
# Date: 2019/11/20
# Desc: 

from urllib.parse import quote, unquote, urlparse
from urllib.request import Request, urlopen


def build_url(url, params):
    """Build a complete parameterized URL
    :argument:
    - `url`:  string, received base_url like this: https://www.example.com
    - `params`:  dict, received params like this: {'name': 'upg', 'age': 11}

    :return string https://www.example.com/?name=upg&age=11
    """
    if not isinstance(url, str) and not isinstance(params, dict):
        raise ValueError()

    if url[-1] != '?':
        url += '?'

    key_values = []
    for k, v in params.items():
        if not v:
            continue
        value = quote(str(v))
        key_values.append("{}={}".format(k, value))

    return url + "&".join(key_values)


def unpack_url(url):
    """Separating URLs with parameters
    :argument:
    - `url`:  string, received base_url like this:
             https://www.example.com/?name=upg&age=11
    :return ('https://www.example.com', {'name': 'upg', 'age': 11})
    :rtype tuple
    """
    if not isinstance(url, str):
        raise TypeError()

    part = url.split('?')
    if len(part) < 2:
        raise ValueError()

    base_url, params_url = url.split('?')

    params = params_url.split('&')
    values = dict()
    for param in params:
        key, value = param.split('=')
        if value.isnumeric():
            value = int(value)
        else:
            value = unquote(value)
        values.update({key: value})

    return base_url, values


def get_page(url):
    """
    Make a network request
    :param url:
    :return:
    """
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                             "Chrome/78.0.3904.97 Safari/537.36",
               "Accept": "*/*",
               "Accept-Encoding": "gzip, deflate",
               "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
               "Cache-Control": "no-cache",
               "Connection": "keep-alive",
               "Pragma": "no-cache",
               "Host": urlparse(url).hostname,
               "DNT": "1"
               }
    req = Request(url, headers=headers)
    res = urlopen(req)
    assert res.status == 200
    # res.headers
    page_source = res.read()
    return page_source
