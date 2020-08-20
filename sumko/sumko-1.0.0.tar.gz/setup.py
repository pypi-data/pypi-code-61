#!/usr/bin/env python
# coding: utf-8

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='sumko',
    version='1.0.0',
    author='fovegage',
    author_email='fovegage@gmail.com',
    url='https://github.com/fovegage/sumko',
    description='SumKo is a Python microservices framework that lets service developers concentrate on application logic and encourages testability.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[],
)
