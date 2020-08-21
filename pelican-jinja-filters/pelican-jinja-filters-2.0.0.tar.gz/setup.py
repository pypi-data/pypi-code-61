# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pelican', 'pelican.plugins.jinja_filters']

package_data = \
{'': ['*']}

install_requires = \
['pelican>=4.5,<5.0', 'titlecase>=1.1.1,<2.0.0']

extras_require = \
{'markdown': ['markdown>=3.2.2,<4.0.0']}

setup_kwargs = {
    'name': 'pelican-jinja-filters',
    'version': '2.0.0',
    'description': 'Pelican plugin for applying useful Jinja filters in theme templates',
    'long_description': '=============\nJinja Filters\n=============\n\n|build| |pypi|\n\n.. |build| image:: https://img.shields.io/github/workflow/status/pelican-plugins/jinja-filters/build\n    :target: https://github.com/pelican-plugins/jinja-filters/actions\n    :alt: Build Status\n\n.. |pypi| image:: https://img.shields.io/pypi/v/pelican-jinja-filters.svg\n    :target: https://pypi.python.org/pypi/pelican-jinja-filters\n    :alt: PyPI Version\n\n``Jinja Filters`` is a plugin for `Pelican <https://docs.getpelican.com/>`_,\na static site generator written in Python.\n\n``Jinja Filters`` provides a selection of functions (called *filters*) for\ntemplates to use when building your website. They are packaged for Pelican, but\nmay prove useful for other projects that make use of\n`Jinja2 <https://palletsprojects.com/p/jinja/>`_.\n\n\nInstallation\n============\n\nThe easiest way to install ``Jinja Filters`` is through the use of Pip. This\nwill also install the required dependencies (currently ``pelican`` and\n``titlecase``) automatically.\n\n.. code-block:: sh\n\n  pip install pelican-jinja-filters\n\nAs ``Jinja Filters`` is a namespace plugin, it should automatically be loaded\nby Pelican. And that\'s it! The filters are now available for use in your\ntemplates.\n\n\nUsage\n=====\n\nAt present, the plugin includes the following filters:\n\n- ``datetime`` |--| allows you to change to format displayed for a datetime\n  object. Optionally supply a `datetime format string\n  <https://docs.python.org/3.8/library/datetime.html#strftime-and-strptime-behavior>`_\n  to get a custom format.\n- ``article_date`` |--| a specialized version of ``datetime`` that returns\n  datetimes as wanted for article dates; specifically\n  *Friday, November 4, 2020*.\n- ``breaking_spaces`` |--| replaces non-breaking spaces (HTML code *&nbsp*)\n  with normal spaces.\n- ``titlecase`` |--| Titlecases the supplied string.\n\nFor example, within your theme templates, you might have code like:\n\n.. code-block:: html+jinja\n\n    <span class="published">\n        Article Published {{ article.date | article_date }}\n    </span>\n\ngives::\n\n    Article Published Friday, November 4, 2020\n\nOr with your own date format:\n\n.. code-block:: html+jinja\n\n    <span class="published">\n        Article Published {{ article.date | datetime(\'%b %d, %Y\') }}\n    </span>\n\ngives::\n\n    Article Published Nov 04, 2020\n\nFilters can also be chained, or applied in sequence. For example to remove\nbreaking spaces and then titlecase a category name, you might have code like:\n\n.. code-block:: html+jinja\n\n    <a href="{{ SITEURL }}/{{ article.category.url }}">\n        {{ article.category | breaking_spaces | titlecase}}\n    </a>\n\n\nLicense\n=======\n\n``Jinja Filters`` is under the MIT License. See attached ``License.txt`` for\nfull license text.\n\n\n.. |--| unicode:: U+2013   .. en dash\n',
    'author': 'William Minchin',
    'author_email': 'w_minchin@hotmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/pelican-plugins/jinja-filters',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
