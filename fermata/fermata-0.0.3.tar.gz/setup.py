# -*- coding: utf-8 -*-
import setuptools

import fermata

with open("README.md") as f:
    # long_description = f.read()
    long_description = 'just for test'

setuptools.setup(
    name="fermata",
    version=fermata.__version__,
    author="rejown",
    author_email="rejown@gmail.com",
    description="A WSGI Server Implementation of OpenAPI 3.0 in Python3.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://fenda.io/ff/fermata",
    packages=['fermata', 'fermata.openapi', 'fermata.ext.apm'],
    python_requires='>=3.6',
    install_requires=[
        'jsonschema',
    ],
    tests_require=[
        'pytest',
    ],
)
