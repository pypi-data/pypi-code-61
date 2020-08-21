# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['linechart']

package_data = \
{'': ['*']}

install_requires = \
['arrow>=0.15.8,<0.16.0',
 'empyrical>=0.5.3,<0.6.0',
 'linefolio>=1.2.0,<2.0.0',
 'matplotlib>=3.3.1,<4.0.0',
 'pandas>=1.1.1,<2.0.0',
 'quantrocket-client>=2.1.1,<3.0.0',
 'scipy>=1.5.2,<2.0.0',
 'seaborn>=0.10.1,<0.11.0']

setup_kwargs = {
    'name': 'linechart',
    'version': '1.4.0',
    'description': 'Backtest performance analysis and charting for MoonLine.',
    'long_description': None,
    'author': 'Tim Wedde',
    'author_email': 'timwedde@icloud.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
