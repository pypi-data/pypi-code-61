#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : WeiWang Zhang
@Time    : 2020-08-20 16:11
@File    : decorator.py
@Software: PyCharm
@Desc    : 装饰器类
"""


class Decorator(object):
    def __init__(self, func_or_name=None):
        """
        自定义装饰器
        任何类只要继承自该类，并实现其中wrapper方法，在wrapper中执行self._function(*args, **kwargs)
        就可以作为一个函数装饰器来使用

        该函数装饰器可以使用两种初始化方式
        1、无参初始化
        @Decorator
        def func(*args):
            ......
            pass

        2、带参初始化，此处参数可以自定义,
        但是第一个列表参数即func_or_name不能为可执行函数,
        否则该函数会成为装饰器的目标函数
        class controller(Decorator):
            ......
            pass

        @controller(func_or_name="name", method="POST")
        def func(*args)
            ......
            pass


        :param func_or_name:
        """
        self._function = None
        self._name = None
        # 检查第一个参数是否为可执行函数
        if callable(func_or_name):
            self._function = func_or_name
            self._name = func_or_name.__qualname__
        else:
            self._name = func_or_name

    def __decorator(self, func):
        if not callable(func):
            raise ValueError("@%s 注解使用错误,需要置于可执行函数上方" % self.__class__.__name__)
        self._function = func
        if self._name is None:
            self._name = func.__qualname__
        return self.wrapper

    def __call__(self, *args, **kwargs):
        # 检查目标函数是否已经注册，如果还没有，说明是带参调用形式
        if self._function is None:
            return self.__decorator(*args, **kwargs)
        else:
            # 如果目标函数已注册，则进行主包装函数
            return self.wrapper(*args, **kwargs)

    def wrapper(self, *args, **kwargs):
        """
        目标包装函数，被装饰器装饰的函数的入参会原封不动的输入
        wrapper, 并有wrapper函数转交self.__function
        该wrapper，为装饰器类的核心功能，需要具体实现。
        :param args:
        :param kwargs:
        :return:
        """
        raise NotImplementedError
