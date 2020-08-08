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

from pulpcore.client.pulp_deb.configuration import Configuration


class DebAptRemote(object):
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
        'name': 'str',
        'url': 'str',
        'ca_cert': 'str',
        'client_cert': 'str',
        'client_key': 'str',
        'tls_validation': 'bool',
        'proxy_url': 'str',
        'username': 'str',
        'password': 'str',
        'download_concurrency': 'int',
        'policy': 'PolicyEnum',
        'distributions': 'str',
        'components': 'str',
        'architectures': 'str',
        'sync_sources': 'bool',
        'sync_udebs': 'bool',
        'sync_installer': 'bool',
        'gpgkey': 'str'
    }

    attribute_map = {
        'name': 'name',
        'url': 'url',
        'ca_cert': 'ca_cert',
        'client_cert': 'client_cert',
        'client_key': 'client_key',
        'tls_validation': 'tls_validation',
        'proxy_url': 'proxy_url',
        'username': 'username',
        'password': 'password',
        'download_concurrency': 'download_concurrency',
        'policy': 'policy',
        'distributions': 'distributions',
        'components': 'components',
        'architectures': 'architectures',
        'sync_sources': 'sync_sources',
        'sync_udebs': 'sync_udebs',
        'sync_installer': 'sync_installer',
        'gpgkey': 'gpgkey'
    }

    def __init__(self, name=None, url=None, ca_cert=None, client_cert=None, client_key=None, tls_validation=None, proxy_url=None, username=None, password=None, download_concurrency=None, policy=None, distributions=None, components=None, architectures=None, sync_sources=None, sync_udebs=None, sync_installer=None, gpgkey=None, local_vars_configuration=None):  # noqa: E501
        """DebAptRemote - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._url = None
        self._ca_cert = None
        self._client_cert = None
        self._client_key = None
        self._tls_validation = None
        self._proxy_url = None
        self._username = None
        self._password = None
        self._download_concurrency = None
        self._policy = None
        self._distributions = None
        self._components = None
        self._architectures = None
        self._sync_sources = None
        self._sync_udebs = None
        self._sync_installer = None
        self._gpgkey = None
        self.discriminator = None

        self.name = name
        self.url = url
        self.ca_cert = ca_cert
        self.client_cert = client_cert
        self.client_key = client_key
        if tls_validation is not None:
            self.tls_validation = tls_validation
        self.proxy_url = proxy_url
        self.username = username
        self.password = password
        if download_concurrency is not None:
            self.download_concurrency = download_concurrency
        if policy is not None:
            self.policy = policy
        self.distributions = distributions
        self.components = components
        self.architectures = architectures
        if sync_sources is not None:
            self.sync_sources = sync_sources
        if sync_udebs is not None:
            self.sync_udebs = sync_udebs
        if sync_installer is not None:
            self.sync_installer = sync_installer
        self.gpgkey = gpgkey

    @property
    def name(self):
        """Gets the name of this DebAptRemote.  # noqa: E501

        A unique name for this remote.  # noqa: E501

        :return: The name of this DebAptRemote.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DebAptRemote.

        A unique name for this remote.  # noqa: E501

        :param name: The name of this DebAptRemote.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def url(self):
        """Gets the url of this DebAptRemote.  # noqa: E501

        The URL of an external content source.  # noqa: E501

        :return: The url of this DebAptRemote.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this DebAptRemote.

        The URL of an external content source.  # noqa: E501

        :param url: The url of this DebAptRemote.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and url is None:  # noqa: E501
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

    @property
    def ca_cert(self):
        """Gets the ca_cert of this DebAptRemote.  # noqa: E501

        A PEM encoded CA certificate used to validate the server certificate presented by the remote server.  # noqa: E501

        :return: The ca_cert of this DebAptRemote.  # noqa: E501
        :rtype: str
        """
        return self._ca_cert

    @ca_cert.setter
    def ca_cert(self, ca_cert):
        """Sets the ca_cert of this DebAptRemote.

        A PEM encoded CA certificate used to validate the server certificate presented by the remote server.  # noqa: E501

        :param ca_cert: The ca_cert of this DebAptRemote.  # noqa: E501
        :type: str
        """

        self._ca_cert = ca_cert

    @property
    def client_cert(self):
        """Gets the client_cert of this DebAptRemote.  # noqa: E501

        A PEM encoded client certificate used for authentication.  # noqa: E501

        :return: The client_cert of this DebAptRemote.  # noqa: E501
        :rtype: str
        """
        return self._client_cert

    @client_cert.setter
    def client_cert(self, client_cert):
        """Sets the client_cert of this DebAptRemote.

        A PEM encoded client certificate used for authentication.  # noqa: E501

        :param client_cert: The client_cert of this DebAptRemote.  # noqa: E501
        :type: str
        """

        self._client_cert = client_cert

    @property
    def client_key(self):
        """Gets the client_key of this DebAptRemote.  # noqa: E501

        A PEM encoded private key used for authentication.  # noqa: E501

        :return: The client_key of this DebAptRemote.  # noqa: E501
        :rtype: str
        """
        return self._client_key

    @client_key.setter
    def client_key(self, client_key):
        """Sets the client_key of this DebAptRemote.

        A PEM encoded private key used for authentication.  # noqa: E501

        :param client_key: The client_key of this DebAptRemote.  # noqa: E501
        :type: str
        """

        self._client_key = client_key

    @property
    def tls_validation(self):
        """Gets the tls_validation of this DebAptRemote.  # noqa: E501

        If True, TLS peer validation must be performed.  # noqa: E501

        :return: The tls_validation of this DebAptRemote.  # noqa: E501
        :rtype: bool
        """
        return self._tls_validation

    @tls_validation.setter
    def tls_validation(self, tls_validation):
        """Sets the tls_validation of this DebAptRemote.

        If True, TLS peer validation must be performed.  # noqa: E501

        :param tls_validation: The tls_validation of this DebAptRemote.  # noqa: E501
        :type: bool
        """

        self._tls_validation = tls_validation

    @property
    def proxy_url(self):
        """Gets the proxy_url of this DebAptRemote.  # noqa: E501

        The proxy URL. Format: scheme://user:password@host:port  # noqa: E501

        :return: The proxy_url of this DebAptRemote.  # noqa: E501
        :rtype: str
        """
        return self._proxy_url

    @proxy_url.setter
    def proxy_url(self, proxy_url):
        """Sets the proxy_url of this DebAptRemote.

        The proxy URL. Format: scheme://user:password@host:port  # noqa: E501

        :param proxy_url: The proxy_url of this DebAptRemote.  # noqa: E501
        :type: str
        """

        self._proxy_url = proxy_url

    @property
    def username(self):
        """Gets the username of this DebAptRemote.  # noqa: E501

        The username to be used for authentication when syncing.  # noqa: E501

        :return: The username of this DebAptRemote.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this DebAptRemote.

        The username to be used for authentication when syncing.  # noqa: E501

        :param username: The username of this DebAptRemote.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def password(self):
        """Gets the password of this DebAptRemote.  # noqa: E501

        The password to be used for authentication when syncing.  # noqa: E501

        :return: The password of this DebAptRemote.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this DebAptRemote.

        The password to be used for authentication when syncing.  # noqa: E501

        :param password: The password of this DebAptRemote.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def download_concurrency(self):
        """Gets the download_concurrency of this DebAptRemote.  # noqa: E501

        Total number of simultaneous connections.  # noqa: E501

        :return: The download_concurrency of this DebAptRemote.  # noqa: E501
        :rtype: int
        """
        return self._download_concurrency

    @download_concurrency.setter
    def download_concurrency(self, download_concurrency):
        """Sets the download_concurrency of this DebAptRemote.

        Total number of simultaneous connections.  # noqa: E501

        :param download_concurrency: The download_concurrency of this DebAptRemote.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                download_concurrency is not None and download_concurrency < 1):  # noqa: E501
            raise ValueError("Invalid value for `download_concurrency`, must be a value greater than or equal to `1`")  # noqa: E501

        self._download_concurrency = download_concurrency

    @property
    def policy(self):
        """Gets the policy of this DebAptRemote.  # noqa: E501

        The policy to use when downloading content. The possible values include: 'immediate', 'on_demand', and 'streamed'. 'immediate' is the default.  # noqa: E501

        :return: The policy of this DebAptRemote.  # noqa: E501
        :rtype: PolicyEnum
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        """Sets the policy of this DebAptRemote.

        The policy to use when downloading content. The possible values include: 'immediate', 'on_demand', and 'streamed'. 'immediate' is the default.  # noqa: E501

        :param policy: The policy of this DebAptRemote.  # noqa: E501
        :type: PolicyEnum
        """

        self._policy = policy

    @property
    def distributions(self):
        """Gets the distributions of this DebAptRemote.  # noqa: E501

        Whitespace separated list of distributions to sync  # noqa: E501

        :return: The distributions of this DebAptRemote.  # noqa: E501
        :rtype: str
        """
        return self._distributions

    @distributions.setter
    def distributions(self, distributions):
        """Sets the distributions of this DebAptRemote.

        Whitespace separated list of distributions to sync  # noqa: E501

        :param distributions: The distributions of this DebAptRemote.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and distributions is None:  # noqa: E501
            raise ValueError("Invalid value for `distributions`, must not be `None`")  # noqa: E501

        self._distributions = distributions

    @property
    def components(self):
        """Gets the components of this DebAptRemote.  # noqa: E501

        Whitespace separatet list of components to sync  # noqa: E501

        :return: The components of this DebAptRemote.  # noqa: E501
        :rtype: str
        """
        return self._components

    @components.setter
    def components(self, components):
        """Sets the components of this DebAptRemote.

        Whitespace separatet list of components to sync  # noqa: E501

        :param components: The components of this DebAptRemote.  # noqa: E501
        :type: str
        """

        self._components = components

    @property
    def architectures(self):
        """Gets the architectures of this DebAptRemote.  # noqa: E501

        Whitespace separated list of architectures to sync  # noqa: E501

        :return: The architectures of this DebAptRemote.  # noqa: E501
        :rtype: str
        """
        return self._architectures

    @architectures.setter
    def architectures(self, architectures):
        """Sets the architectures of this DebAptRemote.

        Whitespace separated list of architectures to sync  # noqa: E501

        :param architectures: The architectures of this DebAptRemote.  # noqa: E501
        :type: str
        """

        self._architectures = architectures

    @property
    def sync_sources(self):
        """Gets the sync_sources of this DebAptRemote.  # noqa: E501

        Sync source packages  # noqa: E501

        :return: The sync_sources of this DebAptRemote.  # noqa: E501
        :rtype: bool
        """
        return self._sync_sources

    @sync_sources.setter
    def sync_sources(self, sync_sources):
        """Sets the sync_sources of this DebAptRemote.

        Sync source packages  # noqa: E501

        :param sync_sources: The sync_sources of this DebAptRemote.  # noqa: E501
        :type: bool
        """

        self._sync_sources = sync_sources

    @property
    def sync_udebs(self):
        """Gets the sync_udebs of this DebAptRemote.  # noqa: E501

        Sync installer packages  # noqa: E501

        :return: The sync_udebs of this DebAptRemote.  # noqa: E501
        :rtype: bool
        """
        return self._sync_udebs

    @sync_udebs.setter
    def sync_udebs(self, sync_udebs):
        """Sets the sync_udebs of this DebAptRemote.

        Sync installer packages  # noqa: E501

        :param sync_udebs: The sync_udebs of this DebAptRemote.  # noqa: E501
        :type: bool
        """

        self._sync_udebs = sync_udebs

    @property
    def sync_installer(self):
        """Gets the sync_installer of this DebAptRemote.  # noqa: E501

        Sync installer files  # noqa: E501

        :return: The sync_installer of this DebAptRemote.  # noqa: E501
        :rtype: bool
        """
        return self._sync_installer

    @sync_installer.setter
    def sync_installer(self, sync_installer):
        """Sets the sync_installer of this DebAptRemote.

        Sync installer files  # noqa: E501

        :param sync_installer: The sync_installer of this DebAptRemote.  # noqa: E501
        :type: bool
        """

        self._sync_installer = sync_installer

    @property
    def gpgkey(self):
        """Gets the gpgkey of this DebAptRemote.  # noqa: E501

        Gpg public key to verify origin releases against  # noqa: E501

        :return: The gpgkey of this DebAptRemote.  # noqa: E501
        :rtype: str
        """
        return self._gpgkey

    @gpgkey.setter
    def gpgkey(self, gpgkey):
        """Sets the gpgkey of this DebAptRemote.

        Gpg public key to verify origin releases against  # noqa: E501

        :param gpgkey: The gpgkey of this DebAptRemote.  # noqa: E501
        :type: str
        """

        self._gpgkey = gpgkey

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
        if not isinstance(other, DebAptRemote):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DebAptRemote):
            return True

        return self.to_dict() != other.to_dict()
