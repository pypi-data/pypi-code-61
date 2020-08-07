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
from agilicus_api.models.rule_v2 import RuleV2  # noqa: E501
from agilicus_api.rest import ApiException

class TestRuleV2(unittest.TestCase):
    """RuleV2 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test RuleV2
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = agilicus_api.models.rule_v2.RuleV2()  # noqa: E501
        if include_optional :
            return RuleV2(
                metadata = {"id":"ac233asaksjfF","created":"2017-07-07T15:49:51.230+00:00","updated":"2020-01-27T12:19:46.430+00:00"}, 
                spec = agilicus_api.models.rule_spec.RuleSpec(
                    app_id = '123', 
                    comments = 'This rule allows access to all static content of the application for any user, even if they are not authenticated.', 
                    condition = agilicus_api.models.http_rule.HttpRule(
                        rule_type = 'HttpRule', 
                        methods = ["get"], 
                        path_regex = '/.*', 
                        query_parameters = [
                            agilicus_api.models.rule_query_parameter.RuleQueryParameter(
                                name = '0', 
                                exact_match = '0', )
                            ], 
                        body = agilicus_api.models.rule_query_body.RuleQueryBody(
                            json = [
                                agilicus_api.models.rule_query_body_json.RuleQueryBodyJSON(
                                    name = '0', 
                                    exact_match = '0', 
                                    match_type = 'string', 
                                    pointer = '/foo/0/a~1b/2', )
                                ], ), ), 
                    org_id = '123', 
                    scope = 'anyone', )
            )
        else :
            return RuleV2(
                spec = agilicus_api.models.rule_spec.RuleSpec(
                    app_id = '123', 
                    comments = 'This rule allows access to all static content of the application for any user, even if they are not authenticated.', 
                    condition = agilicus_api.models.http_rule.HttpRule(
                        rule_type = 'HttpRule', 
                        methods = ["get"], 
                        path_regex = '/.*', 
                        query_parameters = [
                            agilicus_api.models.rule_query_parameter.RuleQueryParameter(
                                name = '0', 
                                exact_match = '0', )
                            ], 
                        body = agilicus_api.models.rule_query_body.RuleQueryBody(
                            json = [
                                agilicus_api.models.rule_query_body_json.RuleQueryBodyJSON(
                                    name = '0', 
                                    exact_match = '0', 
                                    match_type = 'string', 
                                    pointer = '/foo/0/a~1b/2', )
                                ], ), ), 
                    org_id = '123', 
                    scope = 'anyone', ),
        )

    def testRuleV2(self):
        """Test RuleV2"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
