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


class SharedFillMapDetails(object):
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
        'fill_type_id': 'int',
        'solid_fill': 'SharedSolidFillsDetails',
        'gradient_fill': 'SharedGradientFillsDetails',
        'image_fill': 'SharedImageFillsDetails',
        'shape': 'SlideShapesDetails',
        'shape_id': 'str',
        'connector': 'SlideConnectorDetails',
        'connector_id': 'str',
        'effect_attribute_id': 'str',
        'effect_attribute': 'SharedEffectAttributesDetails',
        'table_cell_id': 'str',
        'table_cell': 'TableCellsDetails',
        'theme_background_fill_id': 'str',
        'theme_background_fill': 'ThemeBackgroundFillsDetails',
        'theme_fill_id': 'str',
        'theme_fill': 'ThemeFillsDetails',
        'id': 'str',
        'date_created': 'datetime',
        'user_created': 'str',
        'date_modified': 'datetime',
        'user_modified': 'str'
    }

    attribute_map = {
        'fill_type_id': 'fillTypeId',
        'solid_fill': 'solidFill',
        'gradient_fill': 'gradientFill',
        'image_fill': 'imageFill',
        'shape': 'shape',
        'shape_id': 'shapeId',
        'connector': 'connector',
        'connector_id': 'connectorId',
        'effect_attribute_id': 'effectAttributeId',
        'effect_attribute': 'effectAttribute',
        'table_cell_id': 'tableCellId',
        'table_cell': 'tableCell',
        'theme_background_fill_id': 'themeBackgroundFillId',
        'theme_background_fill': 'themeBackgroundFill',
        'theme_fill_id': 'themeFillId',
        'theme_fill': 'themeFill',
        'id': 'id',
        'date_created': 'dateCreated',
        'user_created': 'userCreated',
        'date_modified': 'dateModified',
        'user_modified': 'userModified'
    }

    def __init__(self, fill_type_id=None, solid_fill=None, gradient_fill=None, image_fill=None, shape=None, shape_id=None, connector=None, connector_id=None, effect_attribute_id=None, effect_attribute=None, table_cell_id=None, table_cell=None, theme_background_fill_id=None, theme_background_fill=None, theme_fill_id=None, theme_fill=None, id=None, date_created=None, user_created=None, date_modified=None, user_modified=None):  # noqa: E501
        """SharedFillMapDetails - a model defined in OpenAPI"""  # noqa: E501

        self._fill_type_id = None
        self._solid_fill = None
        self._gradient_fill = None
        self._image_fill = None
        self._shape = None
        self._shape_id = None
        self._connector = None
        self._connector_id = None
        self._effect_attribute_id = None
        self._effect_attribute = None
        self._table_cell_id = None
        self._table_cell = None
        self._theme_background_fill_id = None
        self._theme_background_fill = None
        self._theme_fill_id = None
        self._theme_fill = None
        self._id = None
        self._date_created = None
        self._user_created = None
        self._date_modified = None
        self._user_modified = None
        self.discriminator = None

        if fill_type_id is not None:
            self.fill_type_id = fill_type_id
        if solid_fill is not None:
            self.solid_fill = solid_fill
        if gradient_fill is not None:
            self.gradient_fill = gradient_fill
        if image_fill is not None:
            self.image_fill = image_fill
        if shape is not None:
            self.shape = shape
        self.shape_id = shape_id
        if connector is not None:
            self.connector = connector
        self.connector_id = connector_id
        self.effect_attribute_id = effect_attribute_id
        if effect_attribute is not None:
            self.effect_attribute = effect_attribute
        self.table_cell_id = table_cell_id
        if table_cell is not None:
            self.table_cell = table_cell
        self.theme_background_fill_id = theme_background_fill_id
        if theme_background_fill is not None:
            self.theme_background_fill = theme_background_fill
        self.theme_fill_id = theme_fill_id
        if theme_fill is not None:
            self.theme_fill = theme_fill
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
    def fill_type_id(self):
        """Gets the fill_type_id of this SharedFillMapDetails.  # noqa: E501


        :return: The fill_type_id of this SharedFillMapDetails.  # noqa: E501
        :rtype: int
        """
        return self._fill_type_id

    @fill_type_id.setter
    def fill_type_id(self, fill_type_id):
        """Sets the fill_type_id of this SharedFillMapDetails.


        :param fill_type_id: The fill_type_id of this SharedFillMapDetails.  # noqa: E501
        :type: int
        """

        self._fill_type_id = fill_type_id

    @property
    def solid_fill(self):
        """Gets the solid_fill of this SharedFillMapDetails.  # noqa: E501


        :return: The solid_fill of this SharedFillMapDetails.  # noqa: E501
        :rtype: SharedSolidFillsDetails
        """
        return self._solid_fill

    @solid_fill.setter
    def solid_fill(self, solid_fill):
        """Sets the solid_fill of this SharedFillMapDetails.


        :param solid_fill: The solid_fill of this SharedFillMapDetails.  # noqa: E501
        :type: SharedSolidFillsDetails
        """

        self._solid_fill = solid_fill

    @property
    def gradient_fill(self):
        """Gets the gradient_fill of this SharedFillMapDetails.  # noqa: E501


        :return: The gradient_fill of this SharedFillMapDetails.  # noqa: E501
        :rtype: SharedGradientFillsDetails
        """
        return self._gradient_fill

    @gradient_fill.setter
    def gradient_fill(self, gradient_fill):
        """Sets the gradient_fill of this SharedFillMapDetails.


        :param gradient_fill: The gradient_fill of this SharedFillMapDetails.  # noqa: E501
        :type: SharedGradientFillsDetails
        """

        self._gradient_fill = gradient_fill

    @property
    def image_fill(self):
        """Gets the image_fill of this SharedFillMapDetails.  # noqa: E501


        :return: The image_fill of this SharedFillMapDetails.  # noqa: E501
        :rtype: SharedImageFillsDetails
        """
        return self._image_fill

    @image_fill.setter
    def image_fill(self, image_fill):
        """Sets the image_fill of this SharedFillMapDetails.


        :param image_fill: The image_fill of this SharedFillMapDetails.  # noqa: E501
        :type: SharedImageFillsDetails
        """

        self._image_fill = image_fill

    @property
    def shape(self):
        """Gets the shape of this SharedFillMapDetails.  # noqa: E501


        :return: The shape of this SharedFillMapDetails.  # noqa: E501
        :rtype: SlideShapesDetails
        """
        return self._shape

    @shape.setter
    def shape(self, shape):
        """Sets the shape of this SharedFillMapDetails.


        :param shape: The shape of this SharedFillMapDetails.  # noqa: E501
        :type: SlideShapesDetails
        """

        self._shape = shape

    @property
    def shape_id(self):
        """Gets the shape_id of this SharedFillMapDetails.  # noqa: E501


        :return: The shape_id of this SharedFillMapDetails.  # noqa: E501
        :rtype: str
        """
        return self._shape_id

    @shape_id.setter
    def shape_id(self, shape_id):
        """Sets the shape_id of this SharedFillMapDetails.


        :param shape_id: The shape_id of this SharedFillMapDetails.  # noqa: E501
        :type: str
        """

        self._shape_id = shape_id

    @property
    def connector(self):
        """Gets the connector of this SharedFillMapDetails.  # noqa: E501


        :return: The connector of this SharedFillMapDetails.  # noqa: E501
        :rtype: SlideConnectorDetails
        """
        return self._connector

    @connector.setter
    def connector(self, connector):
        """Sets the connector of this SharedFillMapDetails.


        :param connector: The connector of this SharedFillMapDetails.  # noqa: E501
        :type: SlideConnectorDetails
        """

        self._connector = connector

    @property
    def connector_id(self):
        """Gets the connector_id of this SharedFillMapDetails.  # noqa: E501


        :return: The connector_id of this SharedFillMapDetails.  # noqa: E501
        :rtype: str
        """
        return self._connector_id

    @connector_id.setter
    def connector_id(self, connector_id):
        """Sets the connector_id of this SharedFillMapDetails.


        :param connector_id: The connector_id of this SharedFillMapDetails.  # noqa: E501
        :type: str
        """

        self._connector_id = connector_id

    @property
    def effect_attribute_id(self):
        """Gets the effect_attribute_id of this SharedFillMapDetails.  # noqa: E501


        :return: The effect_attribute_id of this SharedFillMapDetails.  # noqa: E501
        :rtype: str
        """
        return self._effect_attribute_id

    @effect_attribute_id.setter
    def effect_attribute_id(self, effect_attribute_id):
        """Sets the effect_attribute_id of this SharedFillMapDetails.


        :param effect_attribute_id: The effect_attribute_id of this SharedFillMapDetails.  # noqa: E501
        :type: str
        """

        self._effect_attribute_id = effect_attribute_id

    @property
    def effect_attribute(self):
        """Gets the effect_attribute of this SharedFillMapDetails.  # noqa: E501


        :return: The effect_attribute of this SharedFillMapDetails.  # noqa: E501
        :rtype: SharedEffectAttributesDetails
        """
        return self._effect_attribute

    @effect_attribute.setter
    def effect_attribute(self, effect_attribute):
        """Sets the effect_attribute of this SharedFillMapDetails.


        :param effect_attribute: The effect_attribute of this SharedFillMapDetails.  # noqa: E501
        :type: SharedEffectAttributesDetails
        """

        self._effect_attribute = effect_attribute

    @property
    def table_cell_id(self):
        """Gets the table_cell_id of this SharedFillMapDetails.  # noqa: E501


        :return: The table_cell_id of this SharedFillMapDetails.  # noqa: E501
        :rtype: str
        """
        return self._table_cell_id

    @table_cell_id.setter
    def table_cell_id(self, table_cell_id):
        """Sets the table_cell_id of this SharedFillMapDetails.


        :param table_cell_id: The table_cell_id of this SharedFillMapDetails.  # noqa: E501
        :type: str
        """

        self._table_cell_id = table_cell_id

    @property
    def table_cell(self):
        """Gets the table_cell of this SharedFillMapDetails.  # noqa: E501


        :return: The table_cell of this SharedFillMapDetails.  # noqa: E501
        :rtype: TableCellsDetails
        """
        return self._table_cell

    @table_cell.setter
    def table_cell(self, table_cell):
        """Sets the table_cell of this SharedFillMapDetails.


        :param table_cell: The table_cell of this SharedFillMapDetails.  # noqa: E501
        :type: TableCellsDetails
        """

        self._table_cell = table_cell

    @property
    def theme_background_fill_id(self):
        """Gets the theme_background_fill_id of this SharedFillMapDetails.  # noqa: E501


        :return: The theme_background_fill_id of this SharedFillMapDetails.  # noqa: E501
        :rtype: str
        """
        return self._theme_background_fill_id

    @theme_background_fill_id.setter
    def theme_background_fill_id(self, theme_background_fill_id):
        """Sets the theme_background_fill_id of this SharedFillMapDetails.


        :param theme_background_fill_id: The theme_background_fill_id of this SharedFillMapDetails.  # noqa: E501
        :type: str
        """

        self._theme_background_fill_id = theme_background_fill_id

    @property
    def theme_background_fill(self):
        """Gets the theme_background_fill of this SharedFillMapDetails.  # noqa: E501


        :return: The theme_background_fill of this SharedFillMapDetails.  # noqa: E501
        :rtype: ThemeBackgroundFillsDetails
        """
        return self._theme_background_fill

    @theme_background_fill.setter
    def theme_background_fill(self, theme_background_fill):
        """Sets the theme_background_fill of this SharedFillMapDetails.


        :param theme_background_fill: The theme_background_fill of this SharedFillMapDetails.  # noqa: E501
        :type: ThemeBackgroundFillsDetails
        """

        self._theme_background_fill = theme_background_fill

    @property
    def theme_fill_id(self):
        """Gets the theme_fill_id of this SharedFillMapDetails.  # noqa: E501


        :return: The theme_fill_id of this SharedFillMapDetails.  # noqa: E501
        :rtype: str
        """
        return self._theme_fill_id

    @theme_fill_id.setter
    def theme_fill_id(self, theme_fill_id):
        """Sets the theme_fill_id of this SharedFillMapDetails.


        :param theme_fill_id: The theme_fill_id of this SharedFillMapDetails.  # noqa: E501
        :type: str
        """

        self._theme_fill_id = theme_fill_id

    @property
    def theme_fill(self):
        """Gets the theme_fill of this SharedFillMapDetails.  # noqa: E501


        :return: The theme_fill of this SharedFillMapDetails.  # noqa: E501
        :rtype: ThemeFillsDetails
        """
        return self._theme_fill

    @theme_fill.setter
    def theme_fill(self, theme_fill):
        """Sets the theme_fill of this SharedFillMapDetails.


        :param theme_fill: The theme_fill of this SharedFillMapDetails.  # noqa: E501
        :type: ThemeFillsDetails
        """

        self._theme_fill = theme_fill

    @property
    def id(self):
        """Gets the id of this SharedFillMapDetails.  # noqa: E501


        :return: The id of this SharedFillMapDetails.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SharedFillMapDetails.


        :param id: The id of this SharedFillMapDetails.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def date_created(self):
        """Gets the date_created of this SharedFillMapDetails.  # noqa: E501


        :return: The date_created of this SharedFillMapDetails.  # noqa: E501
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this SharedFillMapDetails.


        :param date_created: The date_created of this SharedFillMapDetails.  # noqa: E501
        :type: datetime
        """

        self._date_created = date_created

    @property
    def user_created(self):
        """Gets the user_created of this SharedFillMapDetails.  # noqa: E501


        :return: The user_created of this SharedFillMapDetails.  # noqa: E501
        :rtype: str
        """
        return self._user_created

    @user_created.setter
    def user_created(self, user_created):
        """Sets the user_created of this SharedFillMapDetails.


        :param user_created: The user_created of this SharedFillMapDetails.  # noqa: E501
        :type: str
        """

        self._user_created = user_created

    @property
    def date_modified(self):
        """Gets the date_modified of this SharedFillMapDetails.  # noqa: E501


        :return: The date_modified of this SharedFillMapDetails.  # noqa: E501
        :rtype: datetime
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this SharedFillMapDetails.


        :param date_modified: The date_modified of this SharedFillMapDetails.  # noqa: E501
        :type: datetime
        """

        self._date_modified = date_modified

    @property
    def user_modified(self):
        """Gets the user_modified of this SharedFillMapDetails.  # noqa: E501


        :return: The user_modified of this SharedFillMapDetails.  # noqa: E501
        :rtype: str
        """
        return self._user_modified

    @user_modified.setter
    def user_modified(self, user_modified):
        """Sets the user_modified of this SharedFillMapDetails.


        :param user_modified: The user_modified of this SharedFillMapDetails.  # noqa: E501
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
        if not isinstance(other, SharedFillMapDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
