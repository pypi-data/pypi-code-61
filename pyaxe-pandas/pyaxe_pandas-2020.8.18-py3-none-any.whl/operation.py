# !/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time  : 2020/8/17 下午6:10
# @Author: 张伟
# @EMAIL: Jtyoui@qq.com
# @Notes : 对算法操作
import os
import re

import pkg_resources
import yaml


class YamlPandas:
    def __init__(self, df, yml, **kwargs):
        """初始化加载pandas类型

        :param df: DataFrame类型
        :param yml: yml配置文件
        :param kwargs:
        """
        self.df = df
        self.yml = yml
        self.kwargs = kwargs

    def read_yaml(self):
        """读取Yml文件"""
        assert os.path.exists(self.yml), FileNotFoundError('yml文件不存在！')
        yaml_ls = []
        with open(self.yml)as fp:
            for yml in yaml.safe_load_all(fp):
                yaml_ls.append(yml)
        return yaml_ls

    def resolve_config(self, yaml_ls):
        """解析yaml配置集合
        :param yaml_ls: 配置文件
        :return: 自动分配结果

        >>> self.resolve_config(self.read_yaml())
        """
        pip = {dist.key: dist.parsed_version for dist in pkg_resources.working_set}
        assert pip.get('pandas'), ModuleNotFoundError('pandas模块没有安装')
        for yml in yaml_ls:
            current_version = pip['pandas'].base_version
            yml_version = yml['version']
            assert current_version == yml_version, ModuleNotFoundError(
                F'您安装的pandas版本是：{current_version},您配置的版本是：{yml_version},两个版本不一致。')
            operations = yml['operations']
            for operation in operations:
                opt = operation['operation']
                if opt.get('switch', None):
                    for flag in opt['switch']:
                        regex = flag['regex']
                        arg = flag['arg']
                        stop = flag.get('stop', False)
                        assert self.kwargs.get(arg), Exception(f'不存在{arg}参数')
                        if re.search(regex, self.kwargs[arg]):
                            yield self._exe(opt['name'], flag['exe'])
                            if stop:
                                break
                else:
                    yield self._exe(opt['name'], opt['exe'])

    def _exe(self, name, exe):
        """回调dataframe中的方法"""
        if hasattr(self.df, name):
            obj = getattr(self.df, name)
            return obj(exe)
