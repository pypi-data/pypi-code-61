# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['strmscience']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'strmscience',
    'version': '0.1.0',
    'description': 'STRM base python package',
    'long_description': '',
    'author': 'OPSXCQ',
    'author_email': 'opsxcq@strm.sh',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
