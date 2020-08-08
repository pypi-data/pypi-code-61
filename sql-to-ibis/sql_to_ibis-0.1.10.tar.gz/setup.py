from distutils.core import setup
import os
from pathlib import Path

from setuptools import find_packages

import versioneer

CODE_DIRECTORY = Path(__file__).parent


def read_file(filename):
    """Source the contents of a file"""
    with open(
        os.path.join(os.path.dirname(__file__), filename), encoding="utf-8"
    ) as file:
        return file.read()


setup(
    name="sql_to_ibis",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    packages=find_packages(),
    long_description="Coming soon...",
    maintainer="Zach Brookler",
    maintainer_email="zachb1996@yahoo.com",
    description="A package for converting sql into ibis expressions",
    python_requires=">=3.6.1",
    install_requires=["lark-parser==0.8.5", "ibis-framework==1.3.0"],
    project_urls={
        "Source Code": "https://github.com/zbrookle/sql_to_ibis",
        "Documentation": "https://github.com/zbrookle/sql_to_ibis",
        "Bug Tracker": "https://github.com/zbrookle/sql_to_ibis/issues",
    },
    url="https://github.com/zbrookle/sql_to_ibis",
    download_url="https://github.com/zbrookle/sql_to_ibis/archive/master.zip",
    keywords=["pandas", "data", "dataframe", "sql", "ibis"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Database :: Database Engines/Servers",
        "Topic :: Database :: Front-Ends",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Typing :: Typed",
        "Operating System :: OS Independent",
    ],
    long_description_content_type="text/markdown",
    include_package_data=True,
)
