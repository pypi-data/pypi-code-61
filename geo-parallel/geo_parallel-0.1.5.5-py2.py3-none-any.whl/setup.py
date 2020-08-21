# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['geoparallel-lib', 'geoparallel-lib.geo_parallel']

package_data = \
{'': ['*'], 'geoparallel-lib': ['dist/*']}

setup_kwargs = {
    'name': 'geo-parallel',
    'version': '0.1.5.5',
    'description': '',
    'long_description': None,
    'author': 'Artur',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=2.7,<3.0',
}


setup(**setup_kwargs)
