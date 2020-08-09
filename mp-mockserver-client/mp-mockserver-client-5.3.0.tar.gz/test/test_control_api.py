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
from mockserver.api.control_api import ControlApi  # noqa: E501
from mockserver.rest import ApiException


class TestControlApi(unittest.TestCase):
    """ControlApi unit test stubs"""

    def setUp(self):
        self.api = mockserver.api.control_api.ControlApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_bind_put(self):
        """Test case for bind_put

        bind additional listening ports  # noqa: E501
        """
        pass

    def test_clear_put(self):
        """Test case for clear_put

        clears expectations and recorded requests that match the request matcher  # noqa: E501
        """
        pass

    def test_reset_put(self):
        """Test case for reset_put

        clears all expectations and recorded requests  # noqa: E501
        """
        pass

    def test_retrieve_put(self):
        """Test case for retrieve_put

        retrieve recorded requests, active expectations, recorded expectations or log messages  # noqa: E501
        """
        pass

    def test_status_put(self):
        """Test case for status_put

        return listening ports  # noqa: E501
        """
        pass

    def test_stop_put(self):
        """Test case for stop_put

        stop running process  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
