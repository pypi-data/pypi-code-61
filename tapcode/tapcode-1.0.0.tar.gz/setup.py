#!/usr/bin/env python3

import pathlib
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt') as f:
    required = f.read().splitlines()



# This call to setup() does all the work
setup(
    name="tapcode",
    version="1.0.0",
    description="Prisoner's tap code encryption",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords='crypto cryptography tapcode cipher encryption ctf ctf-tool',
    url="https://github.com/remiflavien1/tapcode",
    author="shadawck",
    author_email="hug211mire@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["tapcode"],
    include_package_data=True,   
    install_requires=required,
    entry_points={
        "console_scripts": [
            "tapcode=tapcode.__main__",
        ]
    },
)