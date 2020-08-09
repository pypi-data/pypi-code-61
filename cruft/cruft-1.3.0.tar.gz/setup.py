# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cruft', 'cruft.commands']

package_data = \
{'': ['*']}

install_requires = \
['cookiecutter>=1.6,<2.0',
 'examples>=1.0,<2.0',
 'gitpython>=3.0,<4.0',
 'hug>=2.6,<3.0']

extras_require = \
{'pyproject': ['toml>=0.10,<0.11']}

entry_points = \
{'console_scripts': ['cruft = cruft.cli:hug_api.cli']}

setup_kwargs = {
    'name': 'cruft',
    'version': '1.3.0',
    'description': 'Allows you to maintain all the necessary cruft for packaging and building projects separate from the code you intentionally write. Built on-top of CookieCutter.',
    'long_description': '[![cruft - Fight Back Against the Boilerplate Monster!](https://raw.github.com/timothycrosley/cruft/master/art/logo_large.png)](https://timothycrosley.github.io/cruft/)\n_________________\n\n[![PyPI version](https://badge.fury.io/py/cruft.svg)](http://badge.fury.io/py/cruft)\n[![Build Status](https://github.com/timothycrosley/cruft/workflows/Run%20tests/badge.svg)](https://github.com/timothycrosley/cruft/actions?query=workflow%3A%22Run+tests%22+branch%3Amaster)\n[![codecov](https://codecov.io/gh/timothycrosley/cruft/branch/master/graph/badge.svg)](https://codecov.io/gh/timothycrosley/cruft)\n[![Join the chat at https://gitter.im/timothycrosley/cruft](https://badges.gitter.im/timothycrosley/cruft.svg)](https://gitter.im/timothycrosley/cruft?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)\n[![License](https://img.shields.io/github/license/mashape/apistatus.svg)](https://pypi.python.org/pypi/cruft/)\n[![Downloads](https://pepy.tech/badge/cruft)](https://pepy.tech/project/cruft)\n_________________\n\n[Read Latest Documentation](https://timothycrosley.github.io/cruft/) - [Browse GitHub Code Repository](https://github.com/timothycrosley/cruft/)\n_________________\n\n**cruft** allows you to maintain all the necessary boilerplate for packaging and building projects separate from the code you intentionally write.\nFully compatible with existing [Cookiecutter](https://github.com/cookiecutter/cookiecutter) templates.\n\nCreating new projects from templates using cruft is easy:\n\n![Example Usage New Project](https://raw.githubusercontent.com/timothycrosley/cruft/master/art/example.gif)\n\nAnd, so is updating them as the template changes overtime:\n\n![Example Usage New Project](https://raw.githubusercontent.com/timothycrosley/cruft/master/art/example_update.gif)\n\nMany project template utilities exist that automate the copying and pasting of code to create new projects. This *seems* great! However, once created, most leave you with that copy-and-pasted code to manage through the life of your project.\n\ncruft is different. It automates the creation of new projects like the others, but then it also helps you to manage the boilerplate through the life of the project. cruft makes sure your code stays in-sync with the template it came from for you.\n\n## Key Features:\n\n* **Cookiecutter Compatible**: cruft utilizes [Cookiecutter](https://github.com/cookiecutter/cookiecutter) as its template expansion engine. Meaning it retains full compatibility with all existing [Cookiecutter](https://github.com/cookiecutter/cookiecutter) templates.\n* **Template Validation**: cruft can quickly validate whether or not a project is using the latest version of a template using `cruft check`. This check can easily be added to CI pipelines to ensure your projects stay in-sync.\n* **Automatic Template Updates**: cruft automates the process of updating code to match the latest version of a template, making it easy to utilize template improvements across many projects.\n\n## Installation:\n\nTo get started - install `cruft` using a Python package manager:\n\n`pip3 install cruft`\n\nOR\n\n`poetry add cruft`\n\nOR\n\n`pipenv install cruft`\n\n\n## Creating a New Project:\n\nTo create a new project using cruft run `cruft create PROJECT_URL` from the command line.\n\nFor example:\n\n        cruft create https://github.com/timothycrosley/cookiecutter-python/\n\ncruft will then ask you any necessary questions to create your new project. It will use your answers to expand the provided template, and then return the directory it placed the expanded project.\nBehind the scenes, cruft uses [Cookiecutter](https://github.com/cookiecutter/cookiecutter) to do the project expansion. The only difference in the resulting output is a `.cruft.json` file that\ncontains the git hash of the template used as well as the parameters specified.\n\n## Updating a Project\n\nTo update an existing project, that was created using cruft, run `cruft update` in the root of the project.\nIf there are any updates, cruft will have you review them before applying. If you accept the changes cruft will apply them to your project\nand update the `.cruft.json` file for you.\n\n!!! tip\n    Sometimes certain files just aren\'t good fits for updating. Such as test cases or `__init__` files. You can tell cruft to always skip updating these files on a project by project basis by added them\n    to a skip section within your .cruft.json file:\n\n        {\n            "template": "https://github.com/timothycrosley/cookiecutter-python",\n            "commit": "8a65a360d51250221193ed0ec5ed292e72b32b0b",\n            "skip": [\n                "cruft/__init__.py",\n                "tests"\n            ],\n            ...\n        }\n\n    Or, if you have toml installed, you can add skip files directly to a `tool.cruft` section of your `pyproject.toml` file:\n\n        [tool.cruft]\n        skip = ["cruft/__init__.py", "tests"]\n\n\n## Checking a Project\n\nChecking to see if a project is missing a template update is as easy as running `cruft check`. If the project is out-of-date an error and exit code 1 will be returned.\n`cruft check` can be added to CI pipelines to ensure projects don\'t unintentionally drift.\n\n\n## Linking an Existing Project\n\nHave an existing project that you created from a template in the past using Cookiecutter directly? You can link it to the template that was used to create it using: `cruft link TEMPLATE_REPOSITORY`.\n\nFor example:\n\n        cruft link https://github.com/timothycrosley/cookiecutter-python/\n\nYou can then specify the last commit of the template the project has been updated to be consistent with, or accept the default of using the latest commit from the template.\n\n## Why Create cruft?\n\nSince I first saw videos of [quickly](https://www.youtube.com/watch?v=9EctXzH2dss) being used to automate Ubuntu application creation, I\'ve had a love/hate relationship with these kinds of tools.\nI\'ve used them for many projects and certainly seen them lead to productivity improvements. However, I\'ve always felt like they were a double-edged sword. Sure, they would automate away the copying and pasting many would do to create projects. However, by doing so,\nthey encouraged more code to be copied and pasted! Then, over time, you could easily be left with hundreds of projects that contained copy-and-pasted code with no way to easy way to update them. I created cruft to be a tool that recognized that balance between project creation and maintenance and provided mechanisms to keep built projects up-to-date.\n\nI hope you too find `cruft` useful!\n\n~Timothy Crosley\n',
    'author': 'Timothy Crosley',
    'author_email': 'timothy.crosley@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
