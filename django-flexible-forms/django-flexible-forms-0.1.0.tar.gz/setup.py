# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['flexible_forms']

package_data = \
{'': ['*']}

install_requires = \
['django>=2.2', 'swapper>=1.1.2,<2.0.0']

setup_kwargs = {
    'name': 'django-flexible-forms',
    'version': '0.1.0',
    'description': 'A reusable Django app for managing database-backed forms.',
    'long_description': None,
    'author': 'Eric Abruzzese',
    'author_email': 'eric.abruzzese@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
