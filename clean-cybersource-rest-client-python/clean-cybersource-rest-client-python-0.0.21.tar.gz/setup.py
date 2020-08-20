# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['CyberSource',
 'CyberSource.apis',
 'CyberSource.models',
 'CyberSource.utilities',
 'CyberSource.utilities.flex',
 'CyberSource.utilities.flex.exception',
 'authenticationsdk',
 'authenticationsdk.core',
 'authenticationsdk.http',
 'authenticationsdk.jwt',
 'authenticationsdk.logger',
 'authenticationsdk.payloaddigest',
 'authenticationsdk.test',
 'authenticationsdk.util']

package_data = \
{'': ['*']}

install_requires = \
['PyJWT==1.6.4',
 'certifi==2019.9.11',
 'pycryptodome==3.9.8',
 'pyopenssl==17.5.0',
 'python_dateutil==2.5.3',
 'setuptools==21.0.0',
 'six>=1.12.0,<2.0.0',
 'urllib3==1.15.1']

setup_kwargs = {
    'name': 'clean-cybersource-rest-client-python',
    'version': '0.0.21',
    'description': '',
    'long_description': None,
    'author': 'Maximiliano Opitz',
    'author_email': 'maximiliano@cornershopapp.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
