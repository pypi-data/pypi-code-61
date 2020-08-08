# coding: utf-8

"""
    Pulp 3 API

    Fetch, Upload, Organize, and Distribute Software Packages  # noqa: E501

    The version of the OpenAPI document: v3
    Contact: pulp-list@redhat.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pulpcore.client.pulp_container.configuration import Configuration


class ContainerManifestResponse(object):
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
        'pulp_href': 'str',
        'pulp_created': 'datetime',
        'artifact': 'str',
        'digest': 'str',
        'schema_version': 'int',
        'media_type': 'str',
        'listed_manifests': 'list[str]',
        'config_blob': 'str',
        'blobs': 'list[str]'
    }

    attribute_map = {
        'pulp_href': 'pulp_href',
        'pulp_created': 'pulp_created',
        'artifact': 'artifact',
        'digest': 'digest',
        'schema_version': 'schema_version',
        'media_type': 'media_type',
        'listed_manifests': 'listed_manifests',
        'config_blob': 'config_blob',
        'blobs': 'blobs'
    }

    def __init__(self, pulp_href=None, pulp_created=None, artifact=None, digest=None, schema_version=None, media_type=None, listed_manifests=None, config_blob=None, blobs=None, local_vars_configuration=None):  # noqa: E501
        """ContainerManifestResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._pulp_href = None
        self._pulp_created = None
        self._artifact = None
        self._digest = None
        self._schema_version = None
        self._media_type = None
        self._listed_manifests = None
        self._config_blob = None
        self._blobs = None
        self.discriminator = None

        if pulp_href is not None:
            self.pulp_href = pulp_href
        if pulp_created is not None:
            self.pulp_created = pulp_created
        self.artifact = artifact
        self.digest = digest
        self.schema_version = schema_version
        self.media_type = media_type
        self.listed_manifests = listed_manifests
        if config_blob is not None:
            self.config_blob = config_blob
        self.blobs = blobs

    @property
    def pulp_href(self):
        """Gets the pulp_href of this ContainerManifestResponse.  # noqa: E501


        :return: The pulp_href of this ContainerManifestResponse.  # noqa: E501
        :rtype: str
        """
        return self._pulp_href

    @pulp_href.setter
    def pulp_href(self, pulp_href):
        """Sets the pulp_href of this ContainerManifestResponse.


        :param pulp_href: The pulp_href of this ContainerManifestResponse.  # noqa: E501
        :type: str
        """

        self._pulp_href = pulp_href

    @property
    def pulp_created(self):
        """Gets the pulp_created of this ContainerManifestResponse.  # noqa: E501

        Timestamp of creation.  # noqa: E501

        :return: The pulp_created of this ContainerManifestResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._pulp_created

    @pulp_created.setter
    def pulp_created(self, pulp_created):
        """Sets the pulp_created of this ContainerManifestResponse.

        Timestamp of creation.  # noqa: E501

        :param pulp_created: The pulp_created of this ContainerManifestResponse.  # noqa: E501
        :type: datetime
        """

        self._pulp_created = pulp_created

    @property
    def artifact(self):
        """Gets the artifact of this ContainerManifestResponse.  # noqa: E501

        Artifact file representing the physical content  # noqa: E501

        :return: The artifact of this ContainerManifestResponse.  # noqa: E501
        :rtype: str
        """
        return self._artifact

    @artifact.setter
    def artifact(self, artifact):
        """Sets the artifact of this ContainerManifestResponse.

        Artifact file representing the physical content  # noqa: E501

        :param artifact: The artifact of this ContainerManifestResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and artifact is None:  # noqa: E501
            raise ValueError("Invalid value for `artifact`, must not be `None`")  # noqa: E501

        self._artifact = artifact

    @property
    def digest(self):
        """Gets the digest of this ContainerManifestResponse.  # noqa: E501

        sha256 of the Manifest file  # noqa: E501

        :return: The digest of this ContainerManifestResponse.  # noqa: E501
        :rtype: str
        """
        return self._digest

    @digest.setter
    def digest(self, digest):
        """Sets the digest of this ContainerManifestResponse.

        sha256 of the Manifest file  # noqa: E501

        :param digest: The digest of this ContainerManifestResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and digest is None:  # noqa: E501
            raise ValueError("Invalid value for `digest`, must not be `None`")  # noqa: E501

        self._digest = digest

    @property
    def schema_version(self):
        """Gets the schema_version of this ContainerManifestResponse.  # noqa: E501

        Manifest schema version  # noqa: E501

        :return: The schema_version of this ContainerManifestResponse.  # noqa: E501
        :rtype: int
        """
        return self._schema_version

    @schema_version.setter
    def schema_version(self, schema_version):
        """Sets the schema_version of this ContainerManifestResponse.

        Manifest schema version  # noqa: E501

        :param schema_version: The schema_version of this ContainerManifestResponse.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and schema_version is None:  # noqa: E501
            raise ValueError("Invalid value for `schema_version`, must not be `None`")  # noqa: E501

        self._schema_version = schema_version

    @property
    def media_type(self):
        """Gets the media_type of this ContainerManifestResponse.  # noqa: E501

        Manifest media type of the file  # noqa: E501

        :return: The media_type of this ContainerManifestResponse.  # noqa: E501
        :rtype: str
        """
        return self._media_type

    @media_type.setter
    def media_type(self, media_type):
        """Sets the media_type of this ContainerManifestResponse.

        Manifest media type of the file  # noqa: E501

        :param media_type: The media_type of this ContainerManifestResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and media_type is None:  # noqa: E501
            raise ValueError("Invalid value for `media_type`, must not be `None`")  # noqa: E501

        self._media_type = media_type

    @property
    def listed_manifests(self):
        """Gets the listed_manifests of this ContainerManifestResponse.  # noqa: E501

        Manifests that are referenced by this Manifest List  # noqa: E501

        :return: The listed_manifests of this ContainerManifestResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._listed_manifests

    @listed_manifests.setter
    def listed_manifests(self, listed_manifests):
        """Sets the listed_manifests of this ContainerManifestResponse.

        Manifests that are referenced by this Manifest List  # noqa: E501

        :param listed_manifests: The listed_manifests of this ContainerManifestResponse.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and listed_manifests is None:  # noqa: E501
            raise ValueError("Invalid value for `listed_manifests`, must not be `None`")  # noqa: E501

        self._listed_manifests = listed_manifests

    @property
    def config_blob(self):
        """Gets the config_blob of this ContainerManifestResponse.  # noqa: E501

        Blob that contains configuration for this Manifest  # noqa: E501

        :return: The config_blob of this ContainerManifestResponse.  # noqa: E501
        :rtype: str
        """
        return self._config_blob

    @config_blob.setter
    def config_blob(self, config_blob):
        """Sets the config_blob of this ContainerManifestResponse.

        Blob that contains configuration for this Manifest  # noqa: E501

        :param config_blob: The config_blob of this ContainerManifestResponse.  # noqa: E501
        :type: str
        """

        self._config_blob = config_blob

    @property
    def blobs(self):
        """Gets the blobs of this ContainerManifestResponse.  # noqa: E501

        Blobs that are referenced by this Manifest  # noqa: E501

        :return: The blobs of this ContainerManifestResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._blobs

    @blobs.setter
    def blobs(self, blobs):
        """Sets the blobs of this ContainerManifestResponse.

        Blobs that are referenced by this Manifest  # noqa: E501

        :param blobs: The blobs of this ContainerManifestResponse.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and blobs is None:  # noqa: E501
            raise ValueError("Invalid value for `blobs`, must not be `None`")  # noqa: E501

        self._blobs = blobs

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
        if not isinstance(other, ContainerManifestResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ContainerManifestResponse):
            return True

        return self.to_dict() != other.to_dict()
