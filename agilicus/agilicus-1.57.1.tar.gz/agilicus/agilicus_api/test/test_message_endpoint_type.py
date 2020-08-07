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
from agilicus_api.models.message_endpoint_type import MessageEndpointType  # noqa: E501
from agilicus_api.rest import ApiException

class TestMessageEndpointType(unittest.TestCase):
    """MessageEndpointType unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test MessageEndpointType
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = agilicus_api.models.message_endpoint_type.MessageEndpointType()  # noqa: E501
        if include_optional :
            return MessageEndpointType(
            )
        else :
            return MessageEndpointType(
        )

    def testMessageEndpointType(self):
        """Test MessageEndpointType"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
