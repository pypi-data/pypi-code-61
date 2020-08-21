from setuptools import setup

import os.path
from setuptools import setup

# The directory containing this file
HERE = os.path.abspath(os.path.dirname(__file__))

# The text of the README file
with open(os.path.join(HERE, "README.md")) as fid:
    README = fid.read()
# This call to setup() does all the work
setup(
    name="reader-test-rachit-2",
    version="1.0.1",
    long_description=README,
    long_description_content_type="text/markdown",
    author="rachitmishra25",
    author_email="rachit.mishra94@gmail.com",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["reader"],
    include_package_data=True,
    install_requires=["feedparser", "html2text","importlib_resources", "typing"],
    entry_points={
        "console_scripts": [
            "reader-test-rachit-2=reader.__main__:main",
        ]
    },
)