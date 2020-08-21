# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyplates', 'tests']

package_data = \
{'': ['*']}

install_requires = \
['loguru>=0.5.1,<0.6.0']

extras_require = \
{':python_version < "3.7"': ['aiocontextvars>=0.2.0'],
 ':python_version ~= "2.7" and sys_platform == "win32"': ['pathlib2'],
 ':sys_platform == "win32"': ['colorama>=0.4.3,<0.5.0',
                              'win32-setctime>=1.0.0']}

setup_kwargs = {
    'name': 'pyplates',
    'version': '0.1.0',
    'description': 'Project Template for python on macOS Big Sur',
    'long_description': "# IttyTwitty\n\n[![netlify badge](https://api.netlify.com/api/v1/badges/416b8ca3-82db-470f-9adf-a6d06264ca75/deploy-status)](https://app.netlify.com/sites/mystifying-keller-ab5658/deploys) [![Build Status](https://travis-ci.com/skeptycal/.dotfiles.svg?branch=dev)](https://travis-ci.com/skeptycal/.dotfiles) [![test coverage](https://img.shields.io/badge/test_coverage-100%25-6600CC.svg?logo=Coveralls&color=3F5767)](https://coveralls.io)\n\n> Having a basic way to tweet and interact with Twitter from the command line is a simple but handy set of actions. This project provides this functionality with the least amount of configuration.\n>\n> It just works!\n\n---\n\n## Installation\n\n[![macOS Version](https://img.shields.io/badge/macOS-10.16%20Big%20Sur-orange?logo=apple)](https://www.apple.com) [![GitHub Pipenv locked Python version](https://img.shields.io/badge/Python-3.8-yellow?color=3776AB&logo=python&logoColor=yellow)](https://www.python.org/) [![nuxt.js](https://img.shields.io/badge/nuxt.js-2.10.2-35495e?logo=nuxt.js)](https://nuxtjs.org/)\n\n```sh\n# install script ...\n./setup.sh\n```\n\n---\n\n## Contributing\n\n[![code style: prettier](https://img.shields.io/badge/code_style-prettier-ff69b4.svg?logo=prettier)](https://github.com/prettier/prettier) [![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-v1.4%20adopted-ff69b4.svg)](CODE_OF_CONDUCT.md)\n\n**Please feel free to offer [suggestions and changes](https://github.com/skeptycal/dotfiles/issues).**\n\n_I have been coding for many years, but mostly as a side activity ... as a tool to assist me in other endeavors ... so I have not had the 'hard time' invested of constant coding that many of you have. Suggestions/improvements\nwelcome!_\n\n[![License](https://img.shields.io/badge/License-MIT-darkblue)](https://skeptycal.mit-license.org/1976/) [![CII Best Practices](https://bestpractices.coreinfrastructure.org/projects/3454/badge)](https://bestpractices.coreinfrastructure.org/projects/3454)\n\n---\n\n## Author\n\n[![twitter/skeptycal](https://s.gravatar.com/avatar/b939916e40df04f870b03e0b5cff4807?s=80)](http://twitter.com/skeptycal 'Follow @skeptycal on Twitter')\n\nCopyright © 2018-2020 [Michael Treanor](https:/skeptycal.github.com)\n\n![Twitter Follow](https://img.shields.io/twitter/follow/skeptycal.svg?style=social) ![GitHub followers](https://img.shields.io/github/followers/skeptycal.svg?label=GitHub&style=social)\n\n[michael treanor]: (https://www.skeptycal.com)\n[mathias bynens]: (https://mathiasbynens.be/)\n",
    'author': 'skeptycal',
    'author_email': 'skeptycal@gmail.com',
    'maintainer': 'skeptycal',
    'maintainer_email': 'skeptycal@gmail.com ',
    'url': 'https://skeptycal.github.io/as_loguru',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.6.1,<4.0.0',
}


setup(**setup_kwargs)
