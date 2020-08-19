

class Specification:
    '''An OpenAPI specification dict wrapper, for getting value 
       by key path recurrently, and load JSON $ref if necessary.'''

    def __init__(self, spec, refs=None):
        self.data = spec
        if refs is None:
            refs = {}
        self.refs = {**refs, '': self.data}
        self.deref(self.data)

    def deref(self, node, from_uri=''):
        stack = [(node, from_uri)]
        objects = set()
        while len(stack) > 0:
            node, from_uri = stack.pop(0)
            if isinstance(node, dict):
                keys = node.keys()
            elif isinstance(node, list):
                keys = range(len(node))
            else:
                continue

            for k in keys:
                uri = from_uri
                _values = set()

                while isinstance(node[k], dict) and '$ref' in node[k]:
                    value, uri = self._ref(node[k]['$ref'], from_uri=uri)
                    if id(value) in _values:
                        raise RecursionError()
                    _values.add(id(value))
                    node[k] = value

                if isinstance(node[k], (dict, list)) and id(node[k]) not in objects:
                    objects.add(id(node[k]))
                    stack += [(node[k], uri)]

    @classmethod
    def ref2keys(cls, ref, from_uri=''):
        if ref.find('#') == -1:
            ref = '#' + ref
        uri, fragment = ref.split('#', 1)
        return uri or from_uri, tuple(k.replace('~1', '/').replace('~0', '~')
                for k in fragment.strip('/').split('/'))

    def _getitem(self, keys, uri=''):
        node = self.refs[uri]
        for k in keys:
            if isinstance(node, list):
                try:
                    k = int(k)
                except ValueError:
                    pass
            node = node[k]
        return node

    def __getitem__(self, keys):
        return self._getitem(keys)

    def _ref(self, ref, default=None, from_uri=''):
        uri, keys = self.ref2keys(ref, from_uri)
        try:
            v = self._getitem(keys, uri)
        except (KeyError, IndexError, TypeError):
            return default, ''
        v = v if v is not None else default
        return v, uri

    def ref(self, ref, default=None):
        return self._ref(ref, default)[0]

    def items(self, expression):
        _, parts = self.ref2keys(expression)
        results = []
        params = []
        keys = []
        queue = [(self.data, parts, params)]
        while len(queue) > 0:
            node, parts, params = queue.pop(0)
            part, parts = parts[0], parts[1:]
            wildcard = len(part) >= 3 and part[0] == '{' and part[-1] == '}'
            is_list = isinstance(node, list)

            if not wildcard:
                if is_list:
                    try:
                        part = int(part)
                    except ValueError:
                        pass
                try:
                    node = { part: node[part] }
                except (IndexError, KeyError, TypeError):
                    continue
                is_list = False

            items = enumerate(node) if is_list else node.items()

            for k, v in items:
                p = params + [(part[1:-1], k)] if wildcard else params
                if parts:
                    queue.append((v, parts[:], p))
                else:
                    results.append((dict(p), v))

        return results


def deref(spec, refs=None):
    return Specification(spec, refs).data
