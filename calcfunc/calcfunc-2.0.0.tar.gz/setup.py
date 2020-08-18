#!pyhthon
# -*- coding:utf-8 -*-

from __future__ import print_function
from setuptools import setup, find_packages

# with open("README.md", "r", encoding="utf-8") as fh:
#     long_description = fh.read()

setup(
    name = "calcfunc",                                    #包名，避免重复冲突
    version = "2.0.0",                                    #版本号，更新时会寻找比当前高的版本号
    author = "Way Yan",                                   #作者信息
    autuor_email = "yansiwei@comac.intra",
    description = "simple calculate method",              #关于包的短描述
    long_description = "long_description",                #关于包的详细介绍，这里读入了README.md
    # long_description_content_type = "text/markdown",
    license = "MIT",                                      #授权方式 MIT license, APACHE license
    url = "http://git.mom.comac.int",                                             #项目地址，可以给git地址
    packages = find_packages(),                           #packages是包列表，setuptools.find_packages()可以自动找到目录下面的包
    # packages = ["calcfunc"],                            #手动寻到目录下面的闭包
    install_requires=[                                    #依赖的python模块
        ],
    classfiers = [                                        #分类信息，具体填写方式可以参考官方文档中的PyPl Classifiers来写
        "Topic = Math/Method"
        "Programming Language ::python"
    ],
)