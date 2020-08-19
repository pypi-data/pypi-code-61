import requests


class YTKD():
    @staticmethod
    def get_expected_time(request_data):
        API_ENDPOINT = "http://ytkd-env.eba-jcpqnkgc.ap-south-1.elasticbeanstalk.com/api"
        # API_ENDPOINT = 'http://127.0.0.1:5000/api'

        # data to be sent to api
        request_data['get_expected_time_only'] = True

        # sending post request and saving response as response object
        r = requests.post(url=API_ENDPOINT, data=request_data)
        return r.json()

    @staticmethod
    def get_results(request_data):
        API_ENDPOINT = "http://ytkd-env.eba-jcpqnkgc.ap-south-1.elasticbeanstalk.com/api"
        # API_ENDPOINT = 'http://127.0.0.1:5000/api'

        # data to be sent to api
        request_data['get_expected_time_only'] = False

        # sending post request and saving response as response object
        r = requests.post(url=API_ENDPOINT, data=request_data)
        return r.json()
