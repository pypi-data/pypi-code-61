# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['swap_exceptions']

package_data = \
{'': ['*']}

install_requires = \
['six>=1.15.0,<2.0.0']

extras_require = \
{':python_version >= "2.7" and python_version < "3.0"': ['contextlib2>=0.6.0,<0.7.0',
                                                         'typing>=3.7.4,<4.0.0']}

setup_kwargs = {
    'name': 'swap-exceptions',
    'version': '1.0.0',
    'description': 'Python utility decorator and context manager for swapping exceptions',
    'long_description': '# zoombot\n\n[![PyPI](https://img.shields.io/pypi/v/zoombot)](https://pypi.org/project/zoombot/)\n[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/zoombot)](https://pypi.org/project/zoombot/)\n[![PyPI License](https://img.shields.io/pypi/l/zoombot)](https://pypi.org/project/zoombot/)\n[![Code Style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black/)\n\nPython wrapper for Zoom Chatbot API\n\n### Usage\n```python\nfrom zoombot.core import Bot, Message\n\n\nclass MyBot(Bot):\n    async def on_message(self, message: Message):\n        await message.reply("Hello", f"You sent {message.content}")\n\n\nif __name__ == "__main__":\n    bot = MyBot(\n        client_id="CLIENT_ID",\n        client_secret="CLIENT_SECRET",\n        bot_jid="BOT_JID",\n        verification_token="VERIFICATION_TOKEN",\n    )\n\n    bot.run()\n```\n',
    'author': 'Tom',
    'author_email': 'tomgrin10@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/tomgrin10/swap-exceptions',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*',
}


setup(**setup_kwargs)
