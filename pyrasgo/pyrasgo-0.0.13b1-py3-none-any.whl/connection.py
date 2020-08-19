import os
import amplitude
import requests


class Connection(object):
    """
    Base class for all Rasgo objects to facilitate API calls.
    """

    def __init__(self, api_key=None):
        self._api_key = api_key
        self._production_domain = "api.rasgoml.com"
        self._amplitude_key = "08836b1e33763119e01fc62c604a7ea8"

        self._event_logger = amplitude.AmplitudeLogger(api_key=self._amplitude_key)
        self._hostname = os.environ.get("RASGO_DOMAIN", self._production_domain)

        if self._hostname != self._production_domain:
            self._event_logger.turn_off_logging()

    def _url(self, resource):
        if '/' == resource[0]:
            resource = resource[1:]
        return f'https://{self._hostname}/{resource}'

    def _get(self, endpoint, params=None) -> requests.Response:
        """
        Performs GET request to Rasgo API as defined within the class instance.

        :param endpoint: Target resource to GET from API.
        :param params: Additional parameters to specify for GET request.
        :return: Response object containing content returned.
        """
        response = requests.get(self._url(endpoint),
                                headers=self._headers(self._api_key),
                                params=params or {})
        response.raise_for_status()
        return response

    def _patch(self, resource, _json=None, params=None) -> requests.Response:
        """
        Performs PATCH request to Rasgo API as defined within the class instance.

        :param resource: Target resource to POST from API.
        :param _json: JSON object to send in POST request
        :param params: Additional parameters to specify for POST request.
        :return: Response object containing content returned.
        """
        response = requests.patch(self._url(resource),
                                  json=_json,
                                  headers=self._headers(self._api_key),
                                  params=params or {})
        response.raise_for_status()
        return response

    def _post(self, resource, _json=None, params=None) -> requests.Response:
        """
        Performs POST request to Rasgo API as defined within the class instance.

        :param resource: Target resource to POST from API.
        :param _json: JSON object to send in POST request
        :param params: Additional parameters to specify for POST request.
        :return: Response object containing content returned.
        """
        response = requests.post(self._url(resource),
                                 json=_json,
                                 headers=self._headers(self._api_key),
                                 params=params or {})
        response.raise_for_status()
        return response

    @staticmethod
    def _headers(api_key) -> dict:
        if not api_key:
            raise ValueError("Must provide an API key to access the endpoint")
        return {
            "accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}",
        }


