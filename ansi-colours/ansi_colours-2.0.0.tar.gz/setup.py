# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ansi_colours']

package_data = \
{'': ['*']}

install_requires = \
['codecov>=2.1.8,<3.0.0', 'coverage>=5.2.1,<6.0.0', 'pytest>=6.0.1,<7.0.0']

setup_kwargs = {
    'name': 'ansi-colours',
    'version': '2.0.0',
    'description': 'Library of static methods for colouring text in terminal output',
    'long_description': None,
    'author': 'Sarcoma',
    'author_email': 'sarcoma@live.co.uk',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.5,<4.0',
}


setup(**setup_kwargs)
