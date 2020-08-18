from setuptools import setup, find_packages
from io import open
from os import path

import pathlib
# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# automatically captured required modules for install_requires in requirements.txt
with open(path.join(HERE, 'requirements.txt'), encoding='utf-8') as f:
    all_reqs = f.read().split('\n')

install_requires = [x.strip() for x in all_reqs if ('git+' not in x) and (
    not x.startswith('#')) and (not x.startswith('-'))]
dependency_links = [x.strip().replace('git+', '') for x in all_reqs \
                    if 'git+' not in x]

setup (
    name = 'ckan-remote-dataloader',
    description = 'A simple commandline app for uploading tables to a remote CKAN datastore',
    version = '0.0.6',
    packages = find_packages(), 
    install_requires = install_requires,
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
    # download_url='https://github.com/jkgeo/ckan-remote-dataloader/archive/v0.0.0.tar.gz',
    dependency_links= dependency_links,
    author_email='jfkeniston@gmail.com',
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ]
)