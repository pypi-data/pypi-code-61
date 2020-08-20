"""
@author: zhangX
@license: (C) Copyright 1999-2019, NJ_LUCULENT Corporation Limited.
@contact: 494677221@qq.com
@file: model_operator.py
@time: 2020/4/21 19:48
@desc:
"""

import joblib
from .ai_model import SklearnModel, KerasModel


def sklearn_saver(**kwargs):
    model = kwargs.get('model')
    path = kwargs.get('path')
    joblib.dump(model, path)


def sklearn_loader(**kwargs):
    path = kwargs.get('path')
    flag = kwargs.get('flag')
    sklearn_model = SklearnModel()
    sklearn_model.load(file_path=path)
    if flag:
        return sklearn_model.model
    else:
        return sklearn_model


def keras_saver(**kwargs):
    model = kwargs.get('model')
    path = kwargs.get('path')
    # 保存模型及结构,如果训练时有自定义loss 或 metrics，载入会报错
    model.save(path)


def keras_loader(**kwargs):
    path = kwargs.get('path')
    flag = kwargs.get('flag')
    keras_model = KerasModel()
    keras_model.load(file_path=path)
    if flag:
        return keras_model.model
    else:
        return keras_model


class ModelOperator:
    save_opt = {'sklearn': sklearn_saver, 'keras': keras_saver}
    load_opt = {'sklearn': sklearn_loader, 'keras': keras_loader}

    @classmethod
    def save(cls, model, path, model_type):
        cls.save_opt[model_type](model=model, path=path)

    @classmethod
    def load(cls, path, model_type, flag):
        return cls.load_opt[model_type](path=path, flag=flag)
