# coding: utf-8

"""
    Agilicus API

    Agilicus API endpoints  # noqa: E501

    The version of the OpenAPI document: 2020.08.06
    Contact: dev@agilicus.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import agilicus_api
from agilicus_api.models.issuer_client import IssuerClient  # noqa: E501
from agilicus_api.rest import ApiException

class TestIssuerClient(unittest.TestCase):
    """IssuerClient unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test IssuerClient
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = agilicus_api.models.issuer_client.IssuerClient()  # noqa: E501
        if include_optional :
            return IssuerClient(
                id = '123', 
                issuer_id = '123', 
                name = '0', 
                secret = '0', 
                application = '0', 
                org_id = '0', 
                restricted_organisations = ["org-1","org-2"], 
                organisation_scope = 'here_only', 
                redirects = [
                    '0'
                    ], 
                mfa_challenge = 'user_preference'
            )
        else :
            return IssuerClient(
                name = '0',
        )

    def testIssuerClient(self):
        """Test IssuerClient"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
