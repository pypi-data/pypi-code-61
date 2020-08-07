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
from agilicus_api.models.user_roles import UserRoles  # noqa: E501
from agilicus_api.rest import ApiException

class TestUserRoles(unittest.TestCase):
    """UserRoles unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test UserRoles
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = agilicus_api.models.user_roles.UserRoles()  # noqa: E501
        if include_optional :
            return UserRoles(
                user_id = '123', 
                roles = {"app-1":["viewer"],"app-2":["owner"]}
            )
        else :
            return UserRoles(
        )

    def testUserRoles(self):
        """Test UserRoles"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
