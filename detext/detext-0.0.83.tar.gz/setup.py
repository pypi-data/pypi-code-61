# Copyright (c) LinkedIn Corporation. All rights reserved. Licensed under the BSD-2 Clause license.
# See LICENSE in the project root for license information.
import sys
import setuptools
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

exec(open("src/detext/_version.py").read())
version = __version__

setuptools.setup(
    name='detext',
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=["Programming Language :: Python :: 3.7",
                 "Intended Audience :: Science/Research",
                 "Intended Audience :: Developers",
                 "License :: OSI Approved"],
    license='BSD-2-CLAUSE',
    version=version,
    package_dir={'': 'src'},
    packages=setuptools.find_packages('src'),
    include_package_data=True,
    install_requires=[] if version.endswith("dev0") else [
        'numpy<1.17',
        'smart-arg==0.0.5',
        'tensorflow==1.14.0',
        'tensorflow_ranking==0.1.4',
        'gast==0.2.2'
    ],
    tests_require=[
        'pytest',
    ])

setuptools.setup(
    name='li-detext',
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=["Programming Language :: Python :: 3.7",
                 "Intended Audience :: Science/Research",
                 "Intended Audience :: Developers",
                 "License :: OSI Approved"],
    license='BSD-2-CLAUSE',
    version=version,
    package_dir={'': 'src'},
    packages=setuptools.find_packages('src'),
    include_package_data=True,
    tests_require=[
        'pytest',
    ])
