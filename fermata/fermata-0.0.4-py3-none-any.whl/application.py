import typing
import sys
import glob
import os.path

from . import loader
from .jwt import JWT
from .request import Request
from .response import Response
from .response import JSONResponse
from .openapi import Router
from .openapi import Authorizer
from .openapi import Validator
from .openapi import Operator
from .openapi import Specification
from .openapi import default_operation_id
from .openapi import ScopesFetcher
from .exception import HTTPException
from .exception import InternalServerError

MAX_CONTENT_LENGTH = 1024 * 10
ALLOWED_OPERATIONS = {'get', 'put', 'post', 'delete', 'options', 'head', 'patch', 'trace'}
PAYLOAD_OPERATIONS = {'post', 'put', 'options'}


def respond_abort(request, exception: HTTPException):
    return JSONResponse(**exception)


def respond_capture(request, exception):
    return respond_abort(request, InternalServerError())


class Fermata(ScopesFetcher):

    def __init__(
            self,
            default_package: str = None,
            spec_glob: str = None,
            *,
            exception_captors: typing.Dict[typing.Type[Exception], typing.Callable] = None,
            scopes_fetcher: typing.Callable = None,
            jwt_key: str = None,
        ) -> None:

        self.default_package = default_package
        if scopes_fetcher:
            self.fetch_scopes = scopes_fetcher
        self.listeners = {}
        if jwt_key:
            self.jwt = JWT(jwt_key)
        self.max_content_length = MAX_CONTENT_LENGTH

        self.router = Router()
        self.spec_files = []
        if spec_glob:
            self.scan(spec_glob)

        self.exception_captors = {
            HTTPException: respond_abort,
            Exception: respond_capture,
            **(exception_captors or {})
        }

    @property
    def name(self):
        return self.default_package

    def preload(self):
        for _, methods in self.router:
            for method, data in methods.items():
                if 'operator' not in data:
                    continue
                data.get('operator').load()

    def scan(self, spec_glob, filename_as_basepath=True):
        spec_files = {}
        parsers = {
            '.json': 'json.load',
            '.yaml': 'yaml.safe_load',
            '.yml': 'yaml.safe_load',
        }
        for path in glob.glob(spec_glob):
            ext = os.path.splitext(path)[1]
            if ext not in parsers:
                self.log('warning', f'not supported file: {path}')
                continue
            spec_files.setdefault(parsers[ext], []).append(path)
        for parser, files in spec_files.items():
            parse = loader.load(parser)
            for f in files:
                spec = parse(open(f))
                base_path = ''
                if filename_as_basepath:
                    base_path = os.path.splitext(os.path.basename(f))[0]
                self.interpret(spec, base_path)
                self.spec_files.append(f)
        return self

    def interpret(self, spec, base_path=''):
        spec = Specification(spec)

        # router
        for expression in spec.data.get('paths', {}).keys():
            self.router.add(base_path + expression)

        # authorizer
        # securitySchemes
        security = spec.ref('components/securitySchemes')
        if security:
            base = spec.ref('security')
            for k, node in spec.items('paths/{path}/{operation}'):
                security = node.get('security', base)
                if not security:
                    continue
                path, operation = k.values()
                authorizer = Authorizer(security, self)
                self.router.set(authorizer, base_path + path, operation)

        # validator
        # parameters as validate clauses
        for k, node in spec.items('paths/{path}/{operation}'):
            path, operation = k.values()
            if operation not in ALLOWED_OPERATIONS:
                continue
            p = path.replace('/', '~1')
            base = spec.ref(f'paths/{p}/parameters', [])
            parameters = base + node.get('parameters', [])
            if not parameters and 'requestBody' not in node:
                continue
            body = node.get('requestBody', {})
            validator = Validator(
                parameters, 
                body.get('content', {}),
                body.get('required', False))
            self.router.set(validator, base_path + path, operation)

        # operator
        for k, node in spec.items('paths/{path}/{operation}'):
            path, operation = k.values()
            if operation not in ALLOWED_OPERATIONS:
                continue
            path = base_path + path
            op = node.get('operationId') or default_operation_id(path, operation)
            operator = Operator(op, self.default_package)
            self.router.set(operator, path, operation)

        return self

    def respond(self, request):
        authorizer, validator, operator = self.router.route(request)
        headers = authorizer.authorize(request) if authorizer else []
        params = validator.validate(request) if validator else {}
        res = operator.operate(request, **params)
        if not isinstance(res, Response):
            res = JSONResponse(res)
        res.headers += headers
        return res

    def abort(self, request, exception):
        return self.capture(request, exception)

    def capture(self, request, exception):
        for cls in type(exception).__mro__:
            if cls in self.exception_captors:
                return self.exception_captors[cls](request, exception)
        return respond_capture(request, exception)

    def on(self, event, listener):
        self.listeners.setdefault(event, []).append(listener)

    def off(self, event, listener):
        try:
            self.listeners.get(event, []).remove(listener)
        except ValueError:
            pass

    def trigger(self, event, *args, **kwargs):
        if event in self.listeners:
            for l in self.listeners[event]:
                l(*args, **kwargs)

    def log(self, *args, **kwargs):
        self.trigger('log', *args, **kwargs)

    def wsgi(
            self,
            environ: dict,
            start_response: typing.Callable
        ) -> typing.Sequence:
        try:
            environ['fermata.application'] = self
            request = Request(environ)
            self.trigger('request', request=request)
            response = self.respond(request)
            self.trigger('respond', request=request, response=response)
        except HTTPException as e:
            response = self.abort(request, e)
            self.trigger('abort', request=request, response=response)
        except Exception as e:
            response = self.capture(request, e)
            self.trigger('capture', request=request, response=response)

        return response(environ, start_response)

    def __call__(
            self,
            environ: dict,
            start_response: typing.Callable
        ) -> typing.Sequence:
        return self.wsgi(environ, start_response)