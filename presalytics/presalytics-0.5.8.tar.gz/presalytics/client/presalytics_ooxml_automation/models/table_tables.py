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


class TableTables(object):
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
        'svg_blob_url': 'str',
        'has_style_part': 'bool',
        'style_part_outer_xml': 'str',
        'parent_graphic_id': 'str',
        'base_element_blob_url': 'str',
        'changed_base_element_blob_url': 'str',
        'package_uri': 'str',
        'name': 'str',
        'id': 'str'
    }

    attribute_map = {
        'svg_blob_url': 'svgBlobUrl',
        'has_style_part': 'hasStylePart',
        'style_part_outer_xml': 'stylePartOuterXml',
        'parent_graphic_id': 'parentGraphicId',
        'base_element_blob_url': 'baseElementBlobUrl',
        'changed_base_element_blob_url': 'changedBaseElementBlobUrl',
        'package_uri': 'packageUri',
        'name': 'name',
        'id': 'id'
    }

    def __init__(self, svg_blob_url=None, has_style_part=None, style_part_outer_xml=None, parent_graphic_id=None, base_element_blob_url=None, changed_base_element_blob_url=None, package_uri=None, name=None, id=None):  # noqa: E501
        """TableTables - a model defined in OpenAPI"""  # noqa: E501

        self._svg_blob_url = None
        self._has_style_part = None
        self._style_part_outer_xml = None
        self._parent_graphic_id = None
        self._base_element_blob_url = None
        self._changed_base_element_blob_url = None
        self._package_uri = None
        self._name = None
        self._id = None
        self.discriminator = None

        self.svg_blob_url = svg_blob_url
        if has_style_part is not None:
            self.has_style_part = has_style_part
        self.style_part_outer_xml = style_part_outer_xml
        self.parent_graphic_id = parent_graphic_id
        self.base_element_blob_url = base_element_blob_url
        self.changed_base_element_blob_url = changed_base_element_blob_url
        self.package_uri = package_uri
        self.name = name
        if id is not None:
            self.id = id

    @property
    def svg_blob_url(self):
        """Gets the svg_blob_url of this TableTables.  # noqa: E501


        :return: The svg_blob_url of this TableTables.  # noqa: E501
        :rtype: str
        """
        return self._svg_blob_url

    @svg_blob_url.setter
    def svg_blob_url(self, svg_blob_url):
        """Sets the svg_blob_url of this TableTables.


        :param svg_blob_url: The svg_blob_url of this TableTables.  # noqa: E501
        :type: str
        """

        self._svg_blob_url = svg_blob_url

    @property
    def has_style_part(self):
        """Gets the has_style_part of this TableTables.  # noqa: E501


        :return: The has_style_part of this TableTables.  # noqa: E501
        :rtype: bool
        """
        return self._has_style_part

    @has_style_part.setter
    def has_style_part(self, has_style_part):
        """Sets the has_style_part of this TableTables.


        :param has_style_part: The has_style_part of this TableTables.  # noqa: E501
        :type: bool
        """

        self._has_style_part = has_style_part

    @property
    def style_part_outer_xml(self):
        """Gets the style_part_outer_xml of this TableTables.  # noqa: E501


        :return: The style_part_outer_xml of this TableTables.  # noqa: E501
        :rtype: str
        """
        return self._style_part_outer_xml

    @style_part_outer_xml.setter
    def style_part_outer_xml(self, style_part_outer_xml):
        """Sets the style_part_outer_xml of this TableTables.


        :param style_part_outer_xml: The style_part_outer_xml of this TableTables.  # noqa: E501
        :type: str
        """

        self._style_part_outer_xml = style_part_outer_xml

    @property
    def parent_graphic_id(self):
        """Gets the parent_graphic_id of this TableTables.  # noqa: E501


        :return: The parent_graphic_id of this TableTables.  # noqa: E501
        :rtype: str
        """
        return self._parent_graphic_id

    @parent_graphic_id.setter
    def parent_graphic_id(self, parent_graphic_id):
        """Sets the parent_graphic_id of this TableTables.


        :param parent_graphic_id: The parent_graphic_id of this TableTables.  # noqa: E501
        :type: str
        """

        self._parent_graphic_id = parent_graphic_id

    @property
    def base_element_blob_url(self):
        """Gets the base_element_blob_url of this TableTables.  # noqa: E501


        :return: The base_element_blob_url of this TableTables.  # noqa: E501
        :rtype: str
        """
        return self._base_element_blob_url

    @base_element_blob_url.setter
    def base_element_blob_url(self, base_element_blob_url):
        """Sets the base_element_blob_url of this TableTables.


        :param base_element_blob_url: The base_element_blob_url of this TableTables.  # noqa: E501
        :type: str
        """

        self._base_element_blob_url = base_element_blob_url

    @property
    def changed_base_element_blob_url(self):
        """Gets the changed_base_element_blob_url of this TableTables.  # noqa: E501


        :return: The changed_base_element_blob_url of this TableTables.  # noqa: E501
        :rtype: str
        """
        return self._changed_base_element_blob_url

    @changed_base_element_blob_url.setter
    def changed_base_element_blob_url(self, changed_base_element_blob_url):
        """Sets the changed_base_element_blob_url of this TableTables.


        :param changed_base_element_blob_url: The changed_base_element_blob_url of this TableTables.  # noqa: E501
        :type: str
        """

        self._changed_base_element_blob_url = changed_base_element_blob_url

    @property
    def package_uri(self):
        """Gets the package_uri of this TableTables.  # noqa: E501


        :return: The package_uri of this TableTables.  # noqa: E501
        :rtype: str
        """
        return self._package_uri

    @package_uri.setter
    def package_uri(self, package_uri):
        """Sets the package_uri of this TableTables.


        :param package_uri: The package_uri of this TableTables.  # noqa: E501
        :type: str
        """

        self._package_uri = package_uri

    @property
    def name(self):
        """Gets the name of this TableTables.  # noqa: E501


        :return: The name of this TableTables.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TableTables.


        :param name: The name of this TableTables.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def id(self):
        """Gets the id of this TableTables.  # noqa: E501


        :return: The id of this TableTables.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TableTables.


        :param id: The id of this TableTables.  # noqa: E501
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
        if not isinstance(other, TableTables):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
