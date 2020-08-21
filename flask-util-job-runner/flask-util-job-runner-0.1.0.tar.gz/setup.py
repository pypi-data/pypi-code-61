# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['flask_util_job_runner']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'flask-util-job-runner',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'eqqe',
    'author_email': 'simon.rey@esker.fr',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
