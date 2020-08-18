# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['plumes']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'plumes',
    'version': '0.1.0',
    'description': 'Simple Twitter CLI for day-to-day tasks and social media hygiene',
    'long_description': None,
    'author': 'Nicholas Nadeau',
    'author_email': 'nicholas.nadeau@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6.1',
}


setup(**setup_kwargs)
