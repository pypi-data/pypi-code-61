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


class SlideSmartArtsDetails(object):
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
        'graphics_id': 'str',
        'parent_graphic': 'SlideGraphicsDetails',
        'svg_blob_url': 'str',
        'base_element_blob_url': 'str',
        'changed_base_element_blob_url': 'str',
        'package_uri': 'str',
        'name': 'str',
        'id': 'str',
        'date_created': 'datetime',
        'user_created': 'str',
        'date_modified': 'datetime',
        'user_modified': 'str'
    }

    attribute_map = {
        'graphics_id': 'graphicsId',
        'parent_graphic': 'parentGraphic',
        'svg_blob_url': 'svgBlobUrl',
        'base_element_blob_url': 'baseElementBlobUrl',
        'changed_base_element_blob_url': 'changedBaseElementBlobUrl',
        'package_uri': 'packageUri',
        'name': 'name',
        'id': 'id',
        'date_created': 'dateCreated',
        'user_created': 'userCreated',
        'date_modified': 'dateModified',
        'user_modified': 'userModified'
    }

    def __init__(self, graphics_id=None, parent_graphic=None, svg_blob_url=None, base_element_blob_url=None, changed_base_element_blob_url=None, package_uri=None, name=None, id=None, date_created=None, user_created=None, date_modified=None, user_modified=None):  # noqa: E501
        """SlideSmartArtsDetails - a model defined in OpenAPI"""  # noqa: E501

        self._graphics_id = None
        self._parent_graphic = None
        self._svg_blob_url = None
        self._base_element_blob_url = None
        self._changed_base_element_blob_url = None
        self._package_uri = None
        self._name = None
        self._id = None
        self._date_created = None
        self._user_created = None
        self._date_modified = None
        self._user_modified = None
        self.discriminator = None

        self.graphics_id = graphics_id
        if parent_graphic is not None:
            self.parent_graphic = parent_graphic
        self.svg_blob_url = svg_blob_url
        self.base_element_blob_url = base_element_blob_url
        self.changed_base_element_blob_url = changed_base_element_blob_url
        self.package_uri = package_uri
        self.name = name
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
    def graphics_id(self):
        """Gets the graphics_id of this SlideSmartArtsDetails.  # noqa: E501


        :return: The graphics_id of this SlideSmartArtsDetails.  # noqa: E501
        :rtype: str
        """
        return self._graphics_id

    @graphics_id.setter
    def graphics_id(self, graphics_id):
        """Sets the graphics_id of this SlideSmartArtsDetails.


        :param graphics_id: The graphics_id of this SlideSmartArtsDetails.  # noqa: E501
        :type: str
        """

        self._graphics_id = graphics_id

    @property
    def parent_graphic(self):
        """Gets the parent_graphic of this SlideSmartArtsDetails.  # noqa: E501


        :return: The parent_graphic of this SlideSmartArtsDetails.  # noqa: E501
        :rtype: SlideGraphicsDetails
        """
        return self._parent_graphic

    @parent_graphic.setter
    def parent_graphic(self, parent_graphic):
        """Sets the parent_graphic of this SlideSmartArtsDetails.


        :param parent_graphic: The parent_graphic of this SlideSmartArtsDetails.  # noqa: E501
        :type: SlideGraphicsDetails
        """

        self._parent_graphic = parent_graphic

    @property
    def svg_blob_url(self):
        """Gets the svg_blob_url of this SlideSmartArtsDetails.  # noqa: E501


        :return: The svg_blob_url of this SlideSmartArtsDetails.  # noqa: E501
        :rtype: str
        """
        return self._svg_blob_url

    @svg_blob_url.setter
    def svg_blob_url(self, svg_blob_url):
        """Sets the svg_blob_url of this SlideSmartArtsDetails.


        :param svg_blob_url: The svg_blob_url of this SlideSmartArtsDetails.  # noqa: E501
        :type: str
        """

        self._svg_blob_url = svg_blob_url

    @property
    def base_element_blob_url(self):
        """Gets the base_element_blob_url of this SlideSmartArtsDetails.  # noqa: E501


        :return: The base_element_blob_url of this SlideSmartArtsDetails.  # noqa: E501
        :rtype: str
        """
        return self._base_element_blob_url

    @base_element_blob_url.setter
    def base_element_blob_url(self, base_element_blob_url):
        """Sets the base_element_blob_url of this SlideSmartArtsDetails.


        :param base_element_blob_url: The base_element_blob_url of this SlideSmartArtsDetails.  # noqa: E501
        :type: str
        """

        self._base_element_blob_url = base_element_blob_url

    @property
    def changed_base_element_blob_url(self):
        """Gets the changed_base_element_blob_url of this SlideSmartArtsDetails.  # noqa: E501


        :return: The changed_base_element_blob_url of this SlideSmartArtsDetails.  # noqa: E501
        :rtype: str
        """
        return self._changed_base_element_blob_url

    @changed_base_element_blob_url.setter
    def changed_base_element_blob_url(self, changed_base_element_blob_url):
        """Sets the changed_base_element_blob_url of this SlideSmartArtsDetails.


        :param changed_base_element_blob_url: The changed_base_element_blob_url of this SlideSmartArtsDetails.  # noqa: E501
        :type: str
        """

        self._changed_base_element_blob_url = changed_base_element_blob_url

    @property
    def package_uri(self):
        """Gets the package_uri of this SlideSmartArtsDetails.  # noqa: E501


        :return: The package_uri of this SlideSmartArtsDetails.  # noqa: E501
        :rtype: str
        """
        return self._package_uri

    @package_uri.setter
    def package_uri(self, package_uri):
        """Sets the package_uri of this SlideSmartArtsDetails.


        :param package_uri: The package_uri of this SlideSmartArtsDetails.  # noqa: E501
        :type: str
        """

        self._package_uri = package_uri

    @property
    def name(self):
        """Gets the name of this SlideSmartArtsDetails.  # noqa: E501


        :return: The name of this SlideSmartArtsDetails.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SlideSmartArtsDetails.


        :param name: The name of this SlideSmartArtsDetails.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def id(self):
        """Gets the id of this SlideSmartArtsDetails.  # noqa: E501


        :return: The id of this SlideSmartArtsDetails.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SlideSmartArtsDetails.


        :param id: The id of this SlideSmartArtsDetails.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def date_created(self):
        """Gets the date_created of this SlideSmartArtsDetails.  # noqa: E501


        :return: The date_created of this SlideSmartArtsDetails.  # noqa: E501
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this SlideSmartArtsDetails.


        :param date_created: The date_created of this SlideSmartArtsDetails.  # noqa: E501
        :type: datetime
        """

        self._date_created = date_created

    @property
    def user_created(self):
        """Gets the user_created of this SlideSmartArtsDetails.  # noqa: E501


        :return: The user_created of this SlideSmartArtsDetails.  # noqa: E501
        :rtype: str
        """
        return self._user_created

    @user_created.setter
    def user_created(self, user_created):
        """Sets the user_created of this SlideSmartArtsDetails.


        :param user_created: The user_created of this SlideSmartArtsDetails.  # noqa: E501
        :type: str
        """

        self._user_created = user_created

    @property
    def date_modified(self):
        """Gets the date_modified of this SlideSmartArtsDetails.  # noqa: E501


        :return: The date_modified of this SlideSmartArtsDetails.  # noqa: E501
        :rtype: datetime
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this SlideSmartArtsDetails.


        :param date_modified: The date_modified of this SlideSmartArtsDetails.  # noqa: E501
        :type: datetime
        """

        self._date_modified = date_modified

    @property
    def user_modified(self):
        """Gets the user_modified of this SlideSmartArtsDetails.  # noqa: E501


        :return: The user_modified of this SlideSmartArtsDetails.  # noqa: E501
        :rtype: str
        """
        return self._user_modified

    @user_modified.setter
    def user_modified(self, user_modified):
        """Sets the user_modified of this SlideSmartArtsDetails.


        :param user_modified: The user_modified of this SlideSmartArtsDetails.  # noqa: E501
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
        if not isinstance(other, SlideSmartArtsDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
