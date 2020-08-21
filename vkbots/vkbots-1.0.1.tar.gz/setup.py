#!/usr/bin/env python

"""Library for creating VK Bots"""
from setuptools import setup
############
import vkbots

description = open("README.rst").read()

setup(
    name="vkbots",
    author=vkbots.__author__,
    version=vkbots.__version__,
    license=vkbots.__license__,
    packages=["vkbots"],
    keywords="vkbots",
    description=__doc__,
    author_email="dimadersekt@gmail.com",
    url="https://github.com/Rollylni/vkbot",
    long_description=description,
    install_requires=["vk_api"],
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Intended Audience :: Developers',
        'Natural Language :: Russian'
    ]
)