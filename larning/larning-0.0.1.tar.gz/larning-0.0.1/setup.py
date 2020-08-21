#! /usr/bin/env python
import sys

if sys.version_info[:2] < (3, 6):
    raise RuntimeError("Python version >= 3.6 required.")


try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

MAJOR = 0
MINOR = 0
MICRO = 1
VERSION = f"{MAJOR}.{MINOR}.{MICRO}"

setup(
  name='larning',
  version=VERSION,
    author='Tasnádi Gábor',
    author_email='tasi.gabi97@gmail.com',
    description='larning',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/tasigabi97/larning',
    download_url='https://github.com/tasigabi97/larning/archive/v_0.0.tar.gz',
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Physics",
    ],
    install_requires=["twine", "black", "pytest","wheel"],
    keywords=['larning', ],
    license='MIT',

)

