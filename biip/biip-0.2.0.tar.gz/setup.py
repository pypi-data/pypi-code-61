# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['biip', 'biip.gs1']

package_data = \
{'': ['*']}

extras_require = \
{':python_version < "3.8"': ['importlib_metadata>=1.6.0,<2.0.0']}

setup_kwargs = {
    'name': 'biip',
    'version': '0.2.0',
    'description': 'Biip interprets the data in barcodes.',
    'long_description': '<h1 align="center">\n   &#x1F4E6;<br>\n   Biip\n</h1>\n\n<p align="center">\n  <em>Biip interprets the data in barcodes.</em>\n</p>\n\n<p align="center">\n  <a href="https://github.com/jodal/biip/actions?workflow=Tests">\n    <img src="https://github.com/jodal/biip/workflows/Tests/badge.svg" alt="Tests">\n  </a>\n  <a href="https://codecov.io/gh/jodal/biip">\n    <img src="https://codecov.io/gh/jodal/biip/branch/master/graph/badge.svg" alt="Coverage">\n  </a>\n  <a href="https://pypi.org/project/biip/">\n    <img src="https://img.shields.io/pypi/v/biip.svg" alt="PyPI">\n  </a>\n</p>\n\n---\n\nBiip is a Python library for making sense of the data in barcodes.\n\nThe library can interpret the following formats:\n\n- GTIN-8, GTIN-12, GTIN-13, and GTIN-14 numbers,\n  commonly found in EAN-8, EAN-13, UPC-A, UPC-E, and ITF-14 barcodes.\n\n- GS1 AI element strings,\n  commonly found in GS1-128 barcodes.\n\n## Features\n\n- GS1\n  - [x] Parse fixed-length Element Strings\n  - [x] Parse variable-length Element Strings\n    - [x] Support configuring the separation character\n  - Data field enrichment\n    - [ ] Parse `(00)` as SSCC\n    - [x] Parse `(01)` and `(02)` as GTIN\n    - [x] Parse dates into `datetime` objects\n      - [x] Interpret the year to be within -49/+50 years from today\n      - [x] Interpret dates with "00" as the day as the last day of the month\n    - [ ] Parse variable measurement fields (price/weight) into `Decimal` values\n  - [x] Encode as Human Readable Interpretation (HRI), e.g. with parenthesis\n        around the AI numbers\n- GTIN (Global Trade Item Number)\n  - [x] Parse GTIN-8, e.g. from EAN-8 barcodes\n  - [x] Parse GTIN-12, e.g. from UPC-A and UPC-E barcodes\n  - [x] Parse GTIN-13, e.g. from EAN-13 barcodes\n  - [x] Parse GTIN-14, e.g. from ITF-14 barcodes, as well as a data field in GS1 barcodes\n  - [x] Extract and validate check digit\n  - [x] Extract GS1 Prefix\n  - [x] Extract packaging level digit from GTIN-14\n  - [ ] Parse variable measurements (price/weight) into `Decimal` values\n    - The exact semantics vary from market to market, but GS1 have some global\n      recommendations. Have to research if there is enough similarity to have\n      one rule set or if we need to configure what market rule set to use.\n    - Available rule sets include:\n      - [ ] Global recommendations: GS1 General Specifications, chapter 2.1.12.2\n      - [ ] UK: https://www.gs1uk.org/sites/default/files/How_to_calculate_variable_measure_items_0.pdf\n      - [ ] Sweden: https://www.gs1.se/en/our-standards/Identify/variable-weight-number1/\n      - [ ] Baltics: https://gs1lv.org/img/upload/ENG.Variable%20measure_in_Latvia.pdf\n  - Encode\n    - [x] GTIN-8 as GTIN-12/13/14\n    - [x] GTIN-12 as GTIN-13/14\n    - [x] GTIN-13 as GTIN-14\n    - [ ] GTIN with variable weight part zeroed out, to help looking up the correct trade item\n- SSCC\n  - [ ] Validate check digit\n  - [ ] Extract GS1 Company Prefix, if possible due to varying field length\n  - [ ] Extract serial reference, if possible due to varying field length\n- Symbol IDs, e.g. `]EO`\n  - [ ] Use Symbol IDs when automatically selecting what parser to use\n  - [ ] Strip Symbol IDs before parsing the remainder\n\n## Installation\n\nBiip is available from [PyPI](https://pypi.org/project/biip/):\n\n```\npython3 -m pip install biip\n```\n\nBiip requires Python 3.7 or newer.\n\n## Usage\n\nThis project is still in its infancy.\nHowever, some [documentation](https://biip.readthedocs.io/) already exists.\n\n## License\n\nBiip is copyright 2020 Stein Magnus Jodal and contributors.\nBiip is licensed under the\n[Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0).\n',
    'author': 'Stein Magnus Jodal',
    'author_email': 'stein.magnus@jodal.no',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/jodal/biip',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'extras_require': extras_require,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
