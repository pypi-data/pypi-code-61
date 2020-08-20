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
    'version': '0.1.1',
    'description': 'xarray extension for data comparison',
    'long_description': '# xarray-compare\n\n[![PyPI](https://img.shields.io/pypi/v/xarray-compare.svg?label=PyPI&style=flat-square)](https://pypi.org/pypi/xarray-compare/)\n[![Python](https://img.shields.io/pypi/pyversions/xarray-compare.svg?label=Python&color=yellow&style=flat-square)](https://pypi.org/pypi/xarray-compare/)\n[![Test](https://img.shields.io/github/workflow/status/astropenguin/xarray-compare/Test?logo=github&label=Test&style=flat-square)](https://github.com/astropenguin/xarray-compare/actions)\n[![License](https://img.shields.io/badge/license-MIT-blue.svg?label=License&style=flat-square)](LICENSE)\n[![DOI](https://img.shields.io/badge/DOI-10.5281/zenodo.3988924-blue?style=flat-square)](https://doi.org/10.5281/zenodo.3988924)\n\nxarray extension for data comparison\n\n## TL;DR\n\nxarray-compare is a third-party Python package which provides extra data-comparison features.\nAfter importing the package, several DataArray methods (`dataarray.is*()`) will be available.\n\n## Requirements\n\n- **Python:** 3.6, 3.7, or 3.8 (tested by the author)\n- **Dependencies:** See [pyproject.toml](https://github.com/astropenguin/xarray-compare/blob/master/pyproject.toml)\n\n## Installation\n\n```shell\n$ pip install xarray-compare\n```\n\n## List of available methods\n\n- `.isbetween(lower, upper)`: Test whether each value in a DataArray falls within an interval\n- `.ismatch(pattern)`: Test whether each string in a DataArray matches a regex pattern\n\nMethods of "not-in" version are also provided for readability.\n\n- `.isnotin(values)`: Equivalent to `~dataarray.isin(values)` (`.isin()` is an xarray\'s builtin)\n- `.isnotbetween(lower, upper)`: Equivalent to `~dataarray.isbetween(lower, upper)`\n- `.isnotmatch(pattern)`: Equivalent to `~dataarray.ismatch(pattern)`\n\n## Examples\n\nxarray-compare is a just-import package.\nAfter importing it, methods become available from normal DataArray instances.\n\n```python\nimport xarray as xr\nimport xarray_compare\n```\n\nA method returns a boolean DataArray each value of which is `True` where that of the input DataArray fulfills the condition and `False` otherwise.\nThis is why it works well with the `dataarray.where()` method.\n\n```python\nda = xr.DataArray([0, 1, 1, 2, 3, 5, 8, 13])\nda.where(da.isbetween(1, 4), drop=True)\n\n# <xarray.DataArray (dim_0: 4)>\n# array([1., 1., 2., 3.])\n# Dimensions without coordinates: dim_0\n```\n\n```python\nda = xr.DataArray([\'a\', \'aa\', \'ab\', \'bc\'])\nda.where(da.ismatch("^a+$"), drop=True)\n\n# <xarray.DataArray (dim_0: 2)>\n# array([\'a\', \'aa\'], dtype=object)\n# Dimensions without coordinates: dim_0\n```\n',
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
