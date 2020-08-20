class HTTPCodeError(Exception):
    def __init__(self, status_code, *args, **kwargs):
        self.status_code = status_code
        self.message = kwargs.pop('message', None)
        super().__init__(*args, **kwargs)


class DagRunTimeOutError(Exception):
    pass
