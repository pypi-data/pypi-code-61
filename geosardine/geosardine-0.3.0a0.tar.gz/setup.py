# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['geosardine']

package_data = \
{'': ['*']}

install_requires = \
['affine>=2.3.0,<3.0.0',
 'fiona',
 'gdal',
 'numpy>=1.18,<2.0',
 'rasterio',
 'shapely>=1.6.4,<2.0.0',
 'tqdm>=4.48.2,<5.0.0']

entry_points = \
{'console_scripts': ['dine = geosardine.__main__:main']}

setup_kwargs = {
    'name': 'geosardine',
    'version': '0.3.0a0',
    'description': 'Spatial operations extend fiona and rasterio',
    'long_description': '##Geo-Sardine\n\nCollection of spatial operation which i use occasionally\n',
    'author': 'Sahit Tuntas Sadono',
    'author_email': '26474008+sahitono@users.noreply.github.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/sahitono/geosardine',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
