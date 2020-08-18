# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['appunit']

package_data = \
{'': ['*']}

install_requires = \
['starlette>=0.13.8,<0.14.0']

setup_kwargs = {
    'name': 'appunit',
    'version': '0.1.0.dev0',
    'description': '',
    'long_description': None,
    'author': 'Anton Ruhlov',
    'author_email': 'antonruhlov@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
