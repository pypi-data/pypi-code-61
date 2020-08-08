# coding: utf-8

"""
    convertapi

    Convert API lets you effortlessly convert file formats and types.  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class FindRegexMatch(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'character_offset_start': 'int',
        'character_offset_end': 'int',
        'containing_line': 'str',
        'match_value': 'str',
        'match_groups': 'list[str]'
    }

    attribute_map = {
        'character_offset_start': 'CharacterOffsetStart',
        'character_offset_end': 'CharacterOffsetEnd',
        'containing_line': 'ContainingLine',
        'match_value': 'MatchValue',
        'match_groups': 'MatchGroups'
    }

    def __init__(self, character_offset_start=None, character_offset_end=None, containing_line=None, match_value=None, match_groups=None):  # noqa: E501
        """FindRegexMatch - a model defined in Swagger"""  # noqa: E501

        self._character_offset_start = None
        self._character_offset_end = None
        self._containing_line = None
        self._match_value = None
        self._match_groups = None
        self.discriminator = None

        if character_offset_start is not None:
            self.character_offset_start = character_offset_start
        if character_offset_end is not None:
            self.character_offset_end = character_offset_end
        if containing_line is not None:
            self.containing_line = containing_line
        if match_value is not None:
            self.match_value = match_value
        if match_groups is not None:
            self.match_groups = match_groups

    @property
    def character_offset_start(self):
        """Gets the character_offset_start of this FindRegexMatch.  # noqa: E501

        0-based index of the start of the match  # noqa: E501

        :return: The character_offset_start of this FindRegexMatch.  # noqa: E501
        :rtype: int
        """
        return self._character_offset_start

    @character_offset_start.setter
    def character_offset_start(self, character_offset_start):
        """Sets the character_offset_start of this FindRegexMatch.

        0-based index of the start of the match  # noqa: E501

        :param character_offset_start: The character_offset_start of this FindRegexMatch.  # noqa: E501
        :type: int
        """

        self._character_offset_start = character_offset_start

    @property
    def character_offset_end(self):
        """Gets the character_offset_end of this FindRegexMatch.  # noqa: E501

        0-based index of the end of the match  # noqa: E501

        :return: The character_offset_end of this FindRegexMatch.  # noqa: E501
        :rtype: int
        """
        return self._character_offset_end

    @character_offset_end.setter
    def character_offset_end(self, character_offset_end):
        """Sets the character_offset_end of this FindRegexMatch.

        0-based index of the end of the match  # noqa: E501

        :param character_offset_end: The character_offset_end of this FindRegexMatch.  # noqa: E501
        :type: int
        """

        self._character_offset_end = character_offset_end

    @property
    def containing_line(self):
        """Gets the containing_line of this FindRegexMatch.  # noqa: E501

        Text content of the line containing the match  # noqa: E501

        :return: The containing_line of this FindRegexMatch.  # noqa: E501
        :rtype: str
        """
        return self._containing_line

    @containing_line.setter
    def containing_line(self, containing_line):
        """Sets the containing_line of this FindRegexMatch.

        Text content of the line containing the match  # noqa: E501

        :param containing_line: The containing_line of this FindRegexMatch.  # noqa: E501
        :type: str
        """

        self._containing_line = containing_line

    @property
    def match_value(self):
        """Gets the match_value of this FindRegexMatch.  # noqa: E501

        The match value  # noqa: E501

        :return: The match_value of this FindRegexMatch.  # noqa: E501
        :rtype: str
        """
        return self._match_value

    @match_value.setter
    def match_value(self, match_value):
        """Sets the match_value of this FindRegexMatch.

        The match value  # noqa: E501

        :param match_value: The match_value of this FindRegexMatch.  # noqa: E501
        :type: str
        """

        self._match_value = match_value

    @property
    def match_groups(self):
        """Gets the match_groups of this FindRegexMatch.  # noqa: E501

        Regular expression regex match groups; these correspond to the match values  # noqa: E501

        :return: The match_groups of this FindRegexMatch.  # noqa: E501
        :rtype: list[str]
        """
        return self._match_groups

    @match_groups.setter
    def match_groups(self, match_groups):
        """Sets the match_groups of this FindRegexMatch.

        Regular expression regex match groups; these correspond to the match values  # noqa: E501

        :param match_groups: The match_groups of this FindRegexMatch.  # noqa: E501
        :type: list[str]
        """

        self._match_groups = match_groups

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(FindRegexMatch, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, FindRegexMatch):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
