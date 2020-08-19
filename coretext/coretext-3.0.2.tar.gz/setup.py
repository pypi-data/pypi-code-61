#!/usr/bin/env python
#
# Copyright (c) 2011 Jan Pomikalek
# All rights reserved.
#
# This software is licensed as described in the file COPYING, which
# you should have received as part of this distribution.

from distutils.core import setup

setup(
    name='coretext',
    version='3.0.2',
    description='Heuristic based boilerplate removal tool',
    long_description='''jusText is a tool for removing boilerplate content,
    such as navigation links, headers, and footers from HTML pages. It is
    designed to preserve mainly text containing full sentences and it is
    therefore well suited for creating linguistic resources such as Web
    corpora.''',
    author='Jan Pomikalek',
    author_email='jan.pomikalek@gmail.com',
    maintainer='Sitdhibong Laokok',
    maintainer_email='sitdhibong@gmail.com',
    url='http://corpus.tools/wiki/Justext',
    license='BSD',
    requires=['lxml (>=4.1)'],
    packages=['coretext'],
    package_data={'coretext': ['stoplists/*.txt']},
    scripts=['bin/coretext'],
)
