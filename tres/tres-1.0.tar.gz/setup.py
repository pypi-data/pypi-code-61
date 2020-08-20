# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['tres']
setup_kwargs = {
    'name': 'tres',
    'version': '1.0',
    'description': 'Type resolver (dependency container) for Python',
    'long_description': None,
    'author': 'Richard Jones',
    'author_email': 'richard@mechanicalcat.net',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/r1chardj0n3s/tres',
    'py_modules': modules,
}


setup(**setup_kwargs)
