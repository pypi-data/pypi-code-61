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


class SharedSolidFillsDetails(object):
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
        'hex_value': 'str',
        'is_user_color': 'bool',
        'color_type_id': 'int',
        'fill_map_id': 'str',
        'parent_fill_map': 'SharedFillMapDetails',
        'color_transformations': 'SharedColorTransformationsDetails',
        'parent_line_id': 'str',
        'parent_line': 'SharedLinesDetails',
        'parent_text_id': 'str',
        'parent_text': 'SharedTextDetails',
        'parent_gradient_stop_id': 'str',
        'parent_gradient_stop': 'SharedGradientStopsDetails',
        'id': 'str',
        'date_created': 'datetime',
        'user_created': 'str',
        'date_modified': 'datetime',
        'user_modified': 'str'
    }

    attribute_map = {
        'hex_value': 'hexValue',
        'is_user_color': 'isUserColor',
        'color_type_id': 'colorTypeId',
        'fill_map_id': 'fillMapId',
        'parent_fill_map': 'parentFillMap',
        'color_transformations': 'colorTransformations',
        'parent_line_id': 'parentLineId',
        'parent_line': 'parentLine',
        'parent_text_id': 'parentTextId',
        'parent_text': 'parentText',
        'parent_gradient_stop_id': 'parentGradientStopId',
        'parent_gradient_stop': 'parentGradientStop',
        'id': 'id',
        'date_created': 'dateCreated',
        'user_created': 'userCreated',
        'date_modified': 'dateModified',
        'user_modified': 'userModified'
    }

    def __init__(self, hex_value=None, is_user_color=None, color_type_id=None, fill_map_id=None, parent_fill_map=None, color_transformations=None, parent_line_id=None, parent_line=None, parent_text_id=None, parent_text=None, parent_gradient_stop_id=None, parent_gradient_stop=None, id=None, date_created=None, user_created=None, date_modified=None, user_modified=None):  # noqa: E501
        """SharedSolidFillsDetails - a model defined in OpenAPI"""  # noqa: E501

        self._hex_value = None
        self._is_user_color = None
        self._color_type_id = None
        self._fill_map_id = None
        self._parent_fill_map = None
        self._color_transformations = None
        self._parent_line_id = None
        self._parent_line = None
        self._parent_text_id = None
        self._parent_text = None
        self._parent_gradient_stop_id = None
        self._parent_gradient_stop = None
        self._id = None
        self._date_created = None
        self._user_created = None
        self._date_modified = None
        self._user_modified = None
        self.discriminator = None

        self.hex_value = hex_value
        if is_user_color is not None:
            self.is_user_color = is_user_color
        self.color_type_id = color_type_id
        self.fill_map_id = fill_map_id
        if parent_fill_map is not None:
            self.parent_fill_map = parent_fill_map
        if color_transformations is not None:
            self.color_transformations = color_transformations
        self.parent_line_id = parent_line_id
        if parent_line is not None:
            self.parent_line = parent_line
        self.parent_text_id = parent_text_id
        if parent_text is not None:
            self.parent_text = parent_text
        self.parent_gradient_stop_id = parent_gradient_stop_id
        if parent_gradient_stop is not None:
            self.parent_gradient_stop = parent_gradient_stop
        if id is not None:
            self.id = id
        if date_created is not None:
            self.date_created = date_created
        if user_created is not None:
            self.user_created = user_created
        if date_modified is not None:
            self.date_modified = date_modified
        if user_modified is not None:
            self.user_modified = user_modified

    @property
    def hex_value(self):
        """Gets the hex_value of this SharedSolidFillsDetails.  # noqa: E501


        :return: The hex_value of this SharedSolidFillsDetails.  # noqa: E501
        :rtype: str
        """
        return self._hex_value

    @hex_value.setter
    def hex_value(self, hex_value):
        """Sets the hex_value of this SharedSolidFillsDetails.


        :param hex_value: The hex_value of this SharedSolidFillsDetails.  # noqa: E501
        :type: str
        """

        self._hex_value = hex_value

    @property
    def is_user_color(self):
        """Gets the is_user_color of this SharedSolidFillsDetails.  # noqa: E501


        :return: The is_user_color of this SharedSolidFillsDetails.  # noqa: E501
        :rtype: bool
        """
        return self._is_user_color

    @is_user_color.setter
    def is_user_color(self, is_user_color):
        """Sets the is_user_color of this SharedSolidFillsDetails.


        :param is_user_color: The is_user_color of this SharedSolidFillsDetails.  # noqa: E501
        :type: bool
        """

        self._is_user_color = is_user_color

    @property
    def color_type_id(self):
        """Gets the color_type_id of this SharedSolidFillsDetails.  # noqa: E501


        :return: The color_type_id of this SharedSolidFillsDetails.  # noqa: E501
        :rtype: int
        """
        return self._color_type_id

    @color_type_id.setter
    def color_type_id(self, color_type_id):
        """Sets the color_type_id of this SharedSolidFillsDetails.


        :param color_type_id: The color_type_id of this SharedSolidFillsDetails.  # noqa: E501
        :type: int
        """

        self._color_type_id = color_type_id

    @property
    def fill_map_id(self):
        """Gets the fill_map_id of this SharedSolidFillsDetails.  # noqa: E501


        :return: The fill_map_id of this SharedSolidFillsDetails.  # noqa: E501
        :rtype: str
        """
        return self._fill_map_id

    @fill_map_id.setter
    def fill_map_id(self, fill_map_id):
        """Sets the fill_map_id of this SharedSolidFillsDetails.


        :param fill_map_id: The fill_map_id of this SharedSolidFillsDetails.  # noqa: E501
        :type: str
        """

        self._fill_map_id = fill_map_id

    @property
    def parent_fill_map(self):
        """Gets the parent_fill_map of this SharedSolidFillsDetails.  # noqa: E501


        :return: The parent_fill_map of this SharedSolidFillsDetails.  # noqa: E501
        :rtype: SharedFillMapDetails
        """
        return self._parent_fill_map

    @parent_fill_map.setter
    def parent_fill_map(self, parent_fill_map):
        """Sets the parent_fill_map of this SharedSolidFillsDetails.


        :param parent_fill_map: The parent_fill_map of this SharedSolidFillsDetails.  # noqa: E501
        :type: SharedFillMapDetails
        """

        self._parent_fill_map = parent_fill_map

    @property
    def color_transformations(self):
        """Gets the color_transformations of this SharedSolidFillsDetails.  # noqa: E501


        :return: The color_transformations of this SharedSolidFillsDetails.  # noqa: E501
        :rtype: SharedColorTransformationsDetails
        """
        return self._color_transformations

    @color_transformations.setter
    def color_transformations(self, color_transformations):
        """Sets the color_transformations of this SharedSolidFillsDetails.


        :param color_transformations: The color_transformations of this SharedSolidFillsDetails.  # noqa: E501
        :type: SharedColorTransformationsDetails
        """

        self._color_transformations = color_transformations

    @property
    def parent_line_id(self):
        """Gets the parent_line_id of this SharedSolidFillsDetails.  # noqa: E501


        :return: The parent_line_id of this SharedSolidFillsDetails.  # noqa: E501
        :rtype: str
        """
        return self._parent_line_id

    @parent_line_id.setter
    def parent_line_id(self, parent_line_id):
        """Sets the parent_line_id of this SharedSolidFillsDetails.


        :param parent_line_id: The parent_line_id of this SharedSolidFillsDetails.  # noqa: E501
        :type: str
        """

        self._parent_line_id = parent_line_id

    @property
    def parent_line(self):
        """Gets the parent_line of this SharedSolidFillsDetails.  # noqa: E501


        :return: The parent_line of this SharedSolidFillsDetails.  # noqa: E501
        :rtype: SharedLinesDetails
        """
        return self._parent_line

    @parent_line.setter
    def parent_line(self, parent_line):
        """Sets the parent_line of this SharedSolidFillsDetails.


        :param parent_line: The parent_line of this SharedSolidFillsDetails.  # noqa: E501
        :type: SharedLinesDetails
        """

        self._parent_line = parent_line

    @property
    def parent_text_id(self):
        """Gets the parent_text_id of this SharedSolidFillsDetails.  # noqa: E501


        :return: The parent_text_id of this SharedSolidFillsDetails.  # noqa: E501
        :rtype: str
        """
        return self._parent_text_id

    @parent_text_id.setter
    def parent_text_id(self, parent_text_id):
        """Sets the parent_text_id of this SharedSolidFillsDetails.


        :param parent_text_id: The parent_text_id of this SharedSolidFillsDetails.  # noqa: E501
        :type: str
        """

        self._parent_text_id = parent_text_id

    @property
    def parent_text(self):
        """Gets the parent_text of this SharedSolidFillsDetails.  # noqa: E501


        :return: The parent_text of this SharedSolidFillsDetails.  # noqa: E501
        :rtype: SharedTextDetails
        """
        return self._parent_text

    @parent_text.setter
    def parent_text(self, parent_text):
        """Sets the parent_text of this SharedSolidFillsDetails.


        :param parent_text: The parent_text of this SharedSolidFillsDetails.  # noqa: E501
        :type: SharedTextDetails
        """

        self._parent_text = parent_text

    @property
    def parent_gradient_stop_id(self):
        """Gets the parent_gradient_stop_id of this SharedSolidFillsDetails.  # noqa: E501


        :return: The parent_gradient_stop_id of this SharedSolidFillsDetails.  # noqa: E501
        :rtype: str
        """
        return self._parent_gradient_stop_id

    @parent_gradient_stop_id.setter
    def parent_gradient_stop_id(self, parent_gradient_stop_id):
        """Sets the parent_gradient_stop_id of this SharedSolidFillsDetails.


        :param parent_gradient_stop_id: The parent_gradient_stop_id of this SharedSolidFillsDetails.  # noqa: E501
        :type: str
        """

        self._parent_gradient_stop_id = parent_gradient_stop_id

    @property
    def parent_gradient_stop(self):
        """Gets the parent_gradient_stop of this SharedSolidFillsDetails.  # noqa: E501


        :return: The parent_gradient_stop of this SharedSolidFillsDetails.  # noqa: E501
        :rtype: SharedGradientStopsDetails
        """
        return self._parent_gradient_stop

    @parent_gradient_stop.setter
    def parent_gradient_stop(self, parent_gradient_stop):
        """Sets the parent_gradient_stop of this SharedSolidFillsDetails.


        :param parent_gradient_stop: The parent_gradient_stop of this SharedSolidFillsDetails.  # noqa: E501
        :type: SharedGradientStopsDetails
        """

        self._parent_gradient_stop = parent_gradient_stop

    @property
    def id(self):
        """Gets the id of this SharedSolidFillsDetails.  # noqa: E501


        :return: The id of this SharedSolidFillsDetails.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SharedSolidFillsDetails.


        :param id: The id of this SharedSolidFillsDetails.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def date_created(self):
        """Gets the date_created of this SharedSolidFillsDetails.  # noqa: E501


        :return: The date_created of this SharedSolidFillsDetails.  # noqa: E501
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this SharedSolidFillsDetails.


        :param date_created: The date_created of this SharedSolidFillsDetails.  # noqa: E501
        :type: datetime
        """

        self._date_created = date_created

    @property
    def user_created(self):
        """Gets the user_created of this SharedSolidFillsDetails.  # noqa: E501


        :return: The user_created of this SharedSolidFillsDetails.  # noqa: E501
        :rtype: str
        """
        return self._user_created

    @user_created.setter
    def user_created(self, user_created):
        """Sets the user_created of this SharedSolidFillsDetails.


        :param user_created: The user_created of this SharedSolidFillsDetails.  # noqa: E501
        :type: str
        """

        self._user_created = user_created

    @property
    def date_modified(self):
        """Gets the date_modified of this SharedSolidFillsDetails.  # noqa: E501


        :return: The date_modified of this SharedSolidFillsDetails.  # noqa: E501
        :rtype: datetime
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this SharedSolidFillsDetails.


        :param date_modified: The date_modified of this SharedSolidFillsDetails.  # noqa: E501
        :type: datetime
        """

        self._date_modified = date_modified

    @property
    def user_modified(self):
        """Gets the user_modified of this SharedSolidFillsDetails.  # noqa: E501


        :return: The user_modified of this SharedSolidFillsDetails.  # noqa: E501
        :rtype: str
        """
        return self._user_modified

    @user_modified.setter
    def user_modified(self, user_modified):
        """Sets the user_modified of this SharedSolidFillsDetails.


        :param user_modified: The user_modified of this SharedSolidFillsDetails.  # noqa: E501
        :type: str
        """

        self._user_modified = user_modified

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
        if not isinstance(other, SharedSolidFillsDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
