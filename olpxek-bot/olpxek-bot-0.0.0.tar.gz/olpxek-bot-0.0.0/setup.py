# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['olpxek_bot']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'olpxek-bot',
    'version': '0.0.0',
    'description': '',
    'long_description': None,
    'author': 'Chanwoong Kim',
    'author_email': 'me@chanwoong.kim',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
}


setup(**setup_kwargs)
