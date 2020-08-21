from requests import post

BASE_ROUTE = "https://analytics.jederu.nl"

class Analytics:

    def __init__(self, key):
        self.key = key

    def sendAction(self, message):
        data = {"key": self.key, "message": message}
        post(BASE_ROUTE + "/api/activation/", data=data)