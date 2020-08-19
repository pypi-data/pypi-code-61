#!/bin/env python

from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='apolloapi',
    version='0.0.6',
    author='feichenxue',
    author_email='986024058@qq.com',
    url='',
    description=u'操作apollo的python客户端',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=['apolloapi']
)
