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


class ChallengeStatus(object):
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
        'state': 'str',
        'public_challenge': 'str'
    }

    attribute_map = {
        'state': 'state',
        'public_challenge': 'public_challenge'
    }

    def __init__(self, state=None, public_challenge=None, local_vars_configuration=None):  # noqa: E501
        """ChallengeStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._state = None
        self._public_challenge = None
        self.discriminator = None

        if state is not None:
            self.state = state
        if public_challenge is not None:
            self.public_challenge = public_challenge

    @property
    def state(self):
        """Gets the state of this ChallengeStatus.  # noqa: E501

        The current state of the challenge. The challenge may be in the following states:   - pending: waiting to issue the challenge.   - challenge_failed: the system failed to issue the challenge. This could be because there is     no mechanism to do so, communication with the device failed, and so on.   - issued: the challenge has been issued. The system is waiting for a response.   - challenge_passed: the user passed the challenge, typically by accepting a notification.   - challenge_declined: the user declined to accept the challenge. The challenge is no longer valid.   - timed_out: the challenge has timed out. The user can no longer use an answer to it to prove their     possession of a second factor.   # noqa: E501

        :return: The state of this ChallengeStatus.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ChallengeStatus.

        The current state of the challenge. The challenge may be in the following states:   - pending: waiting to issue the challenge.   - challenge_failed: the system failed to issue the challenge. This could be because there is     no mechanism to do so, communication with the device failed, and so on.   - issued: the challenge has been issued. The system is waiting for a response.   - challenge_passed: the user passed the challenge, typically by accepting a notification.   - challenge_declined: the user declined to accept the challenge. The challenge is no longer valid.   - timed_out: the challenge has timed out. The user can no longer use an answer to it to prove their     possession of a second factor.   # noqa: E501

        :param state: The state of this ChallengeStatus.  # noqa: E501
        :type: str
        """
        allowed_values = ["pending", "issued", "challenge_failed", "challenge_passed", "challenge_declined", "timed_out"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and state not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def public_challenge(self):
        """Gets the public_challenge of this ChallengeStatus.  # noqa: E501

        An opaque string used as the public challenge. Currently this is only used when the challenge type is webauthn.  # noqa: E501

        :return: The public_challenge of this ChallengeStatus.  # noqa: E501
        :rtype: str
        """
        return self._public_challenge

    @public_challenge.setter
    def public_challenge(self, public_challenge):
        """Sets the public_challenge of this ChallengeStatus.

        An opaque string used as the public challenge. Currently this is only used when the challenge type is webauthn.  # noqa: E501

        :param public_challenge: The public_challenge of this ChallengeStatus.  # noqa: E501
        :type: str
        """

        self._public_challenge = public_challenge

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
        if not isinstance(other, ChallengeStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ChallengeStatus):
            return True

        return self.to_dict() != other.to_dict()
