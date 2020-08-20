import typing


class HTTPException(Exception):

    status_code = None
    error_code = None
    message = 'HTTP Exception'

    _headers = []

    def __init__(self,
            message: str = None,
            error_code: str = None,
            headers: typing.Sequence[typing.Tuple[str, str]] = None
        ) -> None:
        if message is not None:
            self.message = message
        if error_code is not None:
            self.error_code = error_code
        if headers is not None:
            self._headers = headers

    @property
    def body(self):
        return { k: getattr(self, k) 
            for k in self.__class__.__dict__
            if not k.startswith('_') }

    @property
    def headers(self):
        return self._headers

    def keys(self):
        return ['status_code', 'body', 'headers']

    def __getitem__(self, k):
        return getattr(self, k)


class BadRequest(HTTPException):

    status_code = 400
    error_code = 'bad_request'
    message = 'Bad Request'


class JSONDecodeError(BadRequest):

    error_code = 'json_decode_error'
    message = 'JSON DecodeError'


class Unauthorized(BadRequest):

    status_code = 401
    error_code = 'unauthorized'
    message = 'Unauthorized'


class Forbidden(BadRequest):

    status_code = 403
    error_code = 'forbidden'
    message = 'Forbidden'


class NotFound(BadRequest):

    status_code = 404
    error_code = 'path_not_found'
    message = 'Request Path Not Found'


class UnprocessableEntity(BadRequest):

    status_code = 422
    error_code = 'unprocessable_entity'
    message = 'Unprocessable Entity'


class VerificationFailed(UnprocessableEntity):

    error_code = 'verification_failed'
    message = 'Verification Failed'
    details = None

    def __init__(
            self,
            details: typing.Sequence[typing.Dict[str, str]],
            message: str = None,
            error_code: str = None,
            headers: typing.Sequence[typing.Tuple[str, str]] = None
        ) -> None:
        super(VerificationFailed, self).__init__(message, error_code, headers)
        self.details = details


class PathNotFound(NotFound):

    error_code = 'path_not_found'
    message = 'Request Path Not Found'


class PathNotFound(NotFound):

    error_code = 'path_not_found'
    message = 'Request Path Not Found'


class MethodNotAllowed(BadRequest):

    status_code = 405
    error_code = 'method_not_allowed'
    message = 'Method Not Allowed'        


class InternalServerError(HTTPException):

    status_code = 500
    error_code = 'internal_server_error'
    message = 'Internal Server Error'        


class BadGateway(InternalServerError):

    status_code = 502
    error_code = 'bad_gateway'
    message = 'Bad Gateway'        


class BadOperationId(BadGateway):

    error_code = 'bad_operation_id'
    message = 'Bad Operation Id'        
