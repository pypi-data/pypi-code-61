import json
from urllib.parse import parse_qs

try:
    from functools import cached_property
except ImportError as e:
    from .future import cached_property

from .exception import JSONDecodeError
from .exception import Unauthorized
from . import jwt

HEADERS_WITHOUT_HTTP = ('CONTENT_TYPE', 'CONTENT_LENGTH')


def fmt_header_http(name):
    # header name is case-insensitive, 
    # people prefer Pascal Case in tradition,
    # but lowercase will be fashionable now.
    # https://tools.ietf.org/html/rfc7540#section-8.1.2
    return name.lower().replace('_', '-')


def fmt_header_wsgi(name):
    name = name.upper().replace("-", "_")
    prefix = ['HTTP_', ''][int(name in HEADERS_WITHOUT_HTTP)]
    return prefix + name


class Headers(object):

    def __init__(self, environ):
        self.environ = environ

    def get(self, name, default=None):
        k = fmt_header_wsgi(name)
        return self.environ.get(k, default)

    def __iter__(self):
        for key in self.environ:
            if key[:5] == 'HTTP_':
                yield fmt_header_http(key[5:])
            if key in HEADERS_WITHOUT_HTTP:
                yield fmt_header_http(key)

    def __contains__(self, key):
        return fmt_header_wsgi(key) in self.environ


class MultipleValues(object):

    def __init__(self, kv):
        self.kv = kv

    def get(self, name, default=None):
        return self.kv.get(name, [default])[0]

    def get_list(self, name):
        return self.kv.get(name, [])

    def __iter__(self):
        yield from self.kv

    def __contains__(self, key):
        return key in self.kv


class Token:

    def __init__(self, token):
        self.token = token or {}
        self.user_id = self.token.get('sub')
        self.scopes = self.token.get('scopes', [])
        self.data = self.token.get('data')

    def __bool__(self):
        return bool(self.token)


class Request(object):

    def __init__(self, environ):
        self.environ = environ

    @property
    def app(self):
        return self.environ.get('fermata.application')

    @property
    def expression(self):
        return self.environ.get('fermata.expression')

    @property
    def sections(self):
        return self.environ.get('fermata.sections', {})

    @property
    def operation(self):
        return self.environ.get('fermata.operation', self.method)

    @property
    def content_type(self):
        t = self.environ.get('CONTENT_TYPE', '').lower().split(';')[0]
        return t or 'application/json'

    @property
    def path(self):
        return self.environ.get('PATH_INFO', '')

    @property
    def method(self):
        return self.environ.get('REQUEST_METHOD', 'get').lower()

    @property
    def remote_addr(self):
        return self.environ.get("REMOTE_ADDR", '')

    @cached_property
    def jwt(self):
        parts = self.headers.get('authorization', '').split(maxsplit=1)
        if not parts:
            return Token(None)
        try:
            token = self.app.jwt.loads(parts.pop())
        except IndexError:
            pass
        return Token(token)

    @cached_property
    def headers(self):
        return Headers(self.environ)

    @cached_property
    def content(self):
        try:
            length = int(self.environ.get('CONTENT_LENGTH', -1))
        except ValueError:
            length = 0
        if self.app and (length > self.app.max_content_length or length < 0):
            length = self.app.max_content_length

        return self.environ['wsgi.input'].read(length).decode(errors='replace')

    @cached_property
    def params(self):
        return MultipleValues(parse_qs(
            self.environ.get('QUERY_STRING', ''), keep_blank_values=True))

    @cached_property
    def cookies(self):
        return {}  # not supported
