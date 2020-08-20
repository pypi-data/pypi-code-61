# -*- coding: utf-8 -*-

# from distutils.core import setup
from setuptools import setup, find_packages

# read the contents of your README file
from os import path
import treenodedefinition


this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()


setup(
    name="treenodedefinition",
    version=treenodedefinition.__version__,
    author="David Scheliga",
    author_email="david.scheliga@ivw.uni-kl.de",
    url="https://gitlab.com/david.scheliga/treenodedefinition",
    project_urls={
        "Documentation": "https://gitlab.com/david.scheliga/treenodedefinition",
        "Source Code Repository": "https://gitlab.com/david.scheliga/treenodedefinition",
    },
    description="Providing navigation and selection of objects ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="GNU General Public License v3 (GPLv3)",
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        "Development Status :: 4 - Beta",
        # Indicate who your project is intended for
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        "Programming Language :: Python :: 3",
    ],
    keywords="dictionary, mapping, list, potential_tensor, nested",
    python_requires=">=3.6",
    packages=find_packages(
        exclude=["*.scratches", "*.debug_scripts", "*.scratches.*", "*.debug_scripts.*"]
    )
)
