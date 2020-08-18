#! /usr/bin/env python3
"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

import os
import subprocess

import setuptools
from setuptools.dist import Distribution

import torch

# This is a hack around python wheels not including the adaptor.so library.
class BinaryDistribution(Distribution):
    def is_pure(self):
        return False

    def has_ext_modules(self):
        return True

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
LIBTORCH_DIR = torch.utils.cmake_prefix_path

if not os.path.exists('build'): os.mkdir('build')
os.chdir('build')
if subprocess.call(['cmake', '-DCMAKE_PREFIX_PATH=%s' % LIBTORCH_DIR, BASE_DIR]) != 0:
    raise RuntimeError('Cmake failed in directory: {}'.format(BASE_DIR))
if subprocess.call(['make', '--always-make']) != 0:
    raise RuntimeError('Make failed in directory: {}'.format(BASE_DIR))
os.chdir(BASE_DIR)

setuptools.setup(
    name='lanms-pytorch',

    version='1.0.3',

    description='Locality-Aware Non-Maximum Suppression, as a custom C++ operator in TorchScript.',

    # The project's main homepage.
    url='https://github.com/xhdhr10000/lanms',

    # Author details
    author='argmen (boostczc@gmail.com) is code author, '
           'Dominik Walder (dominik.walder@parquery.com) and Marko Ristin (marko@parquery.com) only packaged the code, '
           'xhdhr10000 (xhdhr2007@126.com) ported to TorchScript framework',
    author_email='xhdhr2007@126.com',

    # Choose your license
    license='GNU General Public License v3.0',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 5 - Production/Stable',

        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',

        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',

        'Programming Language :: Python :: 3.5',
    ],

    keywords='locality aware non-maximum suppression',

    packages=setuptools.find_packages(exclude=[]),

    install_requires=["torch >= 1.6.0"],

    include_package_data=True,
    distclass=BinaryDistribution,
)
