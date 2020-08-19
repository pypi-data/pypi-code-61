
from setuptools import setup


def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="simpleHelloChhavi2",
    version="1.0.0",
    description="A Python package to simply desplay hello world bot in lower case and upper case as per user's need.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    author="Chhavi Trivedi",
    author_email="chhavi7320@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],


)
