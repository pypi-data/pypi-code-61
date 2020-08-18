# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['xarray_compare']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.18,<2.0', 'xarray>=0.15,<0.16']

setup_kwargs = {
    'name': 'xarray-compare',
    'version': '0.1.0',
    'description': 'xarray extension for data comparison',
    'long_description': '# xarray-compare\n\n[![PyPI](https://img.shields.io/pypi/v/xarray-compare.svg?label=PyPI&style=flat-square)](https://pypi.org/pypi/xarray-compare/)\n[![Python](https://img.shields.io/pypi/pyversions/xarray-compare.svg?label=Python&color=yellow&style=flat-square)](https://pypi.org/pypi/xarray-compare/)\n[![Test](https://img.shields.io/github/workflow/status/astropenguin/xarray-compare/Test?logo=github&label=Test&style=flat-square)](https://github.com/astropenguin/xarray-compare/actions)\n[![License](https://img.shields.io/badge/license-MIT-blue.svg?label=License&style=flat-square)](LICENSE)\n\nxarray extension for data comparison\n',
    'author': 'Akio Taniguchi',
    'author_email': 'taniguchi@a.phys.nagoya-u.ac.jp',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/astropenguin/xarray-compare',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
