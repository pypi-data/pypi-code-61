#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

from setuptools import find_packages, setup

MODULE = "worker_demo"
COMMAND = "worker-demo"


def parse_requirements():
    path = Path(__file__).parent.resolve() / "requirements.txt"
    assert path.exists(), f"Missing requirements: {path}"
    return list(map(str.strip, path.read_text().splitlines()))


setup(
    name=MODULE,
    version=open("VERSION").read(),
    description="Demo ML worker for Arkindex",
    author="",
    author_email="",
    install_requires=parse_requirements(),
    entry_points={"console_scripts": [f"{COMMAND}={MODULE}.worker:main"]},
    packages=find_packages(),
)
