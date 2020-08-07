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

import agilicus_api
from agilicus_api.api.audits_api import AuditsApi  # noqa: E501
from agilicus_api.rest import ApiException


class TestAuditsApi(unittest.TestCase):
    """AuditsApi unit test stubs"""

    def setUp(self):
        self.api = agilicus_api.api.audits_api.AuditsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_list_audits(self):
        """Test case for list_audits

        View audit records  # noqa: E501
        """
        pass

    def test_list_auth_records(self):
        """Test case for list_auth_records

        View authentication audit records  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
