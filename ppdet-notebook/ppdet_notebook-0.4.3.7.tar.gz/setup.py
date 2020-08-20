#!/bin/bash
# -*- encoding: utf-8 -*-
import os
import setuptools

this_directory = os.path.abspath(os.path.dirname(__file__))
# 读取文件内容
def read_file(filename):
    with open(os.path.join(this_directory, filename)) as f:
        long_description = f.read()
    return long_description
# 获取依赖
def read_requirements(filename):
    return [line.strip() for line in read_file(filename).splitlines()
            if not line.startswith('#')]

setuptools.setup(
    name='ppdet_notebook',
    version='0.4.3.7',
    author='tianzhi',
    author_email='ylj_yanglijuan@163.com',
    url='https://github.com/PaddlePaddle/PaddleDetection',
    description=u'PaddleDetection for notebook',
    packages=setuptools.find_packages(),
    include_package_data=True,    # 启用清单文件MANIFEST.in
    install_requires=["tqdm", "typeguard; python_version >= '3.4'","visualdl >= 2.0.0b;python_version >= '3.4'","opencv-python", "PyYAML", "shapely"],  # 依赖列表
    # exclude_package_date={'':['.gitignore']},
    dependency_links=[    # 依赖包下载路径
    ],
    entry_points={
        'console_scripts': []
    }
)
