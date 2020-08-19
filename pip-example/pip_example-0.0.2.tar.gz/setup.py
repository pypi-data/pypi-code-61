from setuptools import setup, find_packages
import sys

description = '实现加法，练习将自己的项目打包成pip'
name = 'pip_example'
install_requires = ['numpy>=1.15.3', 'scipy>=1.2.1', 'django>=2.1']
classifiers = [
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
]
setup(author='pengbin',
      author_email='2972768451@qq.com',
      description=description,
      license=license,
      long_description=description,
      install_requires=install_requires,
      maintainer='pengbin',
      name=name,
      packages=find_packages(),
      platforms='windows',
      version='0.0.2',
      classifiers=classifiers,
      python_requires='>=3.5.2', )
