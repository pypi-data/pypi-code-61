# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['blandfeed']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.6.2,<4.0.0',
 'appdirs>=1.4.4,<2.0.0',
 'dbus-python>=1.2.16,<2.0.0',
 'pygobject>=3.36.1,<4.0.0',
 'pynacl>=1.4.0,<2.0.0']

entry_points = \
{'console_scripts': ['blandfeed = blandfeed.main:main']}

setup_kwargs = {
    'name': 'blandfeed',
    'version': '0.1.3',
    'description': 'Push feed for your device, easy to setup, mediocre to use',
    'long_description': None,
    'author': 'rendaw',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
