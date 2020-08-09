import setuptools

content = """'''{README}

visit : https://github.com/greats3an/pyncm for more info
'''

# This file is automaticly generated by `setup.py`

from . import ncm
from .ncm import *
"""
requirements = [
    requirement.strip() for requirement in open('requirements.txt','r',encoding='utf-8').readlines()
]

with open("README.md", "r",encoding='utf-8') as fh:
    long_description = fh.read()

with open("pyncm/__init__.py","w",encoding='utf-8') as target:
    # Update modlue __docstring__    
    content = content.format(README=long_description)
    target.write(content)

setuptools.setup(
    name="pyncm", # Replace with your own username
    version="1.1",
    author="greats3an",
    author_email="greats3an@gmail.com",
    description="NeteaseCloudMusic APIs for Python 3.x 适用于 Python 3 的网易云音乐 API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/greats3an/pyncm",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],install_requires=requirements,
    python_requires='>=3.2',
)