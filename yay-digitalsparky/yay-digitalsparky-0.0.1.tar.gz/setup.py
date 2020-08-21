#!/usr/bin/env python

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "yay-digitalsparky",
    version = "0.0.1",
    author = "Matt Spurrier",
    author_email = "matthew@spurrier.com.au",
    url = 'https://github.com/digitalsparky/python-yay',
    py_modules = ['yay'],
    keywords = ['yay', 'arch linux'],
    description='Simple Python interface to Arch Linux package manager (yay)',
    long_description = long_description,
    download_url = 'https://github.com/digitalsparky/python-yay/archive/0.0.1.tar.gz',
    packages = setuptools.find_packages(),
    license = 'GPLv3',
    classifiers = [
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: Unix",
        "Topic :: System :: Software Distribution",
    ],
    python_requires = '>=3.6',
)