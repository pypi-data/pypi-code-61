# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['termlog', 'termlog.tests']

package_data = \
{'': ['*']}

install_requires = \
['pygments>=2.6.1,<3.0.0']

setup_kwargs = {
    'name': 'termlog',
    'version': '1.3.0',
    'description': 'A Terminal logging library',
    'long_description': None,
    'author': 'Brian Bruggeman',
    'author_email': 'Brian.M.Bruggeman@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
