from ..http import MyHttp
from .dag import DagRun
from .pool import Pool


class Client:
    def __init__(self, base_url) -> None:
        self.__http = MyHttp(base_url)
        self.dag = DagRun(self.__http)
        self.pool = Pool(self.__http)

    def test(self):
        return self.__http.get('/api/experimental/test')
