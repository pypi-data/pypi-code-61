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
from agilicus_api.models.environment_config import EnvironmentConfig  # noqa: E501
from agilicus_api.rest import ApiException

class TestEnvironmentConfig(unittest.TestCase):
    """EnvironmentConfig unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test EnvironmentConfig
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = agilicus_api.models.environment_config.EnvironmentConfig()  # noqa: E501
        if include_optional :
            return EnvironmentConfig(
                id = '123', 
                app_id = '123', 
                environment_name = '123', 
                maintenance_org_id = '0', 
                config_type = 'configmap_mount', 
                mount_domain = '0', 
                mount_username = '0', 
                mount_password = '0', 
                mount_hostname = 'mount.example.com', 
                mount_share = '0', 
                mount_src_path = '0', 
                mount_path = '0', 
                file_store_uri = '0', 
                env_config_vars = [
                    agilicus_api.models.environment_config_var.EnvironmentConfigVar(
                        name = '_ab2a', 
                        value = '0', )
                    ]
            )
        else :
            return EnvironmentConfig(
                maintenance_org_id = '0',
                config_type = 'configmap_mount',
        )

    def testEnvironmentConfig(self):
        """Test EnvironmentConfig"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
