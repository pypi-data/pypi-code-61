import re
import sys
import os
import ast
from itertools import chain
from unittest.mock import patch

from fermata.request import Request

from .util import load_app


class Colonist:

    def __init__(self, name, args, kwargs):
        self.name = name
        self.args = ['request', *args]
        self.kwargs = kwargs

    @property
    def signature(self):
        arguments = self.args + [f'{k}={repr(v)}' for k, v in self.kwargs]
        return f'def {self.name}({", ".join(arguments)}):'

    def __eq__(self, op):
        return (
            op.name == self.name and
            set(op.args) == set(self.args) and
            set(op.kwargs) == set(self.kwargs)
        )

    def __str__(self):
        return '\n\n' + self.signature + '\n    pass\n'


class Aborigine:

    UNKNOWN_DEFAULT = object()

    def __init__(self, signature):
        self.signature = signature
        self.args = []
        self.kwargs = []
        self._parse()

    @property
    def protected(self):
        return (
            self.vararg or 
            self.kwarg or 
            self.UNKNOWN_DEFAULT in [v for _, v in self.kwargs]
        )

    def _parse(self):
        root = ast.parse(self.signature + 'pass')
        self.node = root.body[0]
        self.name = self.node.name
        args = self.node.args

        count = len(args.args) - len(args.defaults)
        kwargs = []

        for n, d in chain(zip(args.args[count:], args.defaults),
                          zip(args.kwonlyargs, args.kw_defaults)):
            if d is None:
                value = None
            elif d.__class__.__name__ in ('Str', 'Num', 'NameConstant'):
                value = getattr(d, d._fields[0])
            else:
                value = self.UNKNOWN_DEFAULT
            kwargs.append((n.arg, value))

        self.args =[n.arg for n in args.args[:count]]
        self.kwargs = kwargs
        self.vararg = args.vararg.arg if args.vararg else None
        self.kwarg = args.kwarg.arg if args.kwarg else None


class Module:

    OPERATE_PATTERN = r'^def\s+\w+\s*\([\s\S]*?\)\s*\:'

    def __init__(self, path):
        self.path = path
        self.lines = []
        self.changes = []
        self.operations = []
        self._rename()
        self._parse()

    def _rename(self):
        is_package = self.path.rsplit('/', 1)[1:] == ['__init__.py']
        os.makedirs(os.path.dirname(self.path), exist_ok=True)
        if is_package:
            module = self.path[:-12] + '.py'
            if os.path.isfile(module):
                os.rename(module, self.path)
        else:
            package = os.path.join(self.path[:-3], '__init__.py')
            if os.path.isfile(package):
                os.rename(package, self.path)
                try:
                    os.rmdir(os.path.dirname(package))
                except OSError:
                    pass

    def _parse(self):
        with open(self.path, 'a+'):
            pass
        with open(self.path, 'r') as f:
            self.source = f.read()
        for signature in re.findall(
                self.OPERATE_PATTERN, self.source, re.MULTILINE):
            self.operations.append(Aborigine(signature))

    def append(self, source):
        self.source = ''.join([self.source, source])

    def replace(self, aborigine, colonist):
        self.source = self.source.replace(aborigine, colonist)

    def dump(self):
        with open(self.path, 'w+') as f:
            f.write(self.source)


class Package:

    def __init__(self):
        self.root = {}

    def set(self, module_name, name, value):
        node = self.root
        for part in module_name.split('.'):
            node = node.setdefault(part, {})
        node.setdefault('.data', {})[name] = value

    def __iter__(self):
        nodes = list(self.root.items())
        while nodes:
            base, node = nodes.pop(0)
            node = {**node}
            data = node.pop('.data', {})
            path = os.path.join(base, '__init__.py') if node else f'{base}.py'
            nodes.extend((os.path.join(base, k), n) for k, n in node.items())
            yield path, data


def fermata_operators(app):
    r = Request({})
    for _, methods in app.router:
        for method, data in methods.items():
            if 'operator' not in data:
                continue
            operator = data.get('operator')
            validator = data.get('validator')
            args, kwargs = [], []
            if validator:
                for c in validator._clauses(r):
                    if c.get('required'):
                        args.append(c['name'])
                    else:
                        kwargs.append((c['name'], c.get('default')))
            module, func = operator.operation_id.rsplit('.', 1)
            yield module, func, args, kwargs


def build_package(app):
    package = Package()
    for module, func, args, kwargs in fermata_operators(app):
        package.set(module, func, Colonist(func, args, kwargs))
    return package


def complete(app_path):
    with patch('fermata.Fermata.preload', lambda s: None):
        app, mod = load_app(app_path)

    base = os.path.dirname(mod.__file__)

    for path, colonists in build_package(app):
        module = Module(os.path.join(base, path))
        for op in module.operations:
            if op.name in colonists:
                colonist = colonists.pop(op.name)
                if not op.protected and colonist != op:
                    module.replace(op.signature, colonist.signature)
            else:
                print(f'{path}::{op.name} is not in specification', file=sys.stderr)
        for op in colonists.values():
            module.append(str(op))
        module.dump()
