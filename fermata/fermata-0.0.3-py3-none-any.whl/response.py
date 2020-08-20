import typing
import json

HTTP_STATUS_PHRASE = {
    100: "CONTINUE",
    101: "SWITCHING PROTOCOLS",
    102: "PROCESSING",
    200: "OK",
    201: "CREATED",
    202: "ACCEPTED",
    203: "NON AUTHORITATIVE INFORMATION",
    204: "NO CONTENT",
    205: "RESET CONTENT",
    206: "PARTIAL CONTENT",
    207: "MULTI STATUS",
    208: "ALREADY REPORTED",
    226: "IM USED",
    300: "MULTIPLE CHOICES",
    301: "MOVED PERMANENTLY",
    302: "FOUND",
    303: "SEE OTHER",
    304: "NOT MODIFIED",
    305: "USE PROXY",
    307: "TEMPORARY REDIRECT",
    308: "PERMANENT REDIRECT",
    400: "BAD REQUEST",
    401: "UNAUTHORIZED",
    402: "PAYMENT REQUIRED",
    403: "FORBIDDEN",
    404: "NOT FOUND",
    405: "METHOD NOT ALLOWED",
    406: "NOT ACCEPTABLE",
    407: "PROXY AUTHENTICATION REQUIRED",
    408: "REQUEST TIMEOUT",
    409: "CONFLICT",
    410: "GONE",
    411: "LENGTH REQUIRED",
    412: "PRECONDITION FAILED",
    413: "REQUEST ENTITY TOO LARGE",
    414: "REQUEST URI TOO LONG",
    415: "UNSUPPORTED MEDIA TYPE",
    416: "REQUESTED RANGE NOT SATISFIABLE",
    417: "EXPECTATION FAILED",
    421: "MISDIRECTED REQUEST",
    422: "UNPROCESSABLE ENTITY",
    423: "LOCKED",
    424: "FAILED DEPENDENCY",
    426: "UPGRADE REQUIRED",
    428: "PRECONDITION REQUIRED",
    429: "TOO MANY REQUESTS",
    431: "REQUEST HEADER FIELDS TOO LARGE",
    451: "UNAVAILABLE FOR LEGAL REASONS",
    500: "INTERNAL SERVER ERROR",
    501: "NOT IMPLEMENTED",
    502: "BAD GATEWAY",
    503: "SERVICE UNAVAILABLE",
    504: "GATEWAY TIMEOUT",
    505: "HTTP VERSION NOT SUPPORTED",
    506: "VARIANT ALSO NEGOTIATES",
    507: "INSUFFICIENT STORAGE",
    508: "LOOP DETECTED",
    510: "NOT EXTENDED",
    511: "NETWORK AUTHENTICATION REQUIRED",
}


def status_code_phrase(status_code):
    phrase = HTTP_STATUS_PHRASE.get(status_code, 'UNKNOWN')
    return '%d %s' % (status_code, phrase)


class Response(object):

    charset = 'utf-8'
    MIME = 'text/plain'

    def __init__(
            self,
            body: typing.Any,
            status_code: int = 200,
            headers: typing.Sequence[typing.Tuple[str, str]] = None,
            media_type=None
        ):
        self.body = body
        self.status_code = status_code
        self.headers = headers or []
        self.media_type = media_type

    def bytes(self) -> typing.Sequence:
        return self.body.encode(self.charset)

    def __call__(
            self,
            environ: dict,
            start_response: typing.Callable
        ) -> typing.Sequence:
        status = status_code_phrase(self.status_code)
        headers = self.headers + [(
                'content-type', 
                f'{self.MIME};charset={self.charset}')]

        start_response(status, [(str(k), str(v)) for k, v in headers])

        return [self.bytes(), b'\n']


class JSONResponse(Response):

    MIME = 'application/json'

    def bytes(self) -> typing.Sequence:
        return json.dumps(
                self.body,
                ensure_ascii=False
            ).encode(self.charset)
