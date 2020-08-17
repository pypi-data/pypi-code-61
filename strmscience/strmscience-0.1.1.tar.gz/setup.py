# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['strmscience']

package_data = \
{'': ['*']}

install_requires = \
['pulp>=2.3,<3.0']

setup_kwargs = {
    'name': 'strmscience',
    'version': '0.1.1',
    'description': 'STRM base python package',
    'long_description': '',
    'author': 'OPSXCQ',
    'author_email': 'opsxcq@strm.sh',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
