from setuptools import setup, find_packages

REQUIRED_PACKAGES = ["tensorflow == 2.2.0"]

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="tfr_image",
    version="1.1",
    license='MIT',
    url='https://github.com/jmarrietar/tfr_image',
    description="TFRimage is minimal tool to create TFRecords from a small dataset of images",
    packages=find_packages(),
)
