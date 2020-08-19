try:
    import singledispatchmethod
except ImportError as e:
    from ..future import singledispatchmethod

from .authorizer import Authorizer
from .validator import Validator
from .operator import Operator
from ..trie import PathTrie
from ..exception import NotFound
from ..exception import PathNotFound
from ..exception import MethodNotAllowed


class Router(object):

    def __init__(self):
        self.trie = PathTrie()

    def add(self, expression):
    	self.trie.add(expression)

    def _set(self, k, v, expression, operation):
        self.trie[expression].setdefault(operation, {})[k] = v

    @singledispatchmethod
    def set(self, v, expression, operator):
        raise NotImplementedError()

    @set.register(Authorizer)
    def _(self, authorizer, expression, operation):
        self._set('authorizer', authorizer, expression, operation)

    @set.register(Validator)
    def _(self, validator, expression, operation):
        self._set('validator', validator, expression, operation)

    @set.register(Operator)
    def _(self, operator, expression, operation):
        self._set('operator', operator, expression, operation)

    def route(self, request):
        expression, sections, operations = self.trie.match(request.path)
        request.environ['fermata.expression'] = expression
        request.environ['fermata.sections'] = sections

        if expression is None:
            raise PathNotFound(f'Path Not Found: `{request.path}`')

        try:
            data = operations[request.method]
        except KeyError:
            if request.method == 'head' and 'get' in operations:
                request.environ['fermata.operation'] = 'get'
                data = operations[request.operation]
            elif request.method in ('get', 'head'):
                raise NotFound('Method Not Found')
            else:
                raise MethodNotAllowed()

        authorizer = data.get('authorizer')
        validator = data.get('validator')
        operator = data.get('operator')

        return authorizer, validator, operator

    def __iter__(self):
        yield from self.trie
