import functools

import requests

from cotoba_cli.error import ApiResponseError


def handle_requests_exception(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except requests.exceptions.HTTPError as e:
            raise ApiResponseError(
                status_code=e.response.status_code, body=e.response.text)
        except requests.exceptions.RequestException as e:
            raise RuntimeError(e)
    return wrapper
