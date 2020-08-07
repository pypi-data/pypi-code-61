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
from agilicus_api.models.message_endpoint import MessageEndpoint  # noqa: E501
from agilicus_api.rest import ApiException

class TestMessageEndpoint(unittest.TestCase):
    """MessageEndpoint unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test MessageEndpoint
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = agilicus_api.models.message_endpoint.MessageEndpoint()  # noqa: E501
        if include_optional :
            return MessageEndpoint(
                metadata = agilicus_api.models.message_endpoint_metadata.MessageEndpointMetadata(
                    message_endpoint_id = '123', 
                    user_id = '123', 
                    created = '2015-07-07T15:49:51.230+02:00', 
                    updated = '2015-07-07T15:49:51.230+02:00', ), 
                spec = agilicus_api.models.message_endpoint_spec.MessageEndpointSpec(
                    endpoint_type = 'web_push', 
                    nickname = '0', 
                    address = '0', 
                    enabled = True, )
            )
        else :
            return MessageEndpoint(
        )

    def testMessageEndpoint(self):
        """Test MessageEndpoint"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
