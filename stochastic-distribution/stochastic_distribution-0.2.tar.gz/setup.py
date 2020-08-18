from setuptools import setup

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='stochastic_distribution',
      version='0.2',
      description='Gaussian and Binomial distributions',
      packages=['stochastic_distribution'],
      author='Robert Csillag',
      author_email='csillagrobert95@gmail.com',
      long_description=long_description,
      long_description_content_type='text/markdown',
      zip_safe=False)