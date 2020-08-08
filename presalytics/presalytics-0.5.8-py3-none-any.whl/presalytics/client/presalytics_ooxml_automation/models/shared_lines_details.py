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


class SharedLinesDetails(object):
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
        'line_color_solid_fill': 'SharedSolidFillsDetails',
        'connector_id': 'str',
        'parent_connector': 'SlideConnectorDetails',
        'shape_id': 'str',
        'parent_shape': 'SlideShapesDetails',
        'dash_type_id': 'int',
        'head_end_type_id': 'int',
        'tail_end_type_id': 'int',
        'weight': 'int',
        'head_end_height_id': 'int',
        'head_end_width_id': 'int',
        'tail_end_height_id': 'int',
        'tail_end_width_id': 'int',
        'top_border_id': 'str',
        'top_border': 'TableBordersDetails',
        'bottom_border_id': 'str',
        'bottom_border': 'TableBordersDetails',
        'right_border_id': 'str',
        'right_border': 'TableBordersDetails',
        'left_border_id': 'str',
        'left_border': 'TableBordersDetails',
        't_lto_br_border_id': 'str',
        't_lto_br_border': 'TableBordersDetails',
        'b_lto_tr_border_id': 'str',
        'b_lto_tr_border': 'TableBordersDetails',
        'line_map_id': 'str',
        'line_map': 'ThemeLineMapDetails',
        'id': 'str',
        'date_created': 'datetime',
        'user_created': 'str',
        'date_modified': 'datetime',
        'user_modified': 'str'
    }

    attribute_map = {
        'line_color_solid_fill': 'lineColorSolidFill',
        'connector_id': 'connectorId',
        'parent_connector': 'parentConnector',
        'shape_id': 'shapeId',
        'parent_shape': 'parentShape',
        'dash_type_id': 'dashTypeId',
        'head_end_type_id': 'headEndTypeId',
        'tail_end_type_id': 'tailEndTypeId',
        'weight': 'weight',
        'head_end_height_id': 'headEndHeightId',
        'head_end_width_id': 'headEndWidthId',
        'tail_end_height_id': 'tailEndHeightId',
        'tail_end_width_id': 'tailEndWidthId',
        'top_border_id': 'topBorderId',
        'top_border': 'topBorder',
        'bottom_border_id': 'bottomBorderId',
        'bottom_border': 'bottomBorder',
        'right_border_id': 'rightBorderId',
        'right_border': 'rightBorder',
        'left_border_id': 'leftBorderId',
        'left_border': 'leftBorder',
        't_lto_br_border_id': 'tLtoBRBorderId',
        't_lto_br_border': 'tLtoBRBorder',
        'b_lto_tr_border_id': 'bLtoTRBorderId',
        'b_lto_tr_border': 'bLtoTRBorder',
        'line_map_id': 'lineMapId',
        'line_map': 'lineMap',
        'id': 'id',
        'date_created': 'dateCreated',
        'user_created': 'userCreated',
        'date_modified': 'dateModified',
        'user_modified': 'userModified'
    }

    def __init__(self, line_color_solid_fill=None, connector_id=None, parent_connector=None, shape_id=None, parent_shape=None, dash_type_id=None, head_end_type_id=None, tail_end_type_id=None, weight=None, head_end_height_id=None, head_end_width_id=None, tail_end_height_id=None, tail_end_width_id=None, top_border_id=None, top_border=None, bottom_border_id=None, bottom_border=None, right_border_id=None, right_border=None, left_border_id=None, left_border=None, t_lto_br_border_id=None, t_lto_br_border=None, b_lto_tr_border_id=None, b_lto_tr_border=None, line_map_id=None, line_map=None, id=None, date_created=None, user_created=None, date_modified=None, user_modified=None):  # noqa: E501
        """SharedLinesDetails - a model defined in OpenAPI"""  # noqa: E501

        self._line_color_solid_fill = None
        self._connector_id = None
        self._parent_connector = None
        self._shape_id = None
        self._parent_shape = None
        self._dash_type_id = None
        self._head_end_type_id = None
        self._tail_end_type_id = None
        self._weight = None
        self._head_end_height_id = None
        self._head_end_width_id = None
        self._tail_end_height_id = None
        self._tail_end_width_id = None
        self._top_border_id = None
        self._top_border = None
        self._bottom_border_id = None
        self._bottom_border = None
        self._right_border_id = None
        self._right_border = None
        self._left_border_id = None
        self._left_border = None
        self._t_lto_br_border_id = None
        self._t_lto_br_border = None
        self._b_lto_tr_border_id = None
        self._b_lto_tr_border = None
        self._line_map_id = None
        self._line_map = None
        self._id = None
        self._date_created = None
        self._user_created = None
        self._date_modified = None
        self._user_modified = None
        self.discriminator = None

        if line_color_solid_fill is not None:
            self.line_color_solid_fill = line_color_solid_fill
        self.connector_id = connector_id
        if parent_connector is not None:
            self.parent_connector = parent_connector
        self.shape_id = shape_id
        if parent_shape is not None:
            self.parent_shape = parent_shape
        if dash_type_id is not None:
            self.dash_type_id = dash_type_id
        if head_end_type_id is not None:
            self.head_end_type_id = head_end_type_id
        if tail_end_type_id is not None:
            self.tail_end_type_id = tail_end_type_id
        if weight is not None:
            self.weight = weight
        if head_end_height_id is not None:
            self.head_end_height_id = head_end_height_id
        if head_end_width_id is not None:
            self.head_end_width_id = head_end_width_id
        if tail_end_height_id is not None:
            self.tail_end_height_id = tail_end_height_id
        if tail_end_width_id is not None:
            self.tail_end_width_id = tail_end_width_id
        self.top_border_id = top_border_id
        if top_border is not None:
            self.top_border = top_border
        self.bottom_border_id = bottom_border_id
        if bottom_border is not None:
            self.bottom_border = bottom_border
        self.right_border_id = right_border_id
        if right_border is not None:
            self.right_border = right_border
        self.left_border_id = left_border_id
        if left_border is not None:
            self.left_border = left_border
        self.t_lto_br_border_id = t_lto_br_border_id
        if t_lto_br_border is not None:
            self.t_lto_br_border = t_lto_br_border
        self.b_lto_tr_border_id = b_lto_tr_border_id
        if b_lto_tr_border is not None:
            self.b_lto_tr_border = b_lto_tr_border
        self.line_map_id = line_map_id
        if line_map is not None:
            self.line_map = line_map
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
    def line_color_solid_fill(self):
        """Gets the line_color_solid_fill of this SharedLinesDetails.  # noqa: E501


        :return: The line_color_solid_fill of this SharedLinesDetails.  # noqa: E501
        :rtype: SharedSolidFillsDetails
        """
        return self._line_color_solid_fill

    @line_color_solid_fill.setter
    def line_color_solid_fill(self, line_color_solid_fill):
        """Sets the line_color_solid_fill of this SharedLinesDetails.


        :param line_color_solid_fill: The line_color_solid_fill of this SharedLinesDetails.  # noqa: E501
        :type: SharedSolidFillsDetails
        """

        self._line_color_solid_fill = line_color_solid_fill

    @property
    def connector_id(self):
        """Gets the connector_id of this SharedLinesDetails.  # noqa: E501


        :return: The connector_id of this SharedLinesDetails.  # noqa: E501
        :rtype: str
        """
        return self._connector_id

    @connector_id.setter
    def connector_id(self, connector_id):
        """Sets the connector_id of this SharedLinesDetails.


        :param connector_id: The connector_id of this SharedLinesDetails.  # noqa: E501
        :type: str
        """

        self._connector_id = connector_id

    @property
    def parent_connector(self):
        """Gets the parent_connector of this SharedLinesDetails.  # noqa: E501


        :return: The parent_connector of this SharedLinesDetails.  # noqa: E501
        :rtype: SlideConnectorDetails
        """
        return self._parent_connector

    @parent_connector.setter
    def parent_connector(self, parent_connector):
        """Sets the parent_connector of this SharedLinesDetails.


        :param parent_connector: The parent_connector of this SharedLinesDetails.  # noqa: E501
        :type: SlideConnectorDetails
        """

        self._parent_connector = parent_connector

    @property
    def shape_id(self):
        """Gets the shape_id of this SharedLinesDetails.  # noqa: E501


        :return: The shape_id of this SharedLinesDetails.  # noqa: E501
        :rtype: str
        """
        return self._shape_id

    @shape_id.setter
    def shape_id(self, shape_id):
        """Sets the shape_id of this SharedLinesDetails.


        :param shape_id: The shape_id of this SharedLinesDetails.  # noqa: E501
        :type: str
        """

        self._shape_id = shape_id

    @property
    def parent_shape(self):
        """Gets the parent_shape of this SharedLinesDetails.  # noqa: E501


        :return: The parent_shape of this SharedLinesDetails.  # noqa: E501
        :rtype: SlideShapesDetails
        """
        return self._parent_shape

    @parent_shape.setter
    def parent_shape(self, parent_shape):
        """Sets the parent_shape of this SharedLinesDetails.


        :param parent_shape: The parent_shape of this SharedLinesDetails.  # noqa: E501
        :type: SlideShapesDetails
        """

        self._parent_shape = parent_shape

    @property
    def dash_type_id(self):
        """Gets the dash_type_id of this SharedLinesDetails.  # noqa: E501


        :return: The dash_type_id of this SharedLinesDetails.  # noqa: E501
        :rtype: int
        """
        return self._dash_type_id

    @dash_type_id.setter
    def dash_type_id(self, dash_type_id):
        """Sets the dash_type_id of this SharedLinesDetails.


        :param dash_type_id: The dash_type_id of this SharedLinesDetails.  # noqa: E501
        :type: int
        """

        self._dash_type_id = dash_type_id

    @property
    def head_end_type_id(self):
        """Gets the head_end_type_id of this SharedLinesDetails.  # noqa: E501


        :return: The head_end_type_id of this SharedLinesDetails.  # noqa: E501
        :rtype: int
        """
        return self._head_end_type_id

    @head_end_type_id.setter
    def head_end_type_id(self, head_end_type_id):
        """Sets the head_end_type_id of this SharedLinesDetails.


        :param head_end_type_id: The head_end_type_id of this SharedLinesDetails.  # noqa: E501
        :type: int
        """

        self._head_end_type_id = head_end_type_id

    @property
    def tail_end_type_id(self):
        """Gets the tail_end_type_id of this SharedLinesDetails.  # noqa: E501


        :return: The tail_end_type_id of this SharedLinesDetails.  # noqa: E501
        :rtype: int
        """
        return self._tail_end_type_id

    @tail_end_type_id.setter
    def tail_end_type_id(self, tail_end_type_id):
        """Sets the tail_end_type_id of this SharedLinesDetails.


        :param tail_end_type_id: The tail_end_type_id of this SharedLinesDetails.  # noqa: E501
        :type: int
        """

        self._tail_end_type_id = tail_end_type_id

    @property
    def weight(self):
        """Gets the weight of this SharedLinesDetails.  # noqa: E501


        :return: The weight of this SharedLinesDetails.  # noqa: E501
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this SharedLinesDetails.


        :param weight: The weight of this SharedLinesDetails.  # noqa: E501
        :type: int
        """

        self._weight = weight

    @property
    def head_end_height_id(self):
        """Gets the head_end_height_id of this SharedLinesDetails.  # noqa: E501


        :return: The head_end_height_id of this SharedLinesDetails.  # noqa: E501
        :rtype: int
        """
        return self._head_end_height_id

    @head_end_height_id.setter
    def head_end_height_id(self, head_end_height_id):
        """Sets the head_end_height_id of this SharedLinesDetails.


        :param head_end_height_id: The head_end_height_id of this SharedLinesDetails.  # noqa: E501
        :type: int
        """

        self._head_end_height_id = head_end_height_id

    @property
    def head_end_width_id(self):
        """Gets the head_end_width_id of this SharedLinesDetails.  # noqa: E501


        :return: The head_end_width_id of this SharedLinesDetails.  # noqa: E501
        :rtype: int
        """
        return self._head_end_width_id

    @head_end_width_id.setter
    def head_end_width_id(self, head_end_width_id):
        """Sets the head_end_width_id of this SharedLinesDetails.


        :param head_end_width_id: The head_end_width_id of this SharedLinesDetails.  # noqa: E501
        :type: int
        """

        self._head_end_width_id = head_end_width_id

    @property
    def tail_end_height_id(self):
        """Gets the tail_end_height_id of this SharedLinesDetails.  # noqa: E501


        :return: The tail_end_height_id of this SharedLinesDetails.  # noqa: E501
        :rtype: int
        """
        return self._tail_end_height_id

    @tail_end_height_id.setter
    def tail_end_height_id(self, tail_end_height_id):
        """Sets the tail_end_height_id of this SharedLinesDetails.


        :param tail_end_height_id: The tail_end_height_id of this SharedLinesDetails.  # noqa: E501
        :type: int
        """

        self._tail_end_height_id = tail_end_height_id

    @property
    def tail_end_width_id(self):
        """Gets the tail_end_width_id of this SharedLinesDetails.  # noqa: E501


        :return: The tail_end_width_id of this SharedLinesDetails.  # noqa: E501
        :rtype: int
        """
        return self._tail_end_width_id

    @tail_end_width_id.setter
    def tail_end_width_id(self, tail_end_width_id):
        """Sets the tail_end_width_id of this SharedLinesDetails.


        :param tail_end_width_id: The tail_end_width_id of this SharedLinesDetails.  # noqa: E501
        :type: int
        """

        self._tail_end_width_id = tail_end_width_id

    @property
    def top_border_id(self):
        """Gets the top_border_id of this SharedLinesDetails.  # noqa: E501


        :return: The top_border_id of this SharedLinesDetails.  # noqa: E501
        :rtype: str
        """
        return self._top_border_id

    @top_border_id.setter
    def top_border_id(self, top_border_id):
        """Sets the top_border_id of this SharedLinesDetails.


        :param top_border_id: The top_border_id of this SharedLinesDetails.  # noqa: E501
        :type: str
        """

        self._top_border_id = top_border_id

    @property
    def top_border(self):
        """Gets the top_border of this SharedLinesDetails.  # noqa: E501


        :return: The top_border of this SharedLinesDetails.  # noqa: E501
        :rtype: TableBordersDetails
        """
        return self._top_border

    @top_border.setter
    def top_border(self, top_border):
        """Sets the top_border of this SharedLinesDetails.


        :param top_border: The top_border of this SharedLinesDetails.  # noqa: E501
        :type: TableBordersDetails
        """

        self._top_border = top_border

    @property
    def bottom_border_id(self):
        """Gets the bottom_border_id of this SharedLinesDetails.  # noqa: E501


        :return: The bottom_border_id of this SharedLinesDetails.  # noqa: E501
        :rtype: str
        """
        return self._bottom_border_id

    @bottom_border_id.setter
    def bottom_border_id(self, bottom_border_id):
        """Sets the bottom_border_id of this SharedLinesDetails.


        :param bottom_border_id: The bottom_border_id of this SharedLinesDetails.  # noqa: E501
        :type: str
        """

        self._bottom_border_id = bottom_border_id

    @property
    def bottom_border(self):
        """Gets the bottom_border of this SharedLinesDetails.  # noqa: E501


        :return: The bottom_border of this SharedLinesDetails.  # noqa: E501
        :rtype: TableBordersDetails
        """
        return self._bottom_border

    @bottom_border.setter
    def bottom_border(self, bottom_border):
        """Sets the bottom_border of this SharedLinesDetails.


        :param bottom_border: The bottom_border of this SharedLinesDetails.  # noqa: E501
        :type: TableBordersDetails
        """

        self._bottom_border = bottom_border

    @property
    def right_border_id(self):
        """Gets the right_border_id of this SharedLinesDetails.  # noqa: E501


        :return: The right_border_id of this SharedLinesDetails.  # noqa: E501
        :rtype: str
        """
        return self._right_border_id

    @right_border_id.setter
    def right_border_id(self, right_border_id):
        """Sets the right_border_id of this SharedLinesDetails.


        :param right_border_id: The right_border_id of this SharedLinesDetails.  # noqa: E501
        :type: str
        """

        self._right_border_id = right_border_id

    @property
    def right_border(self):
        """Gets the right_border of this SharedLinesDetails.  # noqa: E501


        :return: The right_border of this SharedLinesDetails.  # noqa: E501
        :rtype: TableBordersDetails
        """
        return self._right_border

    @right_border.setter
    def right_border(self, right_border):
        """Sets the right_border of this SharedLinesDetails.


        :param right_border: The right_border of this SharedLinesDetails.  # noqa: E501
        :type: TableBordersDetails
        """

        self._right_border = right_border

    @property
    def left_border_id(self):
        """Gets the left_border_id of this SharedLinesDetails.  # noqa: E501


        :return: The left_border_id of this SharedLinesDetails.  # noqa: E501
        :rtype: str
        """
        return self._left_border_id

    @left_border_id.setter
    def left_border_id(self, left_border_id):
        """Sets the left_border_id of this SharedLinesDetails.


        :param left_border_id: The left_border_id of this SharedLinesDetails.  # noqa: E501
        :type: str
        """

        self._left_border_id = left_border_id

    @property
    def left_border(self):
        """Gets the left_border of this SharedLinesDetails.  # noqa: E501


        :return: The left_border of this SharedLinesDetails.  # noqa: E501
        :rtype: TableBordersDetails
        """
        return self._left_border

    @left_border.setter
    def left_border(self, left_border):
        """Sets the left_border of this SharedLinesDetails.


        :param left_border: The left_border of this SharedLinesDetails.  # noqa: E501
        :type: TableBordersDetails
        """

        self._left_border = left_border

    @property
    def t_lto_br_border_id(self):
        """Gets the t_lto_br_border_id of this SharedLinesDetails.  # noqa: E501


        :return: The t_lto_br_border_id of this SharedLinesDetails.  # noqa: E501
        :rtype: str
        """
        return self._t_lto_br_border_id

    @t_lto_br_border_id.setter
    def t_lto_br_border_id(self, t_lto_br_border_id):
        """Sets the t_lto_br_border_id of this SharedLinesDetails.


        :param t_lto_br_border_id: The t_lto_br_border_id of this SharedLinesDetails.  # noqa: E501
        :type: str
        """

        self._t_lto_br_border_id = t_lto_br_border_id

    @property
    def t_lto_br_border(self):
        """Gets the t_lto_br_border of this SharedLinesDetails.  # noqa: E501


        :return: The t_lto_br_border of this SharedLinesDetails.  # noqa: E501
        :rtype: TableBordersDetails
        """
        return self._t_lto_br_border

    @t_lto_br_border.setter
    def t_lto_br_border(self, t_lto_br_border):
        """Sets the t_lto_br_border of this SharedLinesDetails.


        :param t_lto_br_border: The t_lto_br_border of this SharedLinesDetails.  # noqa: E501
        :type: TableBordersDetails
        """

        self._t_lto_br_border = t_lto_br_border

    @property
    def b_lto_tr_border_id(self):
        """Gets the b_lto_tr_border_id of this SharedLinesDetails.  # noqa: E501


        :return: The b_lto_tr_border_id of this SharedLinesDetails.  # noqa: E501
        :rtype: str
        """
        return self._b_lto_tr_border_id

    @b_lto_tr_border_id.setter
    def b_lto_tr_border_id(self, b_lto_tr_border_id):
        """Sets the b_lto_tr_border_id of this SharedLinesDetails.


        :param b_lto_tr_border_id: The b_lto_tr_border_id of this SharedLinesDetails.  # noqa: E501
        :type: str
        """

        self._b_lto_tr_border_id = b_lto_tr_border_id

    @property
    def b_lto_tr_border(self):
        """Gets the b_lto_tr_border of this SharedLinesDetails.  # noqa: E501


        :return: The b_lto_tr_border of this SharedLinesDetails.  # noqa: E501
        :rtype: TableBordersDetails
        """
        return self._b_lto_tr_border

    @b_lto_tr_border.setter
    def b_lto_tr_border(self, b_lto_tr_border):
        """Sets the b_lto_tr_border of this SharedLinesDetails.


        :param b_lto_tr_border: The b_lto_tr_border of this SharedLinesDetails.  # noqa: E501
        :type: TableBordersDetails
        """

        self._b_lto_tr_border = b_lto_tr_border

    @property
    def line_map_id(self):
        """Gets the line_map_id of this SharedLinesDetails.  # noqa: E501


        :return: The line_map_id of this SharedLinesDetails.  # noqa: E501
        :rtype: str
        """
        return self._line_map_id

    @line_map_id.setter
    def line_map_id(self, line_map_id):
        """Sets the line_map_id of this SharedLinesDetails.


        :param line_map_id: The line_map_id of this SharedLinesDetails.  # noqa: E501
        :type: str
        """

        self._line_map_id = line_map_id

    @property
    def line_map(self):
        """Gets the line_map of this SharedLinesDetails.  # noqa: E501


        :return: The line_map of this SharedLinesDetails.  # noqa: E501
        :rtype: ThemeLineMapDetails
        """
        return self._line_map

    @line_map.setter
    def line_map(self, line_map):
        """Sets the line_map of this SharedLinesDetails.


        :param line_map: The line_map of this SharedLinesDetails.  # noqa: E501
        :type: ThemeLineMapDetails
        """

        self._line_map = line_map

    @property
    def id(self):
        """Gets the id of this SharedLinesDetails.  # noqa: E501


        :return: The id of this SharedLinesDetails.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SharedLinesDetails.


        :param id: The id of this SharedLinesDetails.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def date_created(self):
        """Gets the date_created of this SharedLinesDetails.  # noqa: E501


        :return: The date_created of this SharedLinesDetails.  # noqa: E501
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this SharedLinesDetails.


        :param date_created: The date_created of this SharedLinesDetails.  # noqa: E501
        :type: datetime
        """

        self._date_created = date_created

    @property
    def user_created(self):
        """Gets the user_created of this SharedLinesDetails.  # noqa: E501


        :return: The user_created of this SharedLinesDetails.  # noqa: E501
        :rtype: str
        """
        return self._user_created

    @user_created.setter
    def user_created(self, user_created):
        """Sets the user_created of this SharedLinesDetails.


        :param user_created: The user_created of this SharedLinesDetails.  # noqa: E501
        :type: str
        """

        self._user_created = user_created

    @property
    def date_modified(self):
        """Gets the date_modified of this SharedLinesDetails.  # noqa: E501


        :return: The date_modified of this SharedLinesDetails.  # noqa: E501
        :rtype: datetime
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this SharedLinesDetails.


        :param date_modified: The date_modified of this SharedLinesDetails.  # noqa: E501
        :type: datetime
        """

        self._date_modified = date_modified

    @property
    def user_modified(self):
        """Gets the user_modified of this SharedLinesDetails.  # noqa: E501


        :return: The user_modified of this SharedLinesDetails.  # noqa: E501
        :rtype: str
        """
        return self._user_modified

    @user_modified.setter
    def user_modified(self, user_modified):
        """Sets the user_modified of this SharedLinesDetails.


        :param user_modified: The user_modified of this SharedLinesDetails.  # noqa: E501
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
        if not isinstance(other, SharedLinesDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
