#!/usr/bin/env python
# encoding: utf-8

from setuptools import setup

setup(
    name='Bopytex',
    version='0.1.2',
    description='Command line tool for compiling latex with python command embedded',
    author='Benjamin Bertrand',
    author_email='programming@opytex.org',
    packages=['bopytex'],
    install_requires=[
        'mapytex',
        'mypytex',
        'click',
        ],
    entry_points={
        "console_scripts": ['bopytex=bopytex.script:new']
        },
    )

# -----------------------------
# Reglages pour 'vim'
# vim:set autoindent expandtab tabstop=4 shiftwidth=4:
# cursor: 16 del
