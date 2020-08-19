from setuptools import setup
from os import path
with open(path.join(path.abspath(path.dirname(__file__)), 'README.md'), encoding='utf-8') as f:
    readme_description = f.read()
setup(
name = "jsConsole",
packages = ["jsConsole"],
version = "1.0",
license = "MIT",
description = "A JS Console written for and in python",
author = "Anime no Sekai",
author_email = "niichannomail@gmail.com",
url = "https://github.com/Animenosekai/jsConsole",
download_url = "https://github.com/Animenosekai/jsConsole/archive/v1.0.tar.gz",
keywords = ['javascript', ' selenium', ' pyppeteer', ' js', ' jsconsole', ' javascriptconsole', ' animenosekai', ' pythontojavascript'],
install_requires = ['psutil'],
classifiers = ['Development Status :: 4 - Beta', 'License :: OSI Approved :: MIT License', 'Programming Language :: Python :: 3', 'Programming Language :: Python :: 3.4', 'Programming Language :: Python :: 3.5', 'Programming Language :: Python :: 3.6', 'Programming Language :: Python :: 3.7', 'Programming Language :: Python :: 3.8'],
long_description = readme_description,
long_description_content_type = "text/markdown",
include_package_data=True,
)
