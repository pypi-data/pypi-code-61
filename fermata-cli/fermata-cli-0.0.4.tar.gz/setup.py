# -*- coding: utf-8 -*-
import setuptools

with open("README.md") as f:
    # long_description = f.read()
    long_description = 'just for test'

setuptools.setup(
    name="fermata-cli",
    version="0.0.4",
    author="rejown",
    author_email="rejown@gmail.com",
    description="Command Line Interface of Fermata",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://fenda.io/ff/fermata-cli",
    packages=['fermata_cli'],
    entry_points={
        'console_scripts': ['fermata=fermata_cli:main'],
    },
    python_requires='>=3.6',
    install_requires=[
        'fermata',
        'docopt',
        'werkzeug',
        'meinheld',
        'pyyaml',
        'coloredlogs',
    ],
    tests_require=[
        'pytest',
    ],
)
