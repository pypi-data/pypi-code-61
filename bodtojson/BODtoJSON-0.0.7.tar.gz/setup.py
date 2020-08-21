import setuptools
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="BODtoJSON",
    version="0.0.7",
    author="Niraj Kakodkar",
    author_email="niraj.kakodkar@gmail.com",
    license='MIT',
    description="Converts Infor QAGIS BODs to  flattened JSON",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/thekakodkar/Mapper",
    packages=['BODtoJSON'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['xmltodict'],
    python_requires='>=3.0',
)
