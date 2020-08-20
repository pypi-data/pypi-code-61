from ..http import MyHttp


class Pool:
    def __init__(self, _http: MyHttp) -> None:
        self._http = _http

    def all(self):
        return self._http.get('/api/experimental/pools')

    def one(self, name):
        return self._http.get('/api/experimental/pools/{}'.format(name))
