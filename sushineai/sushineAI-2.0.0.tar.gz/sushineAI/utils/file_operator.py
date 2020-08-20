"""
@author: zhangX
@license: (C) Copyright 1999-2019, NJ_LUCULENT Corporation Limited.
@contact: 494677221@qq.com
@file: file_operator.py
@time: 2020/4/15 14:50
@desc:
"""
import os
from pandas import read_csv
from .model_operator import ModelOperator
import json


def save_json(**kwargs):
    data = kwargs.get('data')
    local_path = kwargs.get('local_path')

    with open(local_path+'/json.json', 'w',encoding='utf-8') as f:
        json.dump(data, f)
    return 'json.json'


def save_csv(**kwargs):
    data = kwargs.get('data')
    local_path = kwargs.get('local_path')
    data.to_csv('{}/data.csv'.format(local_path),
                index=False, encoding='utf-8')
    return 'data.csv'


def save_image(**kwargs):
    data = kwargs.get('data')
    local_path = kwargs.get('local_path')
    data.savefig('{}/plot.png'
                 .format(local_path))
    return 'plot.png'


def save_model(**kwargs):
    data = kwargs.get('data')
    local_path = kwargs.get('local_path')
    model_type = kwargs.get('model_type')
    ModelOperator.save(model=data, path=local_path + '{}.model'.format(model_type), model_type=model_type)
    return '{}.model'.format(model_type)


def load_csv(**kwargs):
    fs = kwargs.get('fs')
    remote_path = kwargs.get('remote_path')
    local_path = kwargs.get('local_path')

    fs.download(remote_path + '/data.csv', local_path + '/data.csv', overwrite=True)
    return read_csv(local_path + '/data.csv', encoding='utf-8')


def load_model(**kwargs):
    fs = kwargs.get('fs')
    remote_path = kwargs.get('remote_path')
    local_path = kwargs.get('local_path')
    model_type = kwargs.get('model_type')

    model_type_known_flag = True
    # 这里解析模型文件类型
    if model_type is None:
        model_type_known_flag = False
        model_files = fs.list(remote_path)
        for file in model_files:
            if file.__contains__('sklearn'):
                model_type = 'sklearn'
                break
            if file.__contains__('keras'):
                model_type = 'keras'
                break

    fs.download(remote_path + '{}.model'.format(model_type), local_path + '{}.model'.format(model_type),
                overwrite=True)
    model = ModelOperator.load(path=local_path + '{}.model'.format(model_type), model_type=model_type, flag=model_type_known_flag)

    return model


class FileOperator:
    save_opt = {'Csv': save_csv,
                'Image': save_image,
                'Model': save_model,
                'Json': save_json}

    read_opt = {'Csv': load_csv,
                'Model': load_model}

    @classmethod
    def save(cls, data, local_path, data_type, model_type):
        try:
            os.makedirs(local_path)
        except FileExistsError:
            pass
        return cls.save_opt[data_type](data=data, local_path=local_path, model_type=model_type)

    @classmethod
    def read(cls, fs, remote_path, local_path, data_type, model_type):
        return cls.read_opt[data_type](fs=fs, remote_path=remote_path, local_path=local_path, model_type=model_type)
