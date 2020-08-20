# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import os
import sys

version = '0.5'


def long_description(*desc):
    text = []
    for d in desc:
        with open(d) as f:
            text.append(f.read())
    return '\n\n'.join(text)

tests_require = ['pytest']

setup(name='dolmen.collection',
      version=version,
      description="Collection of named entities",
      long_description=long_description(
          "README.txt",
          os.path.join("docs", "HISTORY.txt")),
      classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='collection library',
      author='Dolmen Team',
      author_email='dolmen@list.dolmen-project.org',
      url='http://pypi.python.org/pypi/dolmen.collection',
      license='BSD',
      package_dir={'': 'src'},
      packages=find_packages('src'),
      namespace_packages=['dolmen', ],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'zope.interface',
          ],
      tests_require=tests_require,
      extras_require={'test': tests_require},
      )
