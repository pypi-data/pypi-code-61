# !/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time  : 2020/8/18 下午5:44
# @Author: 张伟
# @EMAIL: Jtyoui@qq.com
# @Notes : 对flask-requests进行改进
import json
from json.decoder import JSONDecodeError
from urllib.parse import unquote


def flask_request(request):
    """获取flask中的传入参数"""
    if request.method == 'POST':
        return post_request(request)
    elif request.method == 'GET':
        return get_request(request)


def post_request(request):
    """获取POST接口参数"""
    content = request.content_type
    if 'application/x-www-form-urlencoded' == content:
        data = request.form
    elif 'application/json' == content:
        data = request.json
    else:
        raw = request.data.decode(request.charset)
        try:
            data = json.loads(raw)
        except JSONDecodeError:
            if '=' in raw:
                q = unquote(raw)
                data = {i[:i.find('=')]: i[i.find('=') + 1:] for i in q.split('&')}
            else:
                return None
    return data


def get_request(request):
    """获取GET参数"""
    data = request.args
    return data
