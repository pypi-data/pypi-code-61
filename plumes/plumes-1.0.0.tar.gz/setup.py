# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['plumes']

package_data = \
{'': ['*']}

install_requires = \
['dynaconf>=3.1.0,<4.0.0',
 'fire>=0.3.1,<0.4.0',
 'python-box>=5.1.0,<6.0.0',
 'tqdm>=4.48.2,<5.0.0',
 'tweepy>=3.9.0,<4.0.0']

entry_points = \
{'console_scripts': ['plumes = plumes.cli:main']}

setup_kwargs = {
    'name': 'plumes',
    'version': '1.0.0',
    'description': 'Simple Twitter CLI for day-to-day social media hygiene',
    'long_description': None,
    'author': 'Nicholas Nadeau',
    'author_email': 'nicholas.nadeau@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6.1,<4.0.0',
}


setup(**setup_kwargs)
