import os
from setuptools import setup

with open("README.md", "r") as fh:
    README = fh.read()


setup(
    name='django-q-rollbar',
    version='0.1.3',
    author='Daniel Welch, Christo Goosen',
    author_email='dwelch2102@gmail.com, christogoosen@gmail.com',
    keywords='django distributed task queue worker scheduler cron redis disque ironmq sqs orm mongodb multiprocessing rollbar',
    packages=['django_q_rollbar'],
    install_requires=['rollbar>=0.14.0'],
    url='https://django-q.readthedocs.org',
    license='MIT',
    description='A Rollbar support plugin for Django Q',
    long_description=README,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
