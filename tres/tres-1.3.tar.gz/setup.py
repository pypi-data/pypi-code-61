# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['tres']
setup_kwargs = {
    'name': 'tres',
    'version': '1.3',
    'description': 'Typed resolver (dependency container) for Python',
    'long_description': "# tres\nTyped resolver (dependency container) for Python\n\nIt provides a dependency container for you to use in typed dependency resolution.\n\nThat's all. Very type resolution. Much wow.\n\nInspired by the dependency container in [tsyringe](https://www.npmjs.com/package/tsyringe), but more Pythonic.\n\n## Usage:\n\n```python\nfrom tres import container, InjectionToken\n\ndef a(n: int) -> str:\n    return str(n)\n\n\ndef b(a: int, b: int) -> int:\n    return a + b\n\n\na_token = InjectionToken[Callable[[int], str]]()\nb_token = InjectionToken[Callable[[int, int], int]]()\n\ncontainer.register(a_token, a)\ncontainer.register(b_token, b)\ncontainer.register(b_token, a)  # type error\n\n\ndef c(f: Callable[[int], str]):\n    print(f(1))\n\n\nc(container[a_token])\nc(container[b_token])  # type error\n```\n\n## A longer example registering a Protocol\n\n```python\n\n# application logic\n\nfrom typing import Protocol, Iterable\n\nclass OrdersProtocol(Protocol):\n    def byId(self, id) -> Order:\n        ...\n\n    def getLines(self, id) -> Iterable[OrderLine]:\n        ...\n\nOrdersStoreToken = tres.InjectionToken[OrdersProtocol]()\n\ndef calculate_total(orders_store: OrdersProtocol, order_id):\n    order = orders_store.byId(order_id)\n    lines = orders_store.getLines(order_id)\n    return sum(line.price for line in lines) + order.shipping\n\n\n# implementation\n\nfrom config import URL\u2028from domain import Order, OrderLine\nfrom application import OrdersProtocol, OrdersStoreToken\n\nclass OrdersStore(OrdersProtocol):\n\xa0\xa0\xa0\xa0def __init__(self, url):\n\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0self.url = url\n\n\xa0\xa0\xa0\xa0def byId(self, id):\n\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0return map(Order, requests.get(f'{self.url}/order/{id}').json())\n\n\xa0\xa0\xa0\xa0def getLines(self, id):\n\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0return map(OrderLine, requests.get(f'{self.url}/order/{id}/lines').json())\n\ntres.container.register(OrdersStoreToken, OrdersStore(URL))\n\n\n# consumer\n\nfrom application import calculate_total, OrdersStoreToken\n\ndef order_view(order_id):\n\xa0\xa0\xa0\xa0orders_store = tres.container[OrdersStoreToken]\n\xa0\xa0\xa0\xa0order = orders_store.byId(order_id)\n\xa0\xa0\xa0\xa0total = calculate_total(orders_store, order_id)\n\xa0\xa0\xa0\xa0return f'{order.id} - {order.date}: {total}'\n```\n",
    'author': 'Richard Jones',
    'author_email': 'richard@mechanicalcat.net',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/r1chardj0n3s/tres',
    'py_modules': modules,
}


setup(**setup_kwargs)
