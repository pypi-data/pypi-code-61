from setuptools import setup
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

packages = ['is_computer_on']
print('packages=', packages)

setup(
    name="is_computer_on",

    version="1.0.0",

    packages=packages,
    install_requires=[],
    author="Grant miller",
    author_email="grant@grant-miller.com",
    description="A python package to empirically determine if the processing unit is functional.",
    long_description=long_description,
    license="PSF",
    keywords="is computer on",
    url="https://github.com/GrantGMiller/is_computer_on",  # project home page, if any
    project_urls={
        "Source Code": "https://github.com/GrantGMiller/is_computer_on",
    }

)

# python -m setup.py sdist bdist_wheel
# twine upload dist/*