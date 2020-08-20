import requests


class YTKD:
    """ This class is used to encapsulate all attributes and methods pertaining to CNN Classifiers. """

    def __init__(self, url, keywords):
        self.url = url
        self.keywords = keywords
        self.API_ENDPOINT = "http://ytkd-env.eba-jcpqnkgc.ap-south-1.elasticbeanstalk.com/api"
        super().__init__()

    def make_request(self, get_expected_time_only):
        # data to be sent to api
        request_data = {'url': self.url,
                        'keywords': self.keywords,
                        'get_expected_time_only': get_expected_time_only}

        # sending post request and saving response as response object
        r = requests.post(url=self.API_ENDPOINT, data=request_data)
        return r.json()

    def get_expected_time(self):
        return self.make_request(get_expected_time_only=True)

    def get_results(self):
        return self.make_request(get_expected_time_only=False)
