# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['tres']
setup_kwargs = {
    'name': 'tres',
    'version': '1.2',
    'description': 'Typed resolver (dependency container) for Python',
    'long_description': "# tres\nTyped resolver (dependency container) for Python\n\nIt provides a dependency container for you to use in typed dependency resolution.\n\nThat's all. Very type resolution. Much wow.\n\nInspired by the dependency container in [tsyringe](https://www.npmjs.com/package/tsyringe), but more Pythonic.\n\n## Usage:\n\n```python\nfrom tres import container, InjectionToken\n\ndef a(n: int) -> str:\n    return str(n)\n\n\ndef b(a: int, b: int) -> int:\n    return a + b\n\n\na_token = InjectionToken[Callable[[int], str]]()\nb_token = InjectionToken[Callable[[int, int], int]]()\n\ncontainer.register(a_token, a)\ncontainer.register(b_token, b)\ncontainer.register(b_token, a)  # type error\n\n\ndef c(f: Callable[[int], str]):\n    print(f(1))\n\n\nc(container[a_token])\nc(container[b_token])  # type error\n```\n",
    'author': 'Richard Jones',
    'author_email': 'richard@mechanicalcat.net',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/r1chardj0n3s/tres',
    'py_modules': modules,
}


setup(**setup_kwargs)
