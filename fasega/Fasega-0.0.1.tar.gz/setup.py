"""
How to upload new version:
1. Delete dist
2. Up the version number
3. Create dist directory using command: python setup.py sdist bdist_wheel
4. Upload using command: twine upload dist/*
"""
import pathlib
import setuptools

from setuptools import setup

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name='Fasega',
    version='0.0.1',
    description='Happy birthday! 😘😍🥰💝',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://gitlab.com/agerma/fasega',
    author='Abelether Germa',
    author_email='hithere@damngirl.com',
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    install_requires=[
        "click",
        "setuptools",
        "pyfiglet",
        "requests",
        "asciimatics"
    ],
    packages=setuptools.find_packages(exclude=["*.test", "*.test.*", "test.*", "test"]),
    entry_points='''
        [console_scripts]
        abel=fasega:cli
    ''',
    include_package_data=True
)
