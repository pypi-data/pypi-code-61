# coding: utf-8

"""
    Agilicus API

    Agilicus API endpoints  # noqa: E501

    The version of the OpenAPI document: 2020.08.06
    Contact: dev@agilicus.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from agilicus_api.configuration import Configuration


class MessageEndpointSpec(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'endpoint_type': 'MessageEndpointType',
        'nickname': 'str',
        'address': 'str',
        'enabled': 'bool'
    }

    attribute_map = {
        'endpoint_type': 'endpoint_type',
        'nickname': 'nickname',
        'address': 'address',
        'enabled': 'enabled'
    }

    def __init__(self, endpoint_type=None, nickname=None, address=None, enabled=None, local_vars_configuration=None):  # noqa: E501
        """MessageEndpointSpec - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._endpoint_type = None
        self._nickname = None
        self._address = None
        self._enabled = None
        self.discriminator = None

        if endpoint_type is not None:
            self.endpoint_type = endpoint_type
        if nickname is not None:
            self.nickname = nickname
        if address is not None:
            self.address = address
        if enabled is not None:
            self.enabled = enabled

    @property
    def endpoint_type(self):
        """Gets the endpoint_type of this MessageEndpointSpec.  # noqa: E501


        :return: The endpoint_type of this MessageEndpointSpec.  # noqa: E501
        :rtype: MessageEndpointType
        """
        return self._endpoint_type

    @endpoint_type.setter
    def endpoint_type(self, endpoint_type):
        """Sets the endpoint_type of this MessageEndpointSpec.


        :param endpoint_type: The endpoint_type of this MessageEndpointSpec.  # noqa: E501
        :type: MessageEndpointType
        """

        self._endpoint_type = endpoint_type

    @property
    def nickname(self):
        """Gets the nickname of this MessageEndpointSpec.  # noqa: E501

        User-supplied name (e.g. My-Yubikey, don's laptop)  # noqa: E501

        :return: The nickname of this MessageEndpointSpec.  # noqa: E501
        :rtype: str
        """
        return self._nickname

    @nickname.setter
    def nickname(self, nickname):
        """Sets the nickname of this MessageEndpointSpec.

        User-supplied name (e.g. My-Yubikey, don's laptop)  # noqa: E501

        :param nickname: The nickname of this MessageEndpointSpec.  # noqa: E501
        :type: str
        """

        self._nickname = nickname

    @property
    def address(self):
        """Gets the address of this MessageEndpointSpec.  # noqa: E501

        Type-specific address info (e.g. phone num, push-context json, ...)  # noqa: E501

        :return: The address of this MessageEndpointSpec.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this MessageEndpointSpec.

        Type-specific address info (e.g. phone num, push-context json, ...)  # noqa: E501

        :param address: The address of this MessageEndpointSpec.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def enabled(self):
        """Gets the enabled of this MessageEndpointSpec.  # noqa: E501

        The status of the message endpoint, `true` when the endpoint is enabled, and `false` when the endpoint is disabled.  # noqa: E501

        :return: The enabled of this MessageEndpointSpec.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this MessageEndpointSpec.

        The status of the message endpoint, `true` when the endpoint is enabled, and `false` when the endpoint is disabled.  # noqa: E501

        :param enabled: The enabled of this MessageEndpointSpec.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, MessageEndpointSpec):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MessageEndpointSpec):
            return True

        return self.to_dict() != other.to_dict()
