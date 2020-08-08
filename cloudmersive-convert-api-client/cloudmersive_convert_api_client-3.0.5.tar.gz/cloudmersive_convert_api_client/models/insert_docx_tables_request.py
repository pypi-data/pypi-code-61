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


class InsertDocxTablesRequest(object):
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
        'input_file_bytes': 'str',
        'input_file_url': 'str',
        'table_to_insert': 'DocxTable',
        'insert_placement': 'str',
        'insert_path': 'str'
    }

    attribute_map = {
        'input_file_bytes': 'InputFileBytes',
        'input_file_url': 'InputFileUrl',
        'table_to_insert': 'TableToInsert',
        'insert_placement': 'InsertPlacement',
        'insert_path': 'InsertPath'
    }

    def __init__(self, input_file_bytes=None, input_file_url=None, table_to_insert=None, insert_placement=None, insert_path=None):  # noqa: E501
        """InsertDocxTablesRequest - a model defined in Swagger"""  # noqa: E501

        self._input_file_bytes = None
        self._input_file_url = None
        self._table_to_insert = None
        self._insert_placement = None
        self._insert_path = None
        self.discriminator = None

        if input_file_bytes is not None:
            self.input_file_bytes = input_file_bytes
        if input_file_url is not None:
            self.input_file_url = input_file_url
        if table_to_insert is not None:
            self.table_to_insert = table_to_insert
        if insert_placement is not None:
            self.insert_placement = insert_placement
        if insert_path is not None:
            self.insert_path = insert_path

    @property
    def input_file_bytes(self):
        """Gets the input_file_bytes of this InsertDocxTablesRequest.  # noqa: E501

        Optional: Bytes of the input file to operate on  # noqa: E501

        :return: The input_file_bytes of this InsertDocxTablesRequest.  # noqa: E501
        :rtype: str
        """
        return self._input_file_bytes

    @input_file_bytes.setter
    def input_file_bytes(self, input_file_bytes):
        """Sets the input_file_bytes of this InsertDocxTablesRequest.

        Optional: Bytes of the input file to operate on  # noqa: E501

        :param input_file_bytes: The input_file_bytes of this InsertDocxTablesRequest.  # noqa: E501
        :type: str
        """
        if input_file_bytes is not None and not re.search(r'^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$', input_file_bytes):  # noqa: E501
            raise ValueError(r"Invalid value for `input_file_bytes`, must be a follow pattern or equal to `/^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$/`")  # noqa: E501

        self._input_file_bytes = input_file_bytes

    @property
    def input_file_url(self):
        """Gets the input_file_url of this InsertDocxTablesRequest.  # noqa: E501

        Optional: URL of a file to operate on as input.  This can be a public URL, or you can also use the begin-editing API to upload a document and pass in the secure URL result from that operation as the URL here (this URL is not public).  # noqa: E501

        :return: The input_file_url of this InsertDocxTablesRequest.  # noqa: E501
        :rtype: str
        """
        return self._input_file_url

    @input_file_url.setter
    def input_file_url(self, input_file_url):
        """Sets the input_file_url of this InsertDocxTablesRequest.

        Optional: URL of a file to operate on as input.  This can be a public URL, or you can also use the begin-editing API to upload a document and pass in the secure URL result from that operation as the URL here (this URL is not public).  # noqa: E501

        :param input_file_url: The input_file_url of this InsertDocxTablesRequest.  # noqa: E501
        :type: str
        """

        self._input_file_url = input_file_url

    @property
    def table_to_insert(self):
        """Gets the table_to_insert of this InsertDocxTablesRequest.  # noqa: E501

        Table you would like to insert  # noqa: E501

        :return: The table_to_insert of this InsertDocxTablesRequest.  # noqa: E501
        :rtype: DocxTable
        """
        return self._table_to_insert

    @table_to_insert.setter
    def table_to_insert(self, table_to_insert):
        """Sets the table_to_insert of this InsertDocxTablesRequest.

        Table you would like to insert  # noqa: E501

        :param table_to_insert: The table_to_insert of this InsertDocxTablesRequest.  # noqa: E501
        :type: DocxTable
        """

        self._table_to_insert = table_to_insert

    @property
    def insert_placement(self):
        """Gets the insert_placement of this InsertDocxTablesRequest.  # noqa: E501

        Optional; default is DocumentEnd.  Placement Type of the insert; possible values are: DocumentStart (very beginning of the document), DocumentEnd (very end of the document), BeforeExistingObject (right before an existing object - fill in the InsertPath field using the Path value from an existing object), AfterExistingObject (right after an existing object - fill in the InsertPath field using the Path value from an existing object)  # noqa: E501

        :return: The insert_placement of this InsertDocxTablesRequest.  # noqa: E501
        :rtype: str
        """
        return self._insert_placement

    @insert_placement.setter
    def insert_placement(self, insert_placement):
        """Sets the insert_placement of this InsertDocxTablesRequest.

        Optional; default is DocumentEnd.  Placement Type of the insert; possible values are: DocumentStart (very beginning of the document), DocumentEnd (very end of the document), BeforeExistingObject (right before an existing object - fill in the InsertPath field using the Path value from an existing object), AfterExistingObject (right after an existing object - fill in the InsertPath field using the Path value from an existing object)  # noqa: E501

        :param insert_placement: The insert_placement of this InsertDocxTablesRequest.  # noqa: E501
        :type: str
        """

        self._insert_placement = insert_placement

    @property
    def insert_path(self):
        """Gets the insert_path of this InsertDocxTablesRequest.  # noqa: E501

        Optional; location within the document to insert the object; fill in the InsertPath field using the Path value from an existing object.  Used with InsertPlacement of BeforeExistingObject or AfterExistingObject  # noqa: E501

        :return: The insert_path of this InsertDocxTablesRequest.  # noqa: E501
        :rtype: str
        """
        return self._insert_path

    @insert_path.setter
    def insert_path(self, insert_path):
        """Sets the insert_path of this InsertDocxTablesRequest.

        Optional; location within the document to insert the object; fill in the InsertPath field using the Path value from an existing object.  Used with InsertPlacement of BeforeExistingObject or AfterExistingObject  # noqa: E501

        :param insert_path: The insert_path of this InsertDocxTablesRequest.  # noqa: E501
        :type: str
        """

        self._insert_path = insert_path

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
        if issubclass(InsertDocxTablesRequest, dict):
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
        if not isinstance(other, InsertDocxTablesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
