# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fileprep']

package_data = \
{'': ['*']}

install_requires = \
['datetime>=4.3,<5.0', 'pandas>=1.0.5,<2.0.0', 'xlrd>=1.2.0,<2.0.0']

setup_kwargs = {
    'name': 'fileprep',
    'version': '0.0.3',
    'description': 'Batch prepare and clean bad formatted excel files for further analysis.',
    'long_description': '',
    'author': 'Christian Schramm',
    'author_email': 'cschra@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/v0ku/fileprep',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
