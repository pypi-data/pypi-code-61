# coding: utf-8

"""
    OOXML Automation

    This API helps users convert Excel and Powerpoint documents into rich, live dashboards and stories.  # noqa: E501

    The version of the OpenAPI document: 0.1.0-no-tags
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class SharedColorTypes(object):
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
        'type_id': 'int',
        'name': 'str',
        'description': 'str',
        'color_scheme_index_value_enum': 'int',
        'id': 'str'
    }

    attribute_map = {
        'type_id': 'typeId',
        'name': 'name',
        'description': 'description',
        'color_scheme_index_value_enum': 'colorSchemeIndexValueEnum',
        'id': 'id'
    }

    def __init__(self, type_id=None, name=None, description=None, color_scheme_index_value_enum=None, id=None):  # noqa: E501
        """SharedColorTypes - a model defined in OpenAPI"""  # noqa: E501

        self._type_id = None
        self._name = None
        self._description = None
        self._color_scheme_index_value_enum = None
        self._id = None
        self.discriminator = None

        if type_id is not None:
            self.type_id = type_id
        self.name = name
        self.description = description
        self.color_scheme_index_value_enum = color_scheme_index_value_enum
        if id is not None:
            self.id = id

    @property
    def type_id(self):
        """Gets the type_id of this SharedColorTypes.  # noqa: E501


        :return: The type_id of this SharedColorTypes.  # noqa: E501
        :rtype: int
        """
        return self._type_id

    @type_id.setter
    def type_id(self, type_id):
        """Sets the type_id of this SharedColorTypes.


        :param type_id: The type_id of this SharedColorTypes.  # noqa: E501
        :type: int
        """

        self._type_id = type_id

    @property
    def name(self):
        """Gets the name of this SharedColorTypes.  # noqa: E501


        :return: The name of this SharedColorTypes.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SharedColorTypes.


        :param name: The name of this SharedColorTypes.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this SharedColorTypes.  # noqa: E501


        :return: The description of this SharedColorTypes.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SharedColorTypes.


        :param description: The description of this SharedColorTypes.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def color_scheme_index_value_enum(self):
        """Gets the color_scheme_index_value_enum of this SharedColorTypes.  # noqa: E501


        :return: The color_scheme_index_value_enum of this SharedColorTypes.  # noqa: E501
        :rtype: int
        """
        return self._color_scheme_index_value_enum

    @color_scheme_index_value_enum.setter
    def color_scheme_index_value_enum(self, color_scheme_index_value_enum):
        """Sets the color_scheme_index_value_enum of this SharedColorTypes.


        :param color_scheme_index_value_enum: The color_scheme_index_value_enum of this SharedColorTypes.  # noqa: E501
        :type: int
        """

        self._color_scheme_index_value_enum = color_scheme_index_value_enum

    @property
    def id(self):
        """Gets the id of this SharedColorTypes.  # noqa: E501


        :return: The id of this SharedColorTypes.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SharedColorTypes.


        :param id: The id of this SharedColorTypes.  # noqa: E501
        :type: str
        """

        self._id = id

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
        if not isinstance(other, SharedColorTypes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
