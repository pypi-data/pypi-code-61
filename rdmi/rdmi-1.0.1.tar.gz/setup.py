#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

from setuptools import setup, find_packages

import rdmi

setup(
    name='rdmi',
    version='1.0.1',
    packages=['rdmi'],
    author='Kanchen Monnin',
    author_email='kanchen@mail.com',
    description='Print a range of numbers in random order',
    long_description="README on github : https://github.com/Teal-Projects/rdmi",
    install_requires=[
        'sys',
        'random',
    ],
    url='https://github.com/Teal-Projects/rdmi',
    classifiers=[
        'Programming Language :: Python',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',      
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',   
        'Programming Language :: Python :: 3',     
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    entry_points={
        'console_scripts': [
            'rdmi = rdmi.rdmi:main',
        ],
    },
)
