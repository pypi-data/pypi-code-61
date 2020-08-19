import logging
import time
import requests
from datetime import datetime


class Utils:

    @staticmethod
    def log_time_of_function(function):
        def wrapped(*args):
            start_time = time.time()
            res = function(*args)
            arguments_str = ", ".join([str(item) for item in args])
            logging.info("function {func}, args: ({args_str}),secs: {delta_time:.3f}"
                         .format(func=function.__name__, args_str=arguments_str, delta_time=time.time() - start_time))
            return res

        return wrapped

    @staticmethod
    def get_date(date):
        d = None
        if date is not None:
            date_list = [int(item) for item in date.split('.')]
            d = datetime.today().replace(year=date_list[0], month=date_list[1], day=date_list[2])
        return d

    @staticmethod
    def get_response(method="get", url="", data=None):
        if data is None:
            data = {}

        headers = {
            "accept": "text/html,application/xhtml+xml,application/xml",
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
            (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
        }

        response = requests.get(url, headers=headers, verify=True)
        if method == "post":
            headers["cookie"] = '; '.join([x.name + '=' + x.value for x in response.cookies])
            headers["content-type"] = 'application/x-www-form-urlencoded'
            response = requests.post(url, data=data, headers=headers, verify=True)

        return response
