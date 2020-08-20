"""Setup script for realpython-reader"""

import os
from setuptools import setup, find_packages

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(BASE_DIR, 'README.md'), 'r') as f:
    long_description = f.read()

setup(
    name="pyfrontend",
    version="1.0.0",
    author="Sarmad Gulzar",
    author_email="sarmadgulzar@outlook.com",
    description="Make websites using Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sarmadgulzar/pyfrontend",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
)
