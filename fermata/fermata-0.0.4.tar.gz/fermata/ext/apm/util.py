from wsgiref.util import request_uri

from elasticapm.conf import constants
from elasticapm.utils import get_url_dict
from elasticapm.utils.wsgi import get_environ, get_headers


def get_data_from_request(request, config, event_type):
    result = {
        "env": dict(get_environ(request.environ)),
        "method": request.method,
        "socket": {"remote_address": request.environ.get("REMOTE_ADDR")},
    }
    if config.capture_headers:
        result["headers"] = dict(get_headers(request.environ))
    if request.method.upper() in constants.HTTP_WITH_BODY:
        if config.capture_body not in ("all", event_type):
            result["body"] = "[REDACTED]"
        else:
            result["body"] = request.content

    result["url"] = get_url_dict(request_uri(request.environ))

    return result


def get_data_from_response(response, config, event_type):
    return {
    	'status_code': response.status_code,
    	'headers': dict(response.headers)
    }
