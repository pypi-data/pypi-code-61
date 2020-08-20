# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['writeas_view_extractor']

package_data = \
{'': ['*']}

install_requires = \
['writeasapi>=0.1.9,<0.2.0']

entry_points = \
{'console_scripts': ['writeas_view_extractor = '
                     'writeas_view_extractor.main:main']}

setup_kwargs = {
    'name': 'writeas-view-extractor',
    'version': '1.0.1',
    'description': 'Extracts users posts from write.as',
    'long_description': None,
    'author': 'Mikko Uuksulainen',
    'author_email': 'mikko.uuksulainen@uuksu.fi',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
