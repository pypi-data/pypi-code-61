#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
setup(
    name='tdqm',
    version='0.0.0',
    description='Alias for typos of tqdm',
    long_description='Alias for typos of tqdm',
    long_description_content_type='text/x-rst',
    license='MPLv2.0',
    url='https://github.com/tqdm/tqdm',
    maintainer='tqdm developers',
    maintainer_email='python.tqdm@gmail.com',
    platforms=['any'],
    install_requires=['tqdm'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
    keywords='progressbar progressmeter progress bar meter'
             ' rate eta console terminal time',
)
