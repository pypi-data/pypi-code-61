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
from agilicus_api.models.combined_user_detail_status import CombinedUserDetailStatus  # noqa: E501
from agilicus_api.rest import ApiException

class TestCombinedUserDetailStatus(unittest.TestCase):
    """CombinedUserDetailStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CombinedUserDetailStatus
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = agilicus_api.models.combined_user_detail_status.CombinedUserDetailStatus()  # noqa: E501
        if include_optional :
            return CombinedUserDetailStatus(
                user = {"id":"as3sdfl","first_name":"Example","last_name":"User","email":"user@example.com","type":"user"}, 
                mfa_challenge_methods = [
                    agilicus_api.models.mfa_challenge_method.MFAChallengeMethod(
                        metadata = {"id":"ac233asaksjfF","created":"2017-07-07T15:49:51.230+00:00","updated":"2020-01-27T12:19:46.430+00:00"}, 
                        spec = agilicus_api.models.mfa_challenge_method_spec.MFAChallengeMethodSpec(
                            priority = 1, 
                            challenge_type = '0', 
                            endpoint = '0', 
                            nickname = '0', 
                            enabled = True, ), )
                    ]
            )
        else :
            return CombinedUserDetailStatus(
        )

    def testCombinedUserDetailStatus(self):
        """Test CombinedUserDetailStatus"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
