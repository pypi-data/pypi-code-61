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
 'fastapi>=0.61,<0.62',
 'pydantic>=1.6,<2.0',
 'uvicorn>=0.11,<0.12']

setup_kwargs = {
    'name': 'faststan',
    'version': '0.1.6',
    'description': 'Build data streaming pipelines using faststan',
    'long_description': '# FastSTAN\n\n<a href="https://gitlab.com/faststan/faststan/-/commits/next"><img alt="Pipeline status" src="https://gitlab.com/faststan/faststan/badges/next/pipeline.svg"></a>\n<a href="https://gitlab.com/faststan/faststan/-/commits/next"><img alt="Coverage report" src="https://gitlab.com/faststan/faststan/badges/next/coverage.svg"></a>\n<a href="https://python-poetry.org/docs/"><img alt="Packaging: poetry" src="https://img.shields.io/badge/packaging-poetry-blueviolet"></a>\n<a href="https://flake8.pycqa.org/en/latest/"><img alt="Style: flake8" src="https://img.shields.io/badge/style-flake8-ff69b4"></a>\n<a href="https://black.readthedocs.io/en/stable/"><img alt="Format: black" src="https://img.shields.io/badge/format-black-black"></a>\n<a href="https://docs.pytest.org/en/stable/"><img alt="Packaging: pytest" src="https://img.shields.io/badge/tests-pytest-yellowgreen"></a>\n<a href="https://pypi.org/project/faststan/"><img alt="PyPI" src="https://img.shields.io/pypi/v/faststan"></a>\n<a href="https://faststan.gitlab.io/faststan/"><img alt="Documentation" src="https://img.shields.io/badge/docs-mkdocs-blue"></a>\n<a href="https://opensource.org/licenses/MIT"><img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-yellow.svg"></a>\n\nEasily deploy NATS Streaming subscribers using Python.\n\n## Features\n\n- Define subscribers using sync and async python functions\n- Automatic data parsing and validation using type annotations and pydantic\n- Support custom validation using any function\n- Allow several subscribers on same channel\n- Support all subscription configuration available in stan.py\n- Healthcheck available using HTTP GET request to monitor the applications\n- (TODO) Metrics available using HTTP GET requests to monitor subsriptions status\n- All of FastAPI features\n\n## Quick start\n\n- Install the package from pypi:\n\n```bash\npip install faststan\n```\n\n- Create your first subscriber. Create a file named `app.py` and write the following lines:\n\n```python\nfrom faststan import FastSTAN\n\napp = FastSTAN()\n\n@app.stan.subscribe("demo")\ndef on_event(message: str):\n    print(f"INFO :: Received new message: {message}")\n```\n\n- Start your subscriber:\n\n```shell\nuvicorn app:app\n```\n\n- Or if you are in a jupyter notebook environment, start the subscriptions:\n\n```python\nawait app.stan.run()\n```\n\n## Advanced features\n\n### Using error callbacks\n\n```python\nfrom faststan import FastSTAN\n\n\napp = FastSTAN()\n\n\ndef handle_error(error):\n    print("ERROR: {error}")\n\n\n@app.stan.subscribe("demo", error_cb=handle_error)\ndef on_event(message: str):\n    print(f"INFO :: Received new message: {message}")\n```\n\n### Using pydantic models\n\nYou can use pydantic models in order to automatically parse incoming messages:\n\n```python\nfrom pydantic import BaseModel\nfrom faststan import FastSTAN\n\n\nclass Event(BaseModel):\n    timestamp: int\n    temperature: float\n    humidity: float\n\n\napp = FastSTAN()\n\n\n@app.stan.subscribe("event")\ndef on_event(event):\n    msg = f"INFO :: {event.timestamp} :: Temperature: {event.temperature} | Humidity: {event.humidity}"\n    print(msg)\n```\n\n### Using pydantic models with numpy or pandas\n\n```python\nimport numpy as np\nfrom pydantic import BaseModel\nfrom faststan import FastSTAN\n\n\nclass NumpyEvent(BaseModel):\n    values: np.ndarray\n    timestamp: int\n\n    @validator("temperature", pre=True)\n    def validate_array(cls, value):\n        return np.array(value, dtype=np.float32)\n\n    @validator("humidity", pre=True)\n    def validate_array(cls, value):\n        return np.array(value, dtype=np.float32)\n\n    class Config:\n        arbitrary_types_allowed = True\n\n@app.stan.subscribe("event")\ndef on_event(event: NumpyEvent):\n    print(\n        f"INFO :: {event.timestamp} :: Temperature values: {event.values[0]} | Humidity values: {event.values[1]}"\n    )\n```\n',
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
