"""A setuptools based setup module for seismic-format"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from codecs import open
from os import path
from setuptools import setup, find_packages

import seismic_format
#import versioneer

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as readme_file:
    readme = readme_file.read()

with open(path.join(here, 'HISTORY.rst'), encoding='utf-8') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

requirements = [
    # TODO: put package requirements here
    'click',
    'obspy',
]

test_requirements = [
    # TODO: put package test requirements here
    'obspy',
]

setup(
    name='seismic-format',
    #version=versioneer.get_version(),
    version=seismic_format.__version__,
    #cmdclass=versioneer.get_cmdclass(),
    description="Collection of tools for converting between different seismic formats",
    long_description=readme + '\n\n' + history,
    author="Mike Hagerty",
    author_email='mhagerty@isti.com',
    url='https://gitlab.isti.com/mhagerty/seismic-format',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    entry_points={
        'console_scripts':[
            #'seismic-format=seismic_format.cli:cli',
            'quakeml-to-y2k=seismic_format.quakeml_to_y2k:main',
            'y2k-to-quakeml=seismic_format.y2k_to_quakeml:main',
            'seisan-to-quakeml=seismic_format.seisan_to_quakeml:main',
            ],
        },
    include_package_data=True,
    package_data={
        'seismic_format':['formats/format*']
    },
    install_requires=requirements,
    license="MIT",
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements,
)
