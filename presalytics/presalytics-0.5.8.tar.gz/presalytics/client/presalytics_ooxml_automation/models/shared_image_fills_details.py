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


class SharedImageFillsDetails(object):
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
        'fill_map_id': 'str',
        'fill_map': 'SharedFillMapDetails',
        'picture': 'SharedPicturesDetails',
        'compression_state': 'str',
        'stretch': 'bool',
        'tile': 'str',
        'rotate_with_shape': 'bool',
        'source_rectangle': 'str',
        'dpi': 'int',
        'effects_json': 'str',
        'id': 'str',
        'date_created': 'datetime',
        'user_created': 'str',
        'date_modified': 'datetime',
        'user_modified': 'str'
    }

    attribute_map = {
        'fill_map_id': 'fillMapId',
        'fill_map': 'fillMap',
        'picture': 'picture',
        'compression_state': 'compressionState',
        'stretch': 'stretch',
        'tile': 'tile',
        'rotate_with_shape': 'rotateWithShape',
        'source_rectangle': 'sourceRectangle',
        'dpi': 'dpi',
        'effects_json': 'effectsJson',
        'id': 'id',
        'date_created': 'dateCreated',
        'user_created': 'userCreated',
        'date_modified': 'dateModified',
        'user_modified': 'userModified'
    }

    def __init__(self, fill_map_id=None, fill_map=None, picture=None, compression_state=None, stretch=None, tile=None, rotate_with_shape=None, source_rectangle=None, dpi=None, effects_json=None, id=None, date_created=None, user_created=None, date_modified=None, user_modified=None):  # noqa: E501
        """SharedImageFillsDetails - a model defined in OpenAPI"""  # noqa: E501

        self._fill_map_id = None
        self._fill_map = None
        self._picture = None
        self._compression_state = None
        self._stretch = None
        self._tile = None
        self._rotate_with_shape = None
        self._source_rectangle = None
        self._dpi = None
        self._effects_json = None
        self._id = None
        self._date_created = None
        self._user_created = None
        self._date_modified = None
        self._user_modified = None
        self.discriminator = None

        self.fill_map_id = fill_map_id
        if fill_map is not None:
            self.fill_map = fill_map
        if picture is not None:
            self.picture = picture
        self.compression_state = compression_state
        if stretch is not None:
            self.stretch = stretch
        self.tile = tile
        if rotate_with_shape is not None:
            self.rotate_with_shape = rotate_with_shape
        self.source_rectangle = source_rectangle
        self.dpi = dpi
        self.effects_json = effects_json
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
    def fill_map_id(self):
        """Gets the fill_map_id of this SharedImageFillsDetails.  # noqa: E501


        :return: The fill_map_id of this SharedImageFillsDetails.  # noqa: E501
        :rtype: str
        """
        return self._fill_map_id

    @fill_map_id.setter
    def fill_map_id(self, fill_map_id):
        """Sets the fill_map_id of this SharedImageFillsDetails.


        :param fill_map_id: The fill_map_id of this SharedImageFillsDetails.  # noqa: E501
        :type: str
        """

        self._fill_map_id = fill_map_id

    @property
    def fill_map(self):
        """Gets the fill_map of this SharedImageFillsDetails.  # noqa: E501


        :return: The fill_map of this SharedImageFillsDetails.  # noqa: E501
        :rtype: SharedFillMapDetails
        """
        return self._fill_map

    @fill_map.setter
    def fill_map(self, fill_map):
        """Sets the fill_map of this SharedImageFillsDetails.


        :param fill_map: The fill_map of this SharedImageFillsDetails.  # noqa: E501
        :type: SharedFillMapDetails
        """

        self._fill_map = fill_map

    @property
    def picture(self):
        """Gets the picture of this SharedImageFillsDetails.  # noqa: E501


        :return: The picture of this SharedImageFillsDetails.  # noqa: E501
        :rtype: SharedPicturesDetails
        """
        return self._picture

    @picture.setter
    def picture(self, picture):
        """Sets the picture of this SharedImageFillsDetails.


        :param picture: The picture of this SharedImageFillsDetails.  # noqa: E501
        :type: SharedPicturesDetails
        """

        self._picture = picture

    @property
    def compression_state(self):
        """Gets the compression_state of this SharedImageFillsDetails.  # noqa: E501


        :return: The compression_state of this SharedImageFillsDetails.  # noqa: E501
        :rtype: str
        """
        return self._compression_state

    @compression_state.setter
    def compression_state(self, compression_state):
        """Sets the compression_state of this SharedImageFillsDetails.


        :param compression_state: The compression_state of this SharedImageFillsDetails.  # noqa: E501
        :type: str
        """

        self._compression_state = compression_state

    @property
    def stretch(self):
        """Gets the stretch of this SharedImageFillsDetails.  # noqa: E501


        :return: The stretch of this SharedImageFillsDetails.  # noqa: E501
        :rtype: bool
        """
        return self._stretch

    @stretch.setter
    def stretch(self, stretch):
        """Sets the stretch of this SharedImageFillsDetails.


        :param stretch: The stretch of this SharedImageFillsDetails.  # noqa: E501
        :type: bool
        """

        self._stretch = stretch

    @property
    def tile(self):
        """Gets the tile of this SharedImageFillsDetails.  # noqa: E501


        :return: The tile of this SharedImageFillsDetails.  # noqa: E501
        :rtype: str
        """
        return self._tile

    @tile.setter
    def tile(self, tile):
        """Sets the tile of this SharedImageFillsDetails.


        :param tile: The tile of this SharedImageFillsDetails.  # noqa: E501
        :type: str
        """

        self._tile = tile

    @property
    def rotate_with_shape(self):
        """Gets the rotate_with_shape of this SharedImageFillsDetails.  # noqa: E501


        :return: The rotate_with_shape of this SharedImageFillsDetails.  # noqa: E501
        :rtype: bool
        """
        return self._rotate_with_shape

    @rotate_with_shape.setter
    def rotate_with_shape(self, rotate_with_shape):
        """Sets the rotate_with_shape of this SharedImageFillsDetails.


        :param rotate_with_shape: The rotate_with_shape of this SharedImageFillsDetails.  # noqa: E501
        :type: bool
        """

        self._rotate_with_shape = rotate_with_shape

    @property
    def source_rectangle(self):
        """Gets the source_rectangle of this SharedImageFillsDetails.  # noqa: E501


        :return: The source_rectangle of this SharedImageFillsDetails.  # noqa: E501
        :rtype: str
        """
        return self._source_rectangle

    @source_rectangle.setter
    def source_rectangle(self, source_rectangle):
        """Sets the source_rectangle of this SharedImageFillsDetails.


        :param source_rectangle: The source_rectangle of this SharedImageFillsDetails.  # noqa: E501
        :type: str
        """

        self._source_rectangle = source_rectangle

    @property
    def dpi(self):
        """Gets the dpi of this SharedImageFillsDetails.  # noqa: E501


        :return: The dpi of this SharedImageFillsDetails.  # noqa: E501
        :rtype: int
        """
        return self._dpi

    @dpi.setter
    def dpi(self, dpi):
        """Sets the dpi of this SharedImageFillsDetails.


        :param dpi: The dpi of this SharedImageFillsDetails.  # noqa: E501
        :type: int
        """

        self._dpi = dpi

    @property
    def effects_json(self):
        """Gets the effects_json of this SharedImageFillsDetails.  # noqa: E501


        :return: The effects_json of this SharedImageFillsDetails.  # noqa: E501
        :rtype: str
        """
        return self._effects_json

    @effects_json.setter
    def effects_json(self, effects_json):
        """Sets the effects_json of this SharedImageFillsDetails.


        :param effects_json: The effects_json of this SharedImageFillsDetails.  # noqa: E501
        :type: str
        """

        self._effects_json = effects_json

    @property
    def id(self):
        """Gets the id of this SharedImageFillsDetails.  # noqa: E501


        :return: The id of this SharedImageFillsDetails.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SharedImageFillsDetails.


        :param id: The id of this SharedImageFillsDetails.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def date_created(self):
        """Gets the date_created of this SharedImageFillsDetails.  # noqa: E501


        :return: The date_created of this SharedImageFillsDetails.  # noqa: E501
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this SharedImageFillsDetails.


        :param date_created: The date_created of this SharedImageFillsDetails.  # noqa: E501
        :type: datetime
        """

        self._date_created = date_created

    @property
    def user_created(self):
        """Gets the user_created of this SharedImageFillsDetails.  # noqa: E501


        :return: The user_created of this SharedImageFillsDetails.  # noqa: E501
        :rtype: str
        """
        return self._user_created

    @user_created.setter
    def user_created(self, user_created):
        """Sets the user_created of this SharedImageFillsDetails.


        :param user_created: The user_created of this SharedImageFillsDetails.  # noqa: E501
        :type: str
        """

        self._user_created = user_created

    @property
    def date_modified(self):
        """Gets the date_modified of this SharedImageFillsDetails.  # noqa: E501


        :return: The date_modified of this SharedImageFillsDetails.  # noqa: E501
        :rtype: datetime
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this SharedImageFillsDetails.


        :param date_modified: The date_modified of this SharedImageFillsDetails.  # noqa: E501
        :type: datetime
        """

        self._date_modified = date_modified

    @property
    def user_modified(self):
        """Gets the user_modified of this SharedImageFillsDetails.  # noqa: E501


        :return: The user_modified of this SharedImageFillsDetails.  # noqa: E501
        :rtype: str
        """
        return self._user_modified

    @user_modified.setter
    def user_modified(self, user_modified):
        """Sets the user_modified of this SharedImageFillsDetails.


        :param user_modified: The user_modified of this SharedImageFillsDetails.  # noqa: E501
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
        if not isinstance(other, SharedImageFillsDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
