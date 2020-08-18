#!/usr/bin/env python

from setuptools import setup

setup(
    name="p8",
    version="0.1.0",
    description="The Python ultimate meta linter",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Viet Hung Nguyen",
    author_email="hvn@familug.org",
    url="https://github.com/hvnsweeting/p8",
    license="MIT",
    classifiers=["Environment :: Console"],
    entry_points={"console_scripts": ["p8=p8:main"]},
)
