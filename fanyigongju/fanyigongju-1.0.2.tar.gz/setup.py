#!/bin/env python
# -*- coding:utf-8 -*-
# _author:ken

from setuptools import setup, find_packages

setup(
    name='fanyigongju',
    version='1.0.2',
    description=(
        '测试专用'
    ),
    long_description=open('README.rst').read(),
    author='ken',
    author_email='xiaomishaona@126.com',
    maintainer='ken',
    maintainer_email='xiaomishaona@126.com',
    license='BSD License',
    packages=find_packages(),
    # packages=['fanyigongju'],
    platforms=["all"],
    url='http://www.baidu.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries'
    ],
    install_requires=['certifi>=2020.6.20',
                    'chardet>=3.0.4',
                    'idna>=2.10',
                    'requests>=2.24.0',
                    'urllib3>=1.25.10']
)