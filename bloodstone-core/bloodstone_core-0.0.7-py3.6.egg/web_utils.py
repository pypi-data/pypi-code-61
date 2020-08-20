#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : WeiWang Zhang
@Time    : 2019-09-19 14:33
@File    : web_utils.py
@Desc    : 基于注解装饰器的切面工具
"""
import traceback
import logging
from django.http import HttpResponse
from django.http import HttpRequest
from wmpy_util.json_util import json_power_dump
import json
import numpy as np
import time
from django.utils.datastructures import MultiValueDictKeyError
from wmpy_util.decorator import *

logger = logging.getLogger("django_logger")


class ServiceException(Exception):
    def __init__(self, err='service error!'):
        Exception.__init__(self, err)


class IllegalDataException(Exception):
    def __init__(self, err='Illegal data error!', code=1, ):
        Exception.__init__(self, err)
        self.code = code
        self.message = err


class controller(Decorator):
    def __init__(self, func_or_name=None, method=None):
        super().__init__(func_or_name=func_or_name)
        if method is not None:
            method = method.upper()
        self.method = method

    def wrapper(self, *args, **kwargs):
        param = dict()
        # 初始化返回对象
        response_data = dict(code=20001, message="", result=None)
        request = None
        try:
            for arg in args:
                if isinstance(arg, HttpRequest):
                    request = arg
                    break
            if request is None:
                raise AttributeError("not request arg!")
            if request.method == 'POST':
                param = request.POST
            elif request.method == 'GET':
                param = request.GET
        except:
            logger.error(traceback.format_exc())
        start = time.time()
        try:
            if isinstance(request, HttpRequest) and self.method is not None:
                if not self.method == request.method:
                    raise ServiceException("请求类型错误，需要为{}".format(self.method))
            response_data = self._function(*args, **kwargs)
        except (ServiceException, IllegalDataException) as error:
            logger.error(str(error))
            response_data["message"] = str(error)
        except (MultiValueDictKeyError, OSError) as error:
            logger.error("图片参数错误" + traceback.format_exc())
            response_data["message"] = "图片参数错误"
        except (ValueError, KeyError) as error:
            logger.error(" 内部错误 " + traceback.format_exc())
            response_data["message"] = "PY内部错误，请联系管理员"
        except Exception as error:
            logger.error(traceback.format_exc())
            response_data["message"] = "PY系统错误"
        rece_param = json.dumps(param)
        spend = int((time.time() - start) * 1000)
        if isinstance(response_data, HttpResponse):
            logger.info("%s receive_param=%s" % (self._name, rece_param))
            return response_data
        else:
            ret_str = json_power_dump(response_data)
            logger.info(
                "%s receive_param=%s,  respond = %s, time_spend = %dms" %
                (self._name, get_cutted_param_string(param, 200), ret_str, spend))
            callback = param.get("callback")
            if callback is not None:
                ret_str = "%s(%s)" % (callback, ret_str)
            return HttpResponse(ret_str, content_type='application/json')


def get_cutted_param_string(param, len_limit=500):
    new_param = dict()
    for key in param:
        value = str(param[key])
        if len(value) > len_limit:
            value = value[:len_limit]
            value += "...(over %d)" % len_limit
        new_param[key] = value
    return str(new_param)


def kwargs_resolver(**kwargs):
    def decorator(func):
        _name = func.__name__
        _default_kwargs = kwargs

        def wrapper(*args, **kwargs):
            _default_kwargs_clone = dict(_default_kwargs)
            param = None
            try:
                request = None
                for arg in args:
                    if isinstance(arg, HttpRequest):
                        request = arg
                        break
                if request is not None:
                    if request.method == 'POST':
                        param = request.POST
                    elif request.method == 'GET':
                        param = request.GET
            except Exception as e:
                print("Resolve args failed:%s" % str(e))
            if param is not None:
                for key in _default_kwargs_clone:
                    _default_value = _default_kwargs_clone[key]
                    param_value = param.get(key)
                    if param_value is not None:
                        # 如果默认值不为None，则按照默认值的type对参数进行规范
                        if _default_value is None:
                            _default_kwargs_clone[key] = param_value
                        else:
                            _default_type = type(_default_value)
                            _default_kwargs_clone[key] = _default_type(param_value)
            kwargs.update(_default_kwargs_clone)
            ret = func(*args, **kwargs)
            return ret

        wrapper.__name__ = _name
        return wrapper

    return decorator


if __name__ == '__main__':
    pass
