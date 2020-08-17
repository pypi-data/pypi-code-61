# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['faststan']

package_data = \
{'': ['*']}

install_requires = \
['asyncio-nats-client>=0.10.0,<0.11.0',
 'asyncio-nats-streaming>=0.4.0,<0.5.0',
 'fastapi>=0.61.0,<0.62.0',
 'pydantic>=1.6.1,<2.0.0',
 'uvicorn>=0.11.8,<0.12.0']

setup_kwargs = {
    'name': 'faststan',
    'version': '0.1.3',
    'description': 'Build data streaming pipelines using faststan',
    'long_description': '# FastSTAN\n\nEasily deploy NATS Streaming subscribers using Python.\n\n## Features\n\n- Define subscribers using sync and async python functions\n- Automatic data parsing and validation using type annotations and pydantic\n- Support custom validation using any function\n- Allow several subscribers on same channel\n- Support all subscription configuration available in stan.py\n- Healthcheck available using HTTP GET request to monitor the applications\n- (TODO) Metrics available using HTTP GET requests to monitor subsriptions status\n- All of FastAPI features\n\n## Quick start\n\n- Install the package from pypi:\n\n```bash\npip install faststan\n```\n\n- Create your first subscriber. Create a file named `app.py` and write the following lines:\n\n```python\nfrom faststan.faststan import FastSTAN\n\napp = FastSTAN()\n\n@app.subscribe("demo")\ndef on_event(message: str):\n    print(f"INFO :: Received new message: {message}")\n```\n\n- Start your subscriber:\n\n```shell\nuvicorn app:app\n```\n\n- Or if you are in a jupyter notebook environment, start the subscriptions:\n\n```python\nawait app.start()\n```\n\n## Advanced features\n\n### Using error callbacks\n\n```python\nfrom faststan.faststan import FastSTAN\n\n\napp = FastSTAN()\n\n\ndef handle_error(error):\n    print("ERROR: {error}")\n\n\n@app.subscribe("demo", error_cb=handle_error)\ndef on_event(message: str):\n    print(f"INFO :: Received new message: {message}")\n```\n\n### Using pydantic models\n\nYou can use pydantic models in order to automatically parse incoming messages:\n\n```python\nfrom pydantic import BaseModel\nfrom faststan.faststan import FastSTAN\n\n\nclass Event(BaseModel):\n    timestamp: int\n    temperature: float\n    humidity: float\n\n\napp = FastSTAN()\n\n\n@app.subscribe("event")\ndef on_event(event):\n    msg = f"INFO :: {event.timestamp} :: Temperature: {event.temperature} | Humidity: {event.humidity}"\n    print(msg)\n```\n',
    'author': 'gcharbon',
    'author_email': 'guillaume.charbonnier@capgemini.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://pypi.org/project/faststan/',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
