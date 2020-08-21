# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['invisible_hand',
 'invisible_hand.config',
 'invisible_hand.config.templates',
 'invisible_hand.scripts',
 'invisible_hand.utils']

package_data = \
{'': ['*']}

install_requires = \
['beautifulsoup4>=4.9.1,<5.0.0',
 'click>=7.1.2,<8.0.0',
 'colorama>=0.4.3,<0.5.0',
 'gitpython>=3.1.7,<4.0.0',
 'google-api-python-client>=1.10.0,<2.0.0',
 'google-auth-httplib2>=0.0.4,<0.0.5',
 'google-auth-oauthlib>=0.4.1,<0.5.0',
 'halo>=0.0.30,<0.0.31',
 'httpx>=0.14.1,<0.15.0',
 'ipython>=7.17.0,<8.0.0',
 'iso8601>=0.1.12,<0.2.0',
 'lxml>=4.5.2,<5.0.0',
 'pandas>=1.1.1,<2.0.0',
 'prompt-toolkit>=3.0.6,<4.0.0',
 'pygsheets>=2.0.3,<3.0.0',
 'requests>=2.24.0,<3.0.0',
 'selenium>=3.141.0,<4.0.0',
 'tabulate>=0.8.7,<0.9.0',
 'tqdm>=4.48.2,<5.0.0',
 'trio>=0.16.0,<0.17.0',
 'xlsxwriter>=1.3.3,<2.0.0']

entry_points = \
{'console_scripts': ['invisible-hand = invisible_hand.__main__:main']}

setup_kwargs = {
    'name': 'invisible-hand',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Ian Chen',
    'author_email': 'ianre657@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
