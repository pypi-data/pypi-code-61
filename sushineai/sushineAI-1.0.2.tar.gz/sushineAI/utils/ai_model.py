"""
@author: zhangX
@license: (C) Copyright 1999-2019, NJ_LUCULENT Corporation Limited.
@contact: 494677221@qq.com
@file: ai_model.py
@time: 2020/4/26 20:27
@desc:
"""
import abc
from abc import ABC

from keras.models import load_model
import joblib


class AIModel(metaclass=abc.ABCMeta):

    def __init__(self):
        pass

    @abc.abstractmethod
    def fit(self, **kwargs):
        pass

    @abc.abstractmethod
    def transform(self, **kwargs):
        pass

    @abc.abstractmethod
    def predict(self, **kwargs):
        pass

    @abc.abstractmethod
    def load(self, **kwargs):
        pass

    @abc.abstractmethod
    def save(self, **kwargs):
        pass


class SklearnModel(AIModel, ABC):

    def __init__(self):
        super().__init__()

        self.model = None

    def fit(self, *args, **kwargs):
        pass

    def transform(self, *args, **kwargs):
        return self.model.transform(*args, **kwargs)

    def predict(self, *args, **kwargs):
        return self.model.predict(*args, **kwargs)

    def load(self, *args, **kwargs):
        self.model = joblib.load(kwargs.get('file_path'))

    def save(self, *args, **kwargs):
        pass


class KerasModel(AIModel, ABC):
    def __init__(self):
        super().__init__()

        self.model = None

    def fit(self, *args, **kwargs):
        pass

    def transform(self, *args, **kwargs):
        # return self.model.transform(*args, **kwargs)
        pass

    def predict(self, *args, **kwargs):
        return self.model.predict(*args, **kwargs)

    def load(self, *args, **kwargs):
        file_path = kwargs.get('file_path')
        self.model = load_model(file_path)

    def save(self, *args, **kwargs):
        pass


if __name__ == '__main__':
    c = SklearnModel()
    d = KerasModel()
    print()
