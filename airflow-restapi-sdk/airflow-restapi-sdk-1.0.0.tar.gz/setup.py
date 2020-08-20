try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

with open("README.md", "r", encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='airflow-restapi-sdk',
    version='1.0.0',
    author='biao.xu',
    author_email='biao.xu@baodanyun-inc.com',
    description='Airflow Rest API Python SDK',
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires=">=3.5",
    install_requires=['requests'],
    packages=find_packages(),
    classifiers=[
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
)
