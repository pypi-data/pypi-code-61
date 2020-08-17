from setuptools import setup, find_packages
from os import path

REQUIRED_PACKAGES = ["tensorflow == 2.2.0"]

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="tfr_image",
    version="1.2",
    license='MIT',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/jmarrietar/tfr_image',
    description="TFRimage is minimal tool to create TFRecords from a small dataset of images",
    packages=find_packages(),
)
