# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['zoombot']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.6.2,<4.0.0',
 'starlette>=0.13.8,<0.14.0',
 'uvicorn>=0.11.8,<0.12.0']

setup_kwargs = {
    'name': 'zoombot',
    'version': '0.1.2',
    'description': 'Python wrapper for Zoom Chatbot API',
    'long_description': '# zoombot\n\n[![PyPI](https://img.shields.io/pypi/v/zoombot)](https://pypi.org/project/zoombot/)\n[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/zoombot)](https://pypi.org/project/zoombot/)\n[![PyPI License](https://img.shields.io/pypi/l/zoombot)](https://pypi.org/project/zoombot/)\n[![Code Style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black/)\n\nPython wrapper for Zoom Chatbot API\n\n### Usage\n```python\nfrom zoombot.core import Bot, Message\n\n\nclass MyBot(Bot):\n    async def on_message(self, message: Message):\n        await message.reply("Hello", f"You sent {message.content}")\n\n\nif __name__ == "__main__":\n    bot = MyBot(\n        client_id="CLIENT_ID",\n        client_secret="CLIENT_SECRET",\n        bot_jid="BOT_JID",\n        verification_token="VERIFICATION_TOKEN",\n    )\n\n    bot.run()\n```\n',
    'author': 'Tom',
    'author_email': 'tomgrin10@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/tomgrin10/zoombot',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
