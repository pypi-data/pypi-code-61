from setuptools import setup, find_packages
from io import open
from os import path

import pathlib
# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup (
    name = 'ckan-remote-dataloader',
    description = 'A simple commandline app for uploading tables to a remote CKAN datastore',
    version = '0.0.3',
    packages = find_packages(), 
    install_requires = [
        'click',
        'messytables'
    ],
    python_requires='>=3.6', 
    entry_points='''
        [console_scripts]
        ckanloader=ckanloader.__init__:main
    ''',
    author="John Keniston",
    keyword="ckan, datastore, remote, loader",
    long_description=README,
    long_description_content_type="text/markdown",
    license='MIT',
    url='https://github.com/jkgeo/ckan-remote-dataloader',
    download_url='https://github.com/jkgeo/ckan-remote-dataloader/archive/v0.0.0.tar.gz',
    dependency_links=[
        'https://github.com/jkgeo/ckanapi.git@f30afe2a788844188656f2eb0ef7f0e0e11186a9#egg=ckanapi'
    ],
    author_email='jfkeniston@gmail.com',
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ]
)