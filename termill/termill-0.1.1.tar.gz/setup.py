# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['termill']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'termill',
    'version': '0.1.1',
    'description': '',
    'long_description': '# Termill\n\nA command line utility library to print out multiple lines of text and replace\nthem. It\'s simple to print out a single line and replace it by using a carriage\nreturn:\n\n```python\nprint("foo", end="\\r")\nprint("bar")\n```\n\nbut that doesn\'t work with multiple lines. But by utilising backspace\ncharacters and the width of the terminal, you can actually replace multiple\nlines.\n\nThis library is just to handle that, so that you can print out lines, flush\nthem, then print out new lines ontop of the old ones. A simple demo is included\n(`demo.py`) that just prints out the current time for 5 seconds.\n\nThis was just thrown together as a proof of concept, so it\'s likely very buggy.\nThis has also only been tested on my MacOS machine, with ZSH. I have no idea if\nthis works anywhere else.\n\n## Why not curses?\nI wanted to be able to monitor certain things and print out regular updates to\nthe termina. As far as I could tell (based on very very limited research) I\ncould do that with curses, but it would have to take over the whole terminal.\n\nI want to be able to print out few lines and update them, without having to\ntake over the terminal, the idea being that I can see the history in my\nterminal right before running whatever is printing out updates.\n\n## Usage\n\n```python\nimport time\n\nfrom termill import termill\n\nwith termill() as t:\n    t.write("line one")\n    t.write("line two")\n    t.write("line three")\n    t.flush()\n    time.sleep(1)\n    t.write_lines(["line one has changed", "there will be no line three"])\n    t.flush()\n```\n\n## Demo\n\n![demo.gif](https://raw.githubusercontent.com/ikornaselur/termill/master/.github/demo.gif)\n',
    'author': 'Axel',
    'author_email': 'dev@absalon.is',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/ikornaselur/termill',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
