#!/usr/bin/env python

f = open('./README.md', 'r')
from setuptools import setup    
setup(name='qdill',
      version='1.1',
      description='tiny convenience lib for dill',
      long_description= f.read(),
      long_description_content_type='text/markdown',
      author='madgen',
      author_email='madgencontent@gmail.com',
      url='https://github.com/madgen-content/qdill',
      install_requires=['dill'],
      packages=['qdill']
     )
f.close()