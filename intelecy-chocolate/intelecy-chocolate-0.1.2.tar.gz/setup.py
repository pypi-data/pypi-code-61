# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['chocolate',
 'chocolate.conditional',
 'chocolate.connection',
 'chocolate.crossvalidation',
 'chocolate.mo',
 'chocolate.sample',
 'chocolate.search']

package_data = \
{'': ['*']}

install_requires = \
['dataset>=0.8',
 'filelock>=2.0',
 'ghalton>=0.6',
 'numpy==1.16.4',
 'pandas>=0.19',
 'psycopg2-binary>=2.8.5,<3.0.0',
 'pymongo>=3.4',
 'scikit-learn>=0.21,<0.22',
 'scipy>=0.18',
 'sphinx>=1.5']

setup_kwargs = {
    'name': 'intelecy-chocolate',
    'version': '0.1.2',
    'description': 'Intelecy fork of Chocolate',
    'long_description': None,
    'author': 'areeh',
    'author_email': 'are.haartveit@intelecy.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
