# coding: utf-8

"""
    gnomock

    `gnomock` is an HTTP wrapper for [Gnomock](https://github.com/orlangure/gnomock) integration and end-to-end testing toolkit. It allows to use Gnomock outside of Go ecosystem. Not all Gnomock features exist in this wrapper, but official presets, as well as basic general configuration, are supported.   # noqa: E501

    The version of the OpenAPI document: 1.4.2
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from gnomock.configuration import Configuration


class Splunk(object):
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
        'values': 'list[SplunkValues]',
        'values_file': 'str',
        'accept_license': 'bool',
        'admin_password': 'str',
        'version': 'str'
    }

    attribute_map = {
        'values': 'values',
        'values_file': 'values_file',
        'accept_license': 'accept_license',
        'admin_password': 'admin_password',
        'version': 'version'
    }

    def __init__(self, values=None, values_file=None, accept_license=None, admin_password=None, version='latest', local_vars_configuration=None):  # noqa: E501
        """Splunk - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._values = None
        self._values_file = None
        self._accept_license = None
        self._admin_password = None
        self._version = None
        self.discriminator = None

        if values is not None:
            self.values = values
        if values_file is not None:
            self.values_file = values_file
        self.accept_license = accept_license
        self.admin_password = admin_password
        if version is not None:
            self.version = version

    @property
    def values(self):
        """Gets the values of this Splunk.  # noqa: E501

        A list of events to ingest into the container.  # noqa: E501

        :return: The values of this Splunk.  # noqa: E501
        :rtype: list[SplunkValues]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this Splunk.

        A list of events to ingest into the container.  # noqa: E501

        :param values: The values of this Splunk.  # noqa: E501
        :type: list[SplunkValues]
        """

        self._values = values

    @property
    def values_file(self):
        """Gets the values_file of this Splunk.  # noqa: E501

        File name with events to ingest into Splunk. Use JSON Lines format (every event is a separate JSON object), each new event starts from a new line.   # noqa: E501

        :return: The values_file of this Splunk.  # noqa: E501
        :rtype: str
        """
        return self._values_file

    @values_file.setter
    def values_file(self, values_file):
        """Sets the values_file of this Splunk.

        File name with events to ingest into Splunk. Use JSON Lines format (every event is a separate JSON object), each new event starts from a new line.   # noqa: E501

        :param values_file: The values_file of this Splunk.  # noqa: E501
        :type: str
        """

        self._values_file = values_file

    @property
    def accept_license(self):
        """Gets the accept_license of this Splunk.  # noqa: E501

        Accept or decline Splunk license.  # noqa: E501

        :return: The accept_license of this Splunk.  # noqa: E501
        :rtype: bool
        """
        return self._accept_license

    @accept_license.setter
    def accept_license(self, accept_license):
        """Sets the accept_license of this Splunk.

        Accept or decline Splunk license.  # noqa: E501

        :param accept_license: The accept_license of this Splunk.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and accept_license is None:  # noqa: E501
            raise ValueError("Invalid value for `accept_license`, must not be `None`")  # noqa: E501

        self._accept_license = accept_license

    @property
    def admin_password(self):
        """Gets the admin_password of this Splunk.  # noqa: E501

        Set a password for `admin` user.  # noqa: E501

        :return: The admin_password of this Splunk.  # noqa: E501
        :rtype: str
        """
        return self._admin_password

    @admin_password.setter
    def admin_password(self, admin_password):
        """Sets the admin_password of this Splunk.

        Set a password for `admin` user.  # noqa: E501

        :param admin_password: The admin_password of this Splunk.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and admin_password is None:  # noqa: E501
            raise ValueError("Invalid value for `admin_password`, must not be `None`")  # noqa: E501

        self._admin_password = admin_password

    @property
    def version(self):
        """Gets the version of this Splunk.  # noqa: E501

        Splunk version.  # noqa: E501

        :return: The version of this Splunk.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Splunk.

        Splunk version.  # noqa: E501

        :param version: The version of this Splunk.  # noqa: E501
        :type: str
        """

        self._version = version

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
        if not isinstance(other, Splunk):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Splunk):
            return True

        return self.to_dict() != other.to_dict()
