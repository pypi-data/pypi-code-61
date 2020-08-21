# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['utils_plus',
 'utils_plus.management',
 'utils_plus.management.commands',
 'utils_plus.migrations',
 'utils_plus.npm',
 'utils_plus.templatetags',
 'utils_plus.utils',
 'utils_plus.views']

package_data = \
{'': ['*']}

install_requires = \
['django>=2.2']

setup_kwargs = {
    'name': 'django-utils-plus',
    'version': '0.7.4',
    'description': 'A reusable Django app with small set of utilities for urls, viewsets, commands and more',
    'long_description': '# utils-plus \nA simple reusable Django app with various mixins and utility functions.\n\n-------\n\n[![PyPi Version](https://img.shields.io/pypi/v/pconf.svg?style=flat)](https://pypi.python.org/pypi/pconf)\n[![Python Version](https://img.shields.io/pypi/pyversions/returns.svg)](https://pypi.org/project/returns/)\n\n-------\n\n# Installation\ninstall the package using the below command\n\n```commandline\npip install django-utils-plus\n```\n\nor install the development version using \n```commandline\npip install git://github.com/jnoortheen/django-utils-plus.git@master#egg=django-utils-plus\n```\n\n# Utils\n\n## Management Commands\n - clear_records\n - create_admin\n - test_mail\n - cleardata\n - create_middleware\n    \n## Template tags\n 1. klass\n 1. [unpkg](#unpkg)\n 1. [jsdelivr](#jsdelivr) (combined support as well)\n \n### serve static files using npm\n it is convenient to keep track of all external `js` libraries in project using \n a `package.json`. It is used to keep latest version of available packages. \n The following template tags can be used to serve these packages right from CDN on production and \n `node_modules` during development\n\n#### unpkg\n Alternative to standard `static` template tag. When you are using external static files/libraries\nlike bootstrap, jquery you may want to load them from CDNs instead of managing them yourself in production.\nThis tag helps you to do that. When `settings.DEBUG` is false, this will return paths that resolved from\n`package.json` to versioned `unpkg.com`. Otherwise it will resolve to `node_modules` locally.\n\n#### jsdelivr\n    like `unpkg` adds support for using https://www.jsdelivr.com/\n\n#### Usage:\n\nload the template tags and use `unpkg` like `static` tag,\n\n```\n{% load static utils_plus_tags %}\n<link rel="stylesheet" type="text/css" href="{% unpkg \'bootstrap/dist/css/bootstrap.min.css\' %}"/>\n<script src="{% unpkg \'bootstrap/dist/js/bootstrap.min.js\' %}"></script>\n<script src="{% unpkg \'jquery/dist/jquery.min.js\' %}"></script>\n```\n#### Note:\n1. the package.json should be present in the project ROOT DIR.\n1. When DEBUG is True the packages must  be installed and should be available already inside `node_modules`.\n \n\n## Middleware\n - login_required_middleware\n\n## Urls & Routing with ease\n\nAn elegant and DRY way to define urlpatterns. It has easier to nest many levels deeper and still have the readability.\nIt is just a wrapper behind the standard url(), include() methods.\n\nThis is how your urls.py may look\n```python\n### urls.py ###\nurlpatterns = [\n    url(r\'^studenteditordocument/(?P<doc_pk>\\d+)/edit/$\', EditView.as_view(), name=\'edit-student-doc\'),\n    url(r\'^studenteditordocument/(?P<doc_pk>\\d+)/export/$\', ExportView.as_view(), name=\'export-editore-doc\'),\n\n    url(r\'^docs/$\', Docs.as_view(), name=\'student-documents\'),\n    url(r\'^publish/$\', PulishOrDelete.as_view(), {\'action\': \'publish\'}, name="publish_document"),\n    url(r\'^delete/$\', PulishOrDelete.as_view(), name=\'delete_document\'),\n]\n```\n\nafter using `Url`\n```python\n### urls.py ###\n\nfrom utils_plus.router import url\n\nurlpatterns = list(\n        url(\'editor\')[\n            url.int(\'doc_pk\')[\n                url(\'edit\', DocEditorView.as_view(), \'edit-doc\'),\n                url(\'export\', DocExporterView.as_view(), \'export-doc\'),\n            ]\n        ]\n        + url(\'docs\', Docs.as_view(), \'student-documents\')\n        + url(\'publish\', DeleteOrPublistDocument.as_view(), \'publish_document\', action=\'publish\')\n        + url(\'delete\', DeleteOrPublistDocument.as_view(), \'delete_document\')\n```\n\nsee `tests/test_router.py` for more use cases\n\n## Model \n\n1. `CheckDeletableModelMixin`\nadds a `is_deletable` method which then can be used to check any affected related records before actually deleting them.\noriginally it is copied from this [gist](https://gist.github.com/freewayz/69d1b8bcb3c225bea57bd70ee1e765f8)\n\n2. `ChoicesEnum`\nEnumerator class for use with the django ORM choices field\n\n3. `QueryManager`\nA DRYer way to set select_related, prefetch_related & filters to queryset.\n    - this has `first_or_create` method similar to get_or_create\n\n```python\nfrom django.db import models\nfrom utils_plus.models import QueryManager\n\nclass Post(models.Model):\n    author = models.ForeignKey(\'Author\')\n    comments = models.ManyToManyField(\'Comment\')\n    published = models.BooleanField()\n    pub_date = models.DateField()\n    \n    # custom managers\n    objects = QueryManager() # equivalent to models.Manager\n    public_posts = QueryManager(published=True).order_by(\'-pub_date\')\n    rel_objects = QueryManager().selects(\'author\').prefetches(\'comments\')\n```\n\n## Config Option\n\n1. `URL_GROUP_TRAIL_SLASH`\n    - By default all the urls generated by this class will have trailing slash\n    - Set this to False in settings.py to change this behaviour\n\n## Views\n1. **CreateUpdateView**:\n    - combines CreateView and UpdateView\n\n# Testing the project\n    - clone the repo and run migrations after installing dependencies\n    - `inv test` will run all the test for the app\n',
    'author': 'jnoortheen',
    'author_email': 'jnoortheen@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/jnoortheen/django-utils-plus',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6',
}


setup(**setup_kwargs)
