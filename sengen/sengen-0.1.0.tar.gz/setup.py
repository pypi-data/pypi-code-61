# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sengen']

package_data = \
{'': ['*']}

install_requires = \
['matplotlib>=3.3.1,<4.0.0',
 'numpy',
 'pandas>=1.1.1,<2.0.0',
 'scipy>=1.5.2,<2.0.0',
 'sklearn>=0.0,<0.1',
 'sympy>=1.6.2,<2.0.0']

setup_kwargs = {
    'name': 'sengen',
    'version': '0.1.0',
    'description': 'Synthetic Sensor Data Generator',
    'long_description': None,
    'author': 'Your Name',
    'author_email': 'you@example.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
