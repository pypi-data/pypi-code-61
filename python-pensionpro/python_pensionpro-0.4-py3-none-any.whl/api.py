import requests
from pensionpro.errors import *

class ContactAPI(object):
    def __init__(self, api):
        self._api = api
    
    def get_contact(self, contact_id, expand_string=""):
        """Fetches the contact for the given contact ID"""
        url = f'contacts/{contact_id}'
        contact = self._api._get(url, expand_string=expand_string)
        return contact

class PlanAPI(object):
    def __init__(self, api):
        self._api = api

    def get_plan(self, plan_id, expand_string=""):
        """Fetches the plan for the given plan ID"""
        url = f'plans/{plan_id}'
        plan = self._api._get(url, expand_string=expand_string)
        return plan

class PlanContactRoleAPI(object):
    def __init__(self, api):
        self._api = api
    
    def get_plan_contact_role(self, plan_contact_role_id, expand_string=""):
        """Fetches the plan contact role for the given plan contact role ID
            NOTE: A PlanContactRole is the association between a plan and a contact. This is NOT the role type!
        """
        url = f'plancontactroles/{plan_contact_role_id}'
        plan_contact_role = self._api._get(url, expand_string="")
        return plan_contact_role

    def list_plan_contact_roles(self, filter_string="", expand_string=""):
        """Returns a list of all plan contact roles that match the filter"""
        url = f'plancontactroles'
        response = self._api._get(url, filter_string=filter_string, expand_string=expand_string)

        plan_contact_roles = []

        for plan_contact_role in response['Values']:
            plan_contact_roles.append(plan_contact_role)
        return plan_contact_roles

class API(object):
    def __init__(self, username, api_key):
        """Creates a wrapper to perform API actions.

        Arguments:
            username: PensionPro username
            api_key: API Key
        """

        self._session = requests.Session()
        self._session.headers = {'accept': 'application/json', 'username': username, 'apikey': api_key}
        self._api_prefix = 'https://api.pensionpro.com/v1/'

        self.contacts = ContactAPI(self)
        self.plans = PlanAPI(self)
        self.plan_contact_roles = PlanContactRoleAPI(self)
    
    def _action(self, r):
        try:
            j = r.json()
        except ValueError:
            j = {}
        
        error_message = 'PensionPro Request Failed'
        if "errors" in j:
            error_message = f'{j.get("description")}: {j.get("errors")}'
        elif "message" in j:
            error_message = j["message"]

        if r.status_code == 400:
            raise PensionProBadRequest(error_message)
        elif r.status_code == 401:
            raise PensionProUnauthorized(error_message)
        elif r.status_code == 403:
            raise PensionProAccessDenied(error_message)
        elif r.status_code == 404:
            raise PensionProNotFound(error_message)
        elif r.status_code == 429:
            raise PensionProRateLimited(
                f'429 Rate Limit Exceeded: API rate-limit has been reached untill {r.headers.get("x-retry-after-seconds")} seconds.'
            )
        elif 500 < r.status_code < 600:
            raise PensionProServerError(f'{r.status_code}: Server Error')
        
        # Catch other errors
        try:
            r.raise_for_status()
        except HTTPError as e:
            raise PensionProError(f'{e}: {j}')

        # Return json object
        return j

    def _get(self, url, filter_string="", expand_string=""):
        """Wrapper around request.get() to use API prefix. Returns the JSON response."""
        complete_url = f'{self._api_prefix}{url}'
        if (filter_string == "") and (expand_string == ""):
            pass
        elif filter_string == "":
            complete_url = f'{complete_url}?$expand={expand_string}'
        elif expand_string == "":
            complete_url = f'{complete_url}?$filter={filter_string}'
        else:
            complete_url = f'{complete_url}?$filter={filter_string}&$expand={expand_string}'

        print(complete_url)
        request = self._session.get(complete_url)
        return self._action(request)