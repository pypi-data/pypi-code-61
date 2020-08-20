import requests
from .exceptions import HTTPCodeError


class MyHttp:
    def __init__(self, base_url: str) -> None:
        self.base_url = base_url[:-1] if base_url.endswith('/') else base_url

    def __check_response(self, rep):
        rep_json = rep.json()
        if rep.status_code != 200:
            raise HTTPCodeError(rep.status_code, message=rep_json.get('error', None))
        return rep_json

    def get(self, endpoint, params=None, **kwargs):
        rep = requests.get('{}{}'.format(self.base_url, endpoint), params=params, **kwargs)
        return self.__check_response(rep)

    def post(self, endpoint, data=None, json=None, **kwargs):
        rep = requests.post('{}{}'.format(self.base_url, endpoint), data=data, json=json, **kwargs)
        return self.__check_response(rep)

    def put(self, endpoint, data=None, **kwargs):
        rep = requests.put('{}{}'.format(self.base_url, endpoint), data=data, **kwargs)
        return self.__check_response(rep)

    def delete(self, endpoint, **kwargs):
        rep = requests.delete('{}{}'.format(self.base_url, endpoint), **kwargs)
        return self.__check_response(rep)
