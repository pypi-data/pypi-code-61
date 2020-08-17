from setuptools import setup, find_packages

REQUIRED_PACKAGES = ["tensorflow == 2.2.0"]

setup(
    name="tfr_image",
    version="1.0",
    license='MIT',
    url='https://github.com/jmarrietar/tfr_image',
    description="TFRimage is minimal tool to create TFRecords from a small dataset of images",
    packages=find_packages(),
)
