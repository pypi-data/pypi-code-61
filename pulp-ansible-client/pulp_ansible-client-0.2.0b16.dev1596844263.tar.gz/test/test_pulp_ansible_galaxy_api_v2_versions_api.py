# coding: utf-8

"""
    Pulp 3 API

    Fetch, Upload, Organize, and Distribute Software Packages  # noqa: E501

    The version of the OpenAPI document: v3
    Contact: pulp-list@redhat.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import pulpcore.client.pulp_ansible
from pulpcore.client.pulp_ansible.api.pulp_ansible_galaxy_api_v2_versions_api import PulpAnsibleGalaxyApiV2VersionsApi  # noqa: E501
from pulpcore.client.pulp_ansible.rest import ApiException


class TestPulpAnsibleGalaxyApiV2VersionsApi(unittest.TestCase):
    """PulpAnsibleGalaxyApiV2VersionsApi unit test stubs"""

    def setUp(self):
        self.api = pulpcore.client.pulp_ansible.api.pulp_ansible_galaxy_api_v2_versions_api.PulpAnsibleGalaxyApiV2VersionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_read(self):
        """Test case for read

        """
        pass


if __name__ == '__main__':
    unittest.main()
