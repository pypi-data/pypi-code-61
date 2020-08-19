from setuptools import setup

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'shuffle_dist_cards', 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='shuffle_dist_cards',
      version='0.1.1',
      description='Shuffle and distribute cards ',
      author='Ajinkya Joshi',
      author_email='ajinkya.dj92@gmail.com',
      packages=['shuffle_dist_cards'],
      long_description=long_description,
      long_description_content_type="text/markdown",
      zip_safe=False)