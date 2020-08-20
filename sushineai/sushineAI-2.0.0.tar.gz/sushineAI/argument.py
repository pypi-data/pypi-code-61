"""
@author: zhangX
@license: (C) Copyright 1999-2019, NJ_LUCULENT Corporation Limited.
@contact: 494677221@qq.com
@file: argument.py
@time: 2020/4/26 12:24
@desc:
"""

import argparse

from sushineAI.utils.storager import Hdfs, Kafka
from sushineAI.utils.translator import DictToStruct

STORAGER = {'hdfs': Hdfs,
            'kafka': Kafka}


class Argument:
    """
    变量父类
    """

    def __init__(self, argument_keys):
        self.argument_keys = argument_keys

    def complex_args(self, component_port):
        parser = argparse.ArgumentParser()
        parser.add_argument("--" + component_port)
        args = parser.parse_known_args()[0]
        params = args.__dict__.get(component_port)
        if params is None:
            return {}
        try:
            params = eval(params)
        except:
            if component_port == 'preModel':
                return None
            else:
                raise ValueError("Invaild {} ,please check the parameters of component.".format(component_port))
        return params

    def run(self, component_port):
        pass


class Csv(Argument):
    """
    结构为Csv
    """

    def __init__(self, key):
        super().__init__(key)

    def complex_args(self, component_port):
        params = super().complex_args(component_port=component_port)
        return params.get(self.argument_keys)

    def run(self, component_port):
        params = self.complex_args(component_port=component_port)
        params = DictToStruct(**params)
        storager = STORAGER.get(params.storager)
        storer = storager(params.conInfo, file_type='Csv')
        return storer


class Model(Argument):
    """
    结构为模型
    """

    def __init__(self, key, model_type=None):
        super().__init__(key)
        self._model_type = model_type

    def complex_args(self, component_port):
        params = super().complex_args(component_port=component_port)
        return params.get(self.argument_keys)

    def run(self, component_port):
        params = self.complex_args(component_port=component_port)
        params = DictToStruct(**params)
        storager = STORAGER.get(params.storager)
        storer = storager(params.conInfo, file_type='Model', model_type=self._model_type)
        return storer


class StringOfDict(Argument):
    def __init__(self, key):
        super().__init__(key)

    def complex_args(self, component_port):
        params = super().complex_args(component_port=component_port)
        return params

    def run(self, component_port):
        params = self.complex_args(component_port=component_port)
        return params


class StringOfList(Argument):
    def __init__(self, key):
        super().__init__(key)

    def complex_args(self, component_port):
        params = super().complex_args(component_port=component_port)
        return params

    def run(self, component_port):
        params = self.complex_args(component_port=component_port)
        return params.get(self.argument_keys).split(',')


class String(Argument):
    def __init__(self, key):
        super().__init__(key)

    def complex_args(self, component_port):
        params = super().complex_args(component_port=component_port)
        return params

    def run(self, component_port):
        params = self.complex_args(component_port=component_port)
        return params.get(self.argument_keys).split(',')[0]


class PreModel(Argument):
    def __init__(self, key, model_type=None):
        super().__init__(key)
        self._model_type = model_type

    def complex_args(self, component_port):
        params = super().complex_args(component_port=component_port)
        return params

    def run(self, component_port):
        params = self.complex_args(component_port=component_port)
        if not params:
            return None
        else:
            params = DictToStruct(**params)
            storager = STORAGER.get(params.storager)
            storer = storager(params.conInfo, file_type='Model', model_type=self._model_type)
            return storer


class File(Argument):
    def __init__(self, key, file_type):
        super().__init__(key)
        assert file_type in [None, 'Json', 'Image'], TypeError('file_type must be Json , Image or None!')
        self._file_type = file_type

    def complex_args(self, component_port):
        params = super().complex_args(component_port=component_port)
        return params.get(self.argument_keys)

    def run(self, component_port):
        params = self.complex_args(component_port=component_port)
        if params is None:
            return None
        else:
            params = DictToStruct(**params)
            storager = STORAGER.get(params.storager)
            storer = storager(params.conInfo, file_type=self._file_type)
            return storer
