# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fennel', 'fennel.client', 'fennel.client.aio', 'fennel.worker']

package_data = \
{'': ['*'], 'fennel.worker': ['lua/*']}

install_requires = \
['anyio>=2.0.0-beta.2,<3.0.0',
 'aredis>=1.1.8,<2.0.0',
 'click>=7.0,<8.0',
 'colorama>=0.4.1,<0.5.0',
 'hiredis>=1.1.0,<2.0.0',
 'pydantic>=1.5,<2.0',
 'redis>=3.3,<4.0',
 'structlog>=20.0,<21.0',
 'uvloop>=0.14.0,<0.15.0']

entry_points = \
{'console_scripts': ['fennel = fennel.cli:cli']}

setup_kwargs = {
    'name': 'fennel',
    'version': '0.3.0',
    'description': 'A task queue for Python based on Redis Streams.',
    'long_description': "## Fennel\n\nA task queue for Python 3.7+ based on Redis Streams with a Celery-like API.\n\nhttps://fennel.dev/\n\n| Note: This is an *alpha* release. The project is under development, breaking changes are likely. |\n| --- |\n\n### Features\n\n* Supports both sync (e.g. Django, Flask) and async (e.g. Starlette, FastAPI) code.\n* Sane defaults: at least once processing semantics, tasks acknowledged on completion.\n* Automatic retries with exponential backoff for fire-and-forget jobs.\n* Clear task statuses available (e.g. sent, executing, success).\n* Automatic task discovery (defaults to using ``**/tasks.py``).\n* Exceptionally small and understandable codebase.\n\n### Installation\n\n```bash\npip install fennel\n```\n\n### Basic Usage\n\nRun [Redis](https://redis.io) and then execute your code in `tasks.py`:\n```python\nfrom fennel import App\n\napp = App(name='myapp', redis_url='redis://127.0.0.1')\n\n\n@app.task\ndef foo(n):\n    return n\n\n\n# Enqueue a task to be executed in the background by a fennel worker process.\nfoo.delay(7)\n```\n\nMeanwhile, run the worker:\n```bash\n$ fennel worker --app tasks:app\n```\n\n### Asynchronous API\n\nFennel also supports an async API. If your code is running in an event loop\n(e.g. via [Starlette](https://www.starlette.io/) or\n[FastAPI](https://fastapi.tiangolo.com/)), you will want to use the async\ninterface instead:\n```python\nfrom fennel import App\n\napp = App(name='myapp', redis_url='redis://127.0.0.1', interface='async')\n\n\n@app.task\nasync def bar(x):\n    return x\n\n\nawait bar.delay(5)\n```\n\n### See also\n\nIf you need to ensure that all tasks for a given key are processed in-order,\nplease see our sister project [Runnel](https://github.com/mjwestcott/runnel).\n",
    'author': 'Matt Westcott',
    'author_email': 'm.westcott@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://fennel.dev',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
