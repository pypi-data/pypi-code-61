"""
@author: zhangX
@license: (C) Copyright 1999-2020, NJ_LUCULENT Corporation Limited.
@contact: 494677221@qq.com
@file: services.py
@time: 2020/6/10 16:01
@desc:
"""

import abc


class Processor(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def __init__(self):
        self.model = None

    @abc.abstractmethod
    def load(self, model_path: str):
        pass

    @abc.abstractmethod
    def predict(self, data: list):
        pass
