# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['benchling_api_client',
 'benchling_api_client.api',
 'benchling_api_client.async_api',
 'benchling_api_client.models']

package_data = \
{'': ['*']}

install_requires = \
['httpx>=0.13.3,<0.14.0']

setup_kwargs = {
    'name': 'benchling-api-client',
    'version': '0.1.2a0',
    'description': 'A client library for accessing Benchling API',
    'long_description': '# Benchling API Client\n\nA Python 3.8+ API Client for the [Benchling](https://www.benchling.com/) platform automatically generated from OpenAPI specs.\n\n*Important!* This is an unsupported pre-release not suitable for production use.\n\n_Please reach out to your customer support representative if you would be interested in a public version!_',
    'author': 'Benchling Customer Engineering',
    'author_email': 'ce-team@benchling.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
