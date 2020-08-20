"""
@author: zhangX
@license: (C) Copyright 1999-2019, NJ_LUCULENT Corporation Limited.
@contact: 494677221@qq.com
@file: translator.py
@time: 2020/4/11 19:42
@desc:
"""


def transform_params_type(arg, param_type, default):
    if param_type is bool:
        return param_type(arg)
    elif arg == "":
        return default
    else:
        return param_type(arg)


class DictToStruct:
    def __init__(self, **entries):
        self.__dict__.update(entries)
