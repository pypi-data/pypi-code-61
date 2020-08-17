# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['strmscience', 'strmscience.finance']

package_data = \
{'': ['*']}

install_requires = \
['fbprophet>=0.6,<0.7',
 'pandas>=1.1.0,<2.0.0',
 'pulp>=2.3,<3.0',
 'seaborn>=0.10.1,<0.11.0']

setup_kwargs = {
    'name': 'strmscience',
    'version': '0.1.2',
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
