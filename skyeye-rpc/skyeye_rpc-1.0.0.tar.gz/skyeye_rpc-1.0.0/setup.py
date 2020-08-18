# -*- coding: utf-8 -*-
import re

from setuptools import setup

#with open("skyeye_rpc/__init__.py",encoding="utf8") as f:
#    version = re.search(r'__version__ = "(.*?)"', f.read()).group(1)
version = '1.0.0'
setup(
    name="skyeye_rpc",
    version=version,
    install_requires=[
        "msgpack",
    ],
    extras_require={
        "redis": ["redis"],
        "grpc": ["grpcio"],
    },
)
