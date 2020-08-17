# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['faststan']

package_data = \
{'': ['*']}

install_requires = \
['asyncio-nats-client>=0.10.0,<0.11.0',
 'asyncio-nats-streaming>=0.4.0,<0.5.0',
 'fastapi>=0.61.0,<0.62.0',
 'pydantic>=1.6.1,<2.0.0',
 'uvicorn>=0.11.8,<0.12.0']

setup_kwargs = {
    'name': 'faststan',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'gcharbon',
    'author_email': 'guillaume.charbonnier@capgemini.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
