from setuptools import setup, find_packages

version = '0.0.3'

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('./requirements.txt', 'r') as requirements_file:
    requirements = [
        requirement for requirement in requirements_file
    ]

setup(
    name='target-mysql',
    version=version,
    description='A Singer.io target implementation for MySQL',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/czardien/target-mysql",
    author='Adrien Czerny',
    author_email='adrien.czerny@example.com',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=requirements,
)
