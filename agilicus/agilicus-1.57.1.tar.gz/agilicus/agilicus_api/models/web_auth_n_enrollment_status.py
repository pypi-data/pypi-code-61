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


class WebAuthNEnrollmentStatus(object):
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
        'challenge': 'str',
        'credential_id': 'str',
        'transports': 'list[str]'
    }

    attribute_map = {
        'challenge': 'challenge',
        'credential_id': 'credential_id',
        'transports': 'transports'
    }

    def __init__(self, challenge=None, credential_id=None, transports=None, local_vars_configuration=None):  # noqa: E501
        """WebAuthNEnrollmentStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._challenge = None
        self._credential_id = None
        self._transports = None
        self.discriminator = None

        if challenge is not None:
            self.challenge = challenge
        if credential_id is not None:
            self.credential_id = credential_id
        if transports is not None:
            self.transports = transports

    @property
    def challenge(self):
        """Gets the challenge of this WebAuthNEnrollmentStatus.  # noqa: E501

        An opaque string used to challenge a user attempting to login using WebAuthN. The second factor device will return a signed version of this challenge to indicate that the user should be allowed to proceed.   # noqa: E501

        :return: The challenge of this WebAuthNEnrollmentStatus.  # noqa: E501
        :rtype: str
        """
        return self._challenge

    @challenge.setter
    def challenge(self, challenge):
        """Sets the challenge of this WebAuthNEnrollmentStatus.

        An opaque string used to challenge a user attempting to login using WebAuthN. The second factor device will return a signed version of this challenge to indicate that the user should be allowed to proceed.   # noqa: E501

        :param challenge: The challenge of this WebAuthNEnrollmentStatus.  # noqa: E501
        :type: str
        """

        self._challenge = challenge

    @property
    def credential_id(self):
        """Gets the credential_id of this WebAuthNEnrollmentStatus.  # noqa: E501

        A probabilistically-unique byte sequence identifying a public key credential source and its authentication assertions.  See https://www.w3.org/TR/webauthn/#credential-id for more details   # noqa: E501

        :return: The credential_id of this WebAuthNEnrollmentStatus.  # noqa: E501
        :rtype: str
        """
        return self._credential_id

    @credential_id.setter
    def credential_id(self, credential_id):
        """Sets the credential_id of this WebAuthNEnrollmentStatus.

        A probabilistically-unique byte sequence identifying a public key credential source and its authentication assertions.  See https://www.w3.org/TR/webauthn/#credential-id for more details   # noqa: E501

        :param credential_id: The credential_id of this WebAuthNEnrollmentStatus.  # noqa: E501
        :type: str
        """

        self._credential_id = credential_id

    @property
    def transports(self):
        """Gets the transports of this WebAuthNEnrollmentStatus.  # noqa: E501

        List of supported transports for this enrolled credential  # noqa: E501

        :return: The transports of this WebAuthNEnrollmentStatus.  # noqa: E501
        :rtype: list[str]
        """
        return self._transports

    @transports.setter
    def transports(self, transports):
        """Sets the transports of this WebAuthNEnrollmentStatus.

        List of supported transports for this enrolled credential  # noqa: E501

        :param transports: The transports of this WebAuthNEnrollmentStatus.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["internal", "ble", "nfc", "usb"]  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                not set(transports).issubset(set(allowed_values))):  # noqa: E501
            raise ValueError(
                "Invalid values for `transports` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(transports) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._transports = transports

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
        if not isinstance(other, WebAuthNEnrollmentStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WebAuthNEnrollmentStatus):
            return True

        return self.to_dict() != other.to_dict()
