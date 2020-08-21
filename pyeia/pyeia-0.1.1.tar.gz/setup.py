# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['eia', 'eia.api']

package_data = \
{'': ['*']}

install_requires = \
['click>=7.1.2,<8.0.0',
 'dynaconf>=3.0.0,<4.0.0',
 'httpx>=0.13.3,<0.14.0',
 'loguru>=0.5.1,<0.6.0',
 'orjson>=3.3.0,<4.0.0',
 'pandas>=1.1.0,<2.0.0']

setup_kwargs = {
    'name': 'pyeia',
    'version': '0.1.1',
    'description': 'Python client for the Energy Information Administration (EIA) API',
    'long_description': None,
    'author': 'Thomas Tu',
    'author_email': 'thomasthetu@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/thomastu/pyEIA',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
