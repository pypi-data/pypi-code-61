import io
import os
import re
from typing import List, Union

from setuptools import find_packages, setup


def read(f_relative_path: str, read_lines: bool = False) -> Union[List[str], str]:
    """Return the contents of file f_relative_path as a string, or a list of strings if read_lines is True.

    :param f_relative_path: the file path relative to this script folder.
    :param read_lines: if True return list of lines, else return a single string.
    :return: the content of the file.
    """
    here = os.path.dirname(os.path.abspath(__file__))
    with io.open(os.path.join(here, f_relative_path), mode="rt", encoding="utf8") as f:
        return f.readlines() if read_lines else f.read()


def get_version() -> str:
    """Return the package version as defined in kx_core/__init__.py."""
    init = read("example/__init__.py")
    return re.search(r"__version__ = \"(.*?)\"", init).group(1)


setup(
    name="peter_experiment_xxx01",
    version=get_version(),
    url="https://github.com/KENDAXA-Development/repository-template",
    author="Kendaxa Development s.r.o.",
    author_email="contact-prague@kendaxa.com",
    description="Python package example",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    include_package_data=True,
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=read("requirements.txt", read_lines=True),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
    ],
)
