import setuptools
from pathlib import Path

setuptools.setup(
    name="jdla_basic",
    version=1.0,
    long_description_content_type='text/markdown',
    long_description=Path("README.md").read_text(),
    packages=setuptools.find_packages(exclude=["tests"])
)
