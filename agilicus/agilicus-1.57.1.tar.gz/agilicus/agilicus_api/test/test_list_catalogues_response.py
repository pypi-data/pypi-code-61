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
from agilicus_api.models.list_catalogues_response import ListCataloguesResponse  # noqa: E501
from agilicus_api.rest import ApiException

class TestListCataloguesResponse(unittest.TestCase):
    """ListCataloguesResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ListCataloguesResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = agilicus_api.models.list_catalogues_response.ListCataloguesResponse()  # noqa: E501
        if include_optional :
            return ListCataloguesResponse(
                catalogues = [
                    agilicus_api.models.catalogue.Catalogue(
                        id = '123', 
                        category = '0', 
                        catalogue_entries = [
                            agilicus_api.models.catalogue_entry.CatalogueEntry(
                                catalogue_id = '123', 
                                catalogue_category = '0', 
                                name = 'dotnet_core', 
                                content = 'cr.agilicus.com/dotnet_core/app-image:latest', 
                                tag = 'V1.1', 
                                short_description = '0', 
                                long_description = '0', 
                                created = '2015-07-07T15:49:51.230+02:00', 
                                updated = '2015-07-07T15:49:51.230+02:00', )
                            ], 
                        created = '2015-07-07T15:49:51.230+02:00', 
                        updated = '2015-07-07T15:49:51.230+02:00', )
                    ], 
                limit = 56
            )
        else :
            return ListCataloguesResponse(
                limit = 56,
        )

    def testListCataloguesResponse(self):
        """Test ListCataloguesResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
