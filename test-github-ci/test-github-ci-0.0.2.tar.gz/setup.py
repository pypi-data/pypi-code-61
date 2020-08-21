# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['test_github_ci']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['say-hello = test_github_ci.hello:hello']}

setup_kwargs = {
    'name': 'test-github-ci',
    'version': '0.0.2',
    'description': 'This project tests AutoPub with GitHub Actions CI.',
    'long_description': '# Test AutoPub & GitHub Actions CI\n\n1. Create repository\n1. Create GitHub and PyPI tokens with appropriate scopes\n1. Add `GH_TOKEN` & `PYPI_PASSWORD` environment variables via repository Settings > Secrets > New secret\n1. Create `.github/workflows` and add appropriate GitHub CI workflow\n1. Add appropriate AutoPub configuration to `pyproject.toml`\n1. Add `RELEASE.md` file with release type and description\n1. `git add .`, commit, and push\n',
    'author': 'BotPub',
    'author_email': 'botpub@autopub.rocks',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
