# coding: utf-8

"""
    Mock Server API

    MockServer enables easy mocking of any system you integrate with via HTTP or HTTPS with clients written in Java, JavaScript and Ruby and a simple REST API (as shown below).  MockServer Proxy is a proxy that introspects all proxied traffic including encrypted SSL traffic and supports Port Forwarding, Web Proxying (i.e. HTTP proxy), HTTPS Tunneling Proxying (using HTTP CONNECT) and SOCKS Proxying (i.e. dynamic port forwarding).  Both MockServer and the MockServer Proxy record all received requests so that it is possible to verify exactly what requests have been sent by the system under test.  # noqa: E501

    OpenAPI spec version: 5.3.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import mockserver
from mockserver.models.times import Times  # noqa: E501
from mockserver.rest import ApiException


class TestTimes(unittest.TestCase):
    """Times unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTimes(self):
        """Test Times"""
        # FIXME: construct object with mandatory attributes with example values
        # model = mockserver.models.times.Times()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
