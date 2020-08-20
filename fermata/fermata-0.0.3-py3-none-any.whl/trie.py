import typing


def split(expression):
    parts = expression.strip().strip('/').split('/')
    parts = [] if parts == [''] else parts
    return parts


class PathTrie(object):

    def __init__(self, expressions: typing.Sequence[str] = None) -> None:
        self.root = {}
        if expressions:
            for p in expressions:
                self.add(p)

    def __getitem__(self, expression):
        parts = split(expression)
        node = self.root
        for part in parts:
            if part[0] == '{' and part[-1] == '}':
                part = '/*/'
            node = node[part]
        return node['/data/']

    def __iter__(self):
        nodes = [self.root]
        while nodes:
            current = nodes.pop()
            nodes = [v for k, v in current.items()
                     if k == '/*/' or not k.startswith('/')] + nodes
            if '/expression/' in current:
                yield current['/expression/'], current['/data/']

    def add(self, expression: str) -> None:
        parts = split(expression)
        node = self.root
        sections = []
        for part in parts:
            if part[0] == '{' and part[-1] == '}':
                sections.append(part[1:-1])
                node = node.setdefault('/*/', {})
            else:
                node = node.setdefault(part, {})
        node['/expression/'] = expression
        node['/sections/'] = sections
        node['/data/'] = {}

    def match(self, path: str) -> typing.Tuple[str, dict]:
        parts = split(path)
        length = len(parts)
        searches = [(self.root, 0, [])]  # (node, depth, matched_sections)

        while searches:
            node, depth, sections = searches.pop(0)
            # found it! each parts were matched
            if depth == length and '/sections/' in node:
                return node['/expression/'], dict(
                    zip(node['/sections/'], sections)), node['/data/']
            # wont match
            if depth >= length:
                continue
            # search next level
            part = parts[depth]
            # full match search first
            if part in node:
                searches.append((node.get(part), depth + 1, sections))
            # wildcard match also acceptable
            if '/*/' in node:
                searches.append((node.get('/*/'), depth + 1, sections + [part]))

        return None, {}, None
