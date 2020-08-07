import abc
import builtins
import datetime
import enum
import typing

import jsii
import jsii.compat
import publication

from .._jsii import *

from .. import (
    CfnResource as _CfnResource_7760e8e4,
    Construct as _Construct_f50a3f53,
    IResolvable as _IResolvable_9ceae33e,
    FromCloudFormationOptions as _FromCloudFormationOptions_5f49f6f1,
    ICfnFinder as _ICfnFinder_3b168f30,
    TreeInspector as _TreeInspector_154f5999,
    TagManager as _TagManager_2508893f,
    IInspectable as _IInspectable_051e6ed8,
)


@jsii.implements(_IInspectable_051e6ed8)
class CfnCluster(
    _CfnResource_7760e8e4,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk-experiment.aws_msk.CfnCluster",
):
    """A CloudFormation ``AWS::MSK::Cluster``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html
    cloudformationResource:
    :cloudformationResource:: AWS::MSK::Cluster
    """

    def __init__(
        self,
        scope: _Construct_f50a3f53,
        id: str,
        *,
        broker_node_group_info: typing.Union[
            "BrokerNodeGroupInfoProperty", _IResolvable_9ceae33e
        ],
        cluster_name: str,
        kafka_version: str,
        number_of_broker_nodes: jsii.Number,
        client_authentication: typing.Optional[
            typing.Union["ClientAuthenticationProperty", _IResolvable_9ceae33e]
        ] = None,
        configuration_info: typing.Optional[
            typing.Union["ConfigurationInfoProperty", _IResolvable_9ceae33e]
        ] = None,
        encryption_info: typing.Optional[
            typing.Union["EncryptionInfoProperty", _IResolvable_9ceae33e]
        ] = None,
        enhanced_monitoring: typing.Optional[str] = None,
        logging_info: typing.Optional[
            typing.Union["LoggingInfoProperty", _IResolvable_9ceae33e]
        ] = None,
        open_monitoring: typing.Optional[
            typing.Union["OpenMonitoringProperty", _IResolvable_9ceae33e]
        ] = None,
        tags: typing.Any = None,
    ) -> None:
        """Create a new ``AWS::MSK::Cluster``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param broker_node_group_info: ``AWS::MSK::Cluster.BrokerNodeGroupInfo``.
        :param cluster_name: ``AWS::MSK::Cluster.ClusterName``.
        :param kafka_version: ``AWS::MSK::Cluster.KafkaVersion``.
        :param number_of_broker_nodes: ``AWS::MSK::Cluster.NumberOfBrokerNodes``.
        :param client_authentication: ``AWS::MSK::Cluster.ClientAuthentication``.
        :param configuration_info: ``AWS::MSK::Cluster.ConfigurationInfo``.
        :param encryption_info: ``AWS::MSK::Cluster.EncryptionInfo``.
        :param enhanced_monitoring: ``AWS::MSK::Cluster.EnhancedMonitoring``.
        :param logging_info: ``AWS::MSK::Cluster.LoggingInfo``.
        :param open_monitoring: ``AWS::MSK::Cluster.OpenMonitoring``.
        :param tags: ``AWS::MSK::Cluster.Tags``.
        """
        props = CfnClusterProps(
            broker_node_group_info=broker_node_group_info,
            cluster_name=cluster_name,
            kafka_version=kafka_version,
            number_of_broker_nodes=number_of_broker_nodes,
            client_authentication=client_authentication,
            configuration_info=configuration_info,
            encryption_info=encryption_info,
            enhanced_monitoring=enhanced_monitoring,
            logging_info=logging_info,
            open_monitoring=open_monitoring,
            tags=tags,
        )

        jsii.create(CfnCluster, self, [scope, id, props])

    @jsii.member(jsii_name="fromCloudFormation")
    @builtins.classmethod
    def from_cloud_formation(
        cls,
        scope: _Construct_f50a3f53,
        id: str,
        resource_attributes: typing.Any,
        *,
        finder: _ICfnFinder_3b168f30,
    ) -> "CfnCluster":
        """A factory method that creates a new instance of this class from an object containing the CloudFormation properties of this resource.

        Used in the @aws-cdk/cloudformation-include module.

        :param scope: -
        :param id: -
        :param resource_attributes: -
        :param finder: The finder interface used to resolve references across the template.

        stability
        :stability: experimental
        """
        options = _FromCloudFormationOptions_5f49f6f1(finder=finder)

        return jsii.sinvoke(
            cls, "fromCloudFormation", [scope, id, resource_attributes, options]
        )

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_154f5999) -> None:
        """Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "inspect", [inspector])

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self, props: typing.Mapping[str, typing.Any]
    ) -> typing.Mapping[str, typing.Any]:
        """
        :param props: -
        """
        return jsii.invoke(self, "renderProperties", [props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> str:
        """The CloudFormation resource type name for this resource class."""
        return jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME")

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[str, typing.Any]:
        return jsii.get(self, "cfnProperties")

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_2508893f:
        """``AWS::MSK::Cluster.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html#cfn-msk-cluster-tags
        """
        return jsii.get(self, "tags")

    @builtins.property
    @jsii.member(jsii_name="brokerNodeGroupInfo")
    def broker_node_group_info(
        self,
    ) -> typing.Union["BrokerNodeGroupInfoProperty", _IResolvable_9ceae33e]:
        """``AWS::MSK::Cluster.BrokerNodeGroupInfo``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html#cfn-msk-cluster-brokernodegroupinfo
        """
        return jsii.get(self, "brokerNodeGroupInfo")

    @broker_node_group_info.setter
    def broker_node_group_info(
        self, value: typing.Union["BrokerNodeGroupInfoProperty", _IResolvable_9ceae33e]
    ) -> None:
        jsii.set(self, "brokerNodeGroupInfo", value)

    @builtins.property
    @jsii.member(jsii_name="clusterName")
    def cluster_name(self) -> str:
        """``AWS::MSK::Cluster.ClusterName``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html#cfn-msk-cluster-clustername
        """
        return jsii.get(self, "clusterName")

    @cluster_name.setter
    def cluster_name(self, value: str) -> None:
        jsii.set(self, "clusterName", value)

    @builtins.property
    @jsii.member(jsii_name="kafkaVersion")
    def kafka_version(self) -> str:
        """``AWS::MSK::Cluster.KafkaVersion``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html#cfn-msk-cluster-kafkaversion
        """
        return jsii.get(self, "kafkaVersion")

    @kafka_version.setter
    def kafka_version(self, value: str) -> None:
        jsii.set(self, "kafkaVersion", value)

    @builtins.property
    @jsii.member(jsii_name="numberOfBrokerNodes")
    def number_of_broker_nodes(self) -> jsii.Number:
        """``AWS::MSK::Cluster.NumberOfBrokerNodes``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html#cfn-msk-cluster-numberofbrokernodes
        """
        return jsii.get(self, "numberOfBrokerNodes")

    @number_of_broker_nodes.setter
    def number_of_broker_nodes(self, value: jsii.Number) -> None:
        jsii.set(self, "numberOfBrokerNodes", value)

    @builtins.property
    @jsii.member(jsii_name="clientAuthentication")
    def client_authentication(
        self,
    ) -> typing.Optional[
        typing.Union["ClientAuthenticationProperty", _IResolvable_9ceae33e]
    ]:
        """``AWS::MSK::Cluster.ClientAuthentication``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html#cfn-msk-cluster-clientauthentication
        """
        return jsii.get(self, "clientAuthentication")

    @client_authentication.setter
    def client_authentication(
        self,
        value: typing.Optional[
            typing.Union["ClientAuthenticationProperty", _IResolvable_9ceae33e]
        ],
    ) -> None:
        jsii.set(self, "clientAuthentication", value)

    @builtins.property
    @jsii.member(jsii_name="configurationInfo")
    def configuration_info(
        self,
    ) -> typing.Optional[
        typing.Union["ConfigurationInfoProperty", _IResolvable_9ceae33e]
    ]:
        """``AWS::MSK::Cluster.ConfigurationInfo``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html#cfn-msk-cluster-configurationinfo
        """
        return jsii.get(self, "configurationInfo")

    @configuration_info.setter
    def configuration_info(
        self,
        value: typing.Optional[
            typing.Union["ConfigurationInfoProperty", _IResolvable_9ceae33e]
        ],
    ) -> None:
        jsii.set(self, "configurationInfo", value)

    @builtins.property
    @jsii.member(jsii_name="encryptionInfo")
    def encryption_info(
        self,
    ) -> typing.Optional[typing.Union["EncryptionInfoProperty", _IResolvable_9ceae33e]]:
        """``AWS::MSK::Cluster.EncryptionInfo``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html#cfn-msk-cluster-encryptioninfo
        """
        return jsii.get(self, "encryptionInfo")

    @encryption_info.setter
    def encryption_info(
        self,
        value: typing.Optional[
            typing.Union["EncryptionInfoProperty", _IResolvable_9ceae33e]
        ],
    ) -> None:
        jsii.set(self, "encryptionInfo", value)

    @builtins.property
    @jsii.member(jsii_name="enhancedMonitoring")
    def enhanced_monitoring(self) -> typing.Optional[str]:
        """``AWS::MSK::Cluster.EnhancedMonitoring``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html#cfn-msk-cluster-enhancedmonitoring
        """
        return jsii.get(self, "enhancedMonitoring")

    @enhanced_monitoring.setter
    def enhanced_monitoring(self, value: typing.Optional[str]) -> None:
        jsii.set(self, "enhancedMonitoring", value)

    @builtins.property
    @jsii.member(jsii_name="loggingInfo")
    def logging_info(
        self,
    ) -> typing.Optional[typing.Union["LoggingInfoProperty", _IResolvable_9ceae33e]]:
        """``AWS::MSK::Cluster.LoggingInfo``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html#cfn-msk-cluster-logginginfo
        """
        return jsii.get(self, "loggingInfo")

    @logging_info.setter
    def logging_info(
        self,
        value: typing.Optional[
            typing.Union["LoggingInfoProperty", _IResolvable_9ceae33e]
        ],
    ) -> None:
        jsii.set(self, "loggingInfo", value)

    @builtins.property
    @jsii.member(jsii_name="openMonitoring")
    def open_monitoring(
        self,
    ) -> typing.Optional[typing.Union["OpenMonitoringProperty", _IResolvable_9ceae33e]]:
        """``AWS::MSK::Cluster.OpenMonitoring``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html#cfn-msk-cluster-openmonitoring
        """
        return jsii.get(self, "openMonitoring")

    @open_monitoring.setter
    def open_monitoring(
        self,
        value: typing.Optional[
            typing.Union["OpenMonitoringProperty", _IResolvable_9ceae33e]
        ],
    ) -> None:
        jsii.set(self, "openMonitoring", value)

    @jsii.data_type(
        jsii_type="monocdk-experiment.aws_msk.CfnCluster.BrokerLogsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "cloud_watch_logs": "cloudWatchLogs",
            "firehose": "firehose",
            "s3": "s3",
        },
    )
    class BrokerLogsProperty:
        def __init__(
            self,
            *,
            cloud_watch_logs: typing.Optional[
                typing.Union["CfnCluster.CloudWatchLogsProperty", _IResolvable_9ceae33e]
            ] = None,
            firehose: typing.Optional[
                typing.Union["CfnCluster.FirehoseProperty", _IResolvable_9ceae33e]
            ] = None,
            s3: typing.Optional[
                typing.Union["CfnCluster.S3Property", _IResolvable_9ceae33e]
            ] = None,
        ) -> None:
            """
            :param cloud_watch_logs: ``CfnCluster.BrokerLogsProperty.CloudWatchLogs``.
            :param firehose: ``CfnCluster.BrokerLogsProperty.Firehose``.
            :param s3: ``CfnCluster.BrokerLogsProperty.S3``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-brokerlogs.html
            """
            self._values = {}
            if cloud_watch_logs is not None:
                self._values["cloud_watch_logs"] = cloud_watch_logs
            if firehose is not None:
                self._values["firehose"] = firehose
            if s3 is not None:
                self._values["s3"] = s3

        @builtins.property
        def cloud_watch_logs(
            self,
        ) -> typing.Optional[
            typing.Union["CfnCluster.CloudWatchLogsProperty", _IResolvable_9ceae33e]
        ]:
            """``CfnCluster.BrokerLogsProperty.CloudWatchLogs``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-brokerlogs.html#cfn-msk-cluster-brokerlogs-cloudwatchlogs
            """
            return self._values.get("cloud_watch_logs")

        @builtins.property
        def firehose(
            self,
        ) -> typing.Optional[
            typing.Union["CfnCluster.FirehoseProperty", _IResolvable_9ceae33e]
        ]:
            """``CfnCluster.BrokerLogsProperty.Firehose``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-brokerlogs.html#cfn-msk-cluster-brokerlogs-firehose
            """
            return self._values.get("firehose")

        @builtins.property
        def s3(
            self,
        ) -> typing.Optional[
            typing.Union["CfnCluster.S3Property", _IResolvable_9ceae33e]
        ]:
            """``CfnCluster.BrokerLogsProperty.S3``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-brokerlogs.html#cfn-msk-cluster-brokerlogs-s3
            """
            return self._values.get("s3")

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BrokerLogsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk-experiment.aws_msk.CfnCluster.BrokerNodeGroupInfoProperty",
        jsii_struct_bases=[],
        name_mapping={
            "client_subnets": "clientSubnets",
            "instance_type": "instanceType",
            "broker_az_distribution": "brokerAzDistribution",
            "security_groups": "securityGroups",
            "storage_info": "storageInfo",
        },
    )
    class BrokerNodeGroupInfoProperty:
        def __init__(
            self,
            *,
            client_subnets: typing.List[str],
            instance_type: str,
            broker_az_distribution: typing.Optional[str] = None,
            security_groups: typing.Optional[typing.List[str]] = None,
            storage_info: typing.Optional[
                typing.Union["CfnCluster.StorageInfoProperty", _IResolvable_9ceae33e]
            ] = None,
        ) -> None:
            """
            :param client_subnets: ``CfnCluster.BrokerNodeGroupInfoProperty.ClientSubnets``.
            :param instance_type: ``CfnCluster.BrokerNodeGroupInfoProperty.InstanceType``.
            :param broker_az_distribution: ``CfnCluster.BrokerNodeGroupInfoProperty.BrokerAZDistribution``.
            :param security_groups: ``CfnCluster.BrokerNodeGroupInfoProperty.SecurityGroups``.
            :param storage_info: ``CfnCluster.BrokerNodeGroupInfoProperty.StorageInfo``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-brokernodegroupinfo.html
            """
            self._values = {
                "client_subnets": client_subnets,
                "instance_type": instance_type,
            }
            if broker_az_distribution is not None:
                self._values["broker_az_distribution"] = broker_az_distribution
            if security_groups is not None:
                self._values["security_groups"] = security_groups
            if storage_info is not None:
                self._values["storage_info"] = storage_info

        @builtins.property
        def client_subnets(self) -> typing.List[str]:
            """``CfnCluster.BrokerNodeGroupInfoProperty.ClientSubnets``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-brokernodegroupinfo.html#cfn-msk-cluster-brokernodegroupinfo-clientsubnets
            """
            return self._values.get("client_subnets")

        @builtins.property
        def instance_type(self) -> str:
            """``CfnCluster.BrokerNodeGroupInfoProperty.InstanceType``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-brokernodegroupinfo.html#cfn-msk-cluster-brokernodegroupinfo-instancetype
            """
            return self._values.get("instance_type")

        @builtins.property
        def broker_az_distribution(self) -> typing.Optional[str]:
            """``CfnCluster.BrokerNodeGroupInfoProperty.BrokerAZDistribution``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-brokernodegroupinfo.html#cfn-msk-cluster-brokernodegroupinfo-brokerazdistribution
            """
            return self._values.get("broker_az_distribution")

        @builtins.property
        def security_groups(self) -> typing.Optional[typing.List[str]]:
            """``CfnCluster.BrokerNodeGroupInfoProperty.SecurityGroups``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-brokernodegroupinfo.html#cfn-msk-cluster-brokernodegroupinfo-securitygroups
            """
            return self._values.get("security_groups")

        @builtins.property
        def storage_info(
            self,
        ) -> typing.Optional[
            typing.Union["CfnCluster.StorageInfoProperty", _IResolvable_9ceae33e]
        ]:
            """``CfnCluster.BrokerNodeGroupInfoProperty.StorageInfo``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-brokernodegroupinfo.html#cfn-msk-cluster-brokernodegroupinfo-storageinfo
            """
            return self._values.get("storage_info")

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BrokerNodeGroupInfoProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk-experiment.aws_msk.CfnCluster.ClientAuthenticationProperty",
        jsii_struct_bases=[],
        name_mapping={"tls": "tls"},
    )
    class ClientAuthenticationProperty:
        def __init__(
            self,
            *,
            tls: typing.Optional[
                typing.Union["CfnCluster.TlsProperty", _IResolvable_9ceae33e]
            ] = None,
        ) -> None:
            """
            :param tls: ``CfnCluster.ClientAuthenticationProperty.Tls``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-clientauthentication.html
            """
            self._values = {}
            if tls is not None:
                self._values["tls"] = tls

        @builtins.property
        def tls(
            self,
        ) -> typing.Optional[
            typing.Union["CfnCluster.TlsProperty", _IResolvable_9ceae33e]
        ]:
            """``CfnCluster.ClientAuthenticationProperty.Tls``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-clientauthentication.html#cfn-msk-cluster-clientauthentication-tls
            """
            return self._values.get("tls")

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ClientAuthenticationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk-experiment.aws_msk.CfnCluster.CloudWatchLogsProperty",
        jsii_struct_bases=[],
        name_mapping={"enabled": "enabled", "log_group": "logGroup"},
    )
    class CloudWatchLogsProperty:
        def __init__(
            self,
            *,
            enabled: typing.Union[bool, _IResolvable_9ceae33e],
            log_group: typing.Optional[str] = None,
        ) -> None:
            """
            :param enabled: ``CfnCluster.CloudWatchLogsProperty.Enabled``.
            :param log_group: ``CfnCluster.CloudWatchLogsProperty.LogGroup``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-cloudwatchlogs.html
            """
            self._values = {
                "enabled": enabled,
            }
            if log_group is not None:
                self._values["log_group"] = log_group

        @builtins.property
        def enabled(self) -> typing.Union[bool, _IResolvable_9ceae33e]:
            """``CfnCluster.CloudWatchLogsProperty.Enabled``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-cloudwatchlogs.html#cfn-msk-cluster-cloudwatchlogs-enabled
            """
            return self._values.get("enabled")

        @builtins.property
        def log_group(self) -> typing.Optional[str]:
            """``CfnCluster.CloudWatchLogsProperty.LogGroup``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-cloudwatchlogs.html#cfn-msk-cluster-cloudwatchlogs-loggroup
            """
            return self._values.get("log_group")

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CloudWatchLogsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk-experiment.aws_msk.CfnCluster.ConfigurationInfoProperty",
        jsii_struct_bases=[],
        name_mapping={"arn": "arn", "revision": "revision"},
    )
    class ConfigurationInfoProperty:
        def __init__(self, *, arn: str, revision: jsii.Number) -> None:
            """
            :param arn: ``CfnCluster.ConfigurationInfoProperty.Arn``.
            :param revision: ``CfnCluster.ConfigurationInfoProperty.Revision``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-configurationinfo.html
            """
            self._values = {
                "arn": arn,
                "revision": revision,
            }

        @builtins.property
        def arn(self) -> str:
            """``CfnCluster.ConfigurationInfoProperty.Arn``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-configurationinfo.html#cfn-msk-cluster-configurationinfo-arn
            """
            return self._values.get("arn")

        @builtins.property
        def revision(self) -> jsii.Number:
            """``CfnCluster.ConfigurationInfoProperty.Revision``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-configurationinfo.html#cfn-msk-cluster-configurationinfo-revision
            """
            return self._values.get("revision")

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConfigurationInfoProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk-experiment.aws_msk.CfnCluster.EBSStorageInfoProperty",
        jsii_struct_bases=[],
        name_mapping={"volume_size": "volumeSize"},
    )
    class EBSStorageInfoProperty:
        def __init__(self, *, volume_size: typing.Optional[jsii.Number] = None) -> None:
            """
            :param volume_size: ``CfnCluster.EBSStorageInfoProperty.VolumeSize``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-ebsstorageinfo.html
            """
            self._values = {}
            if volume_size is not None:
                self._values["volume_size"] = volume_size

        @builtins.property
        def volume_size(self) -> typing.Optional[jsii.Number]:
            """``CfnCluster.EBSStorageInfoProperty.VolumeSize``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-ebsstorageinfo.html#cfn-msk-cluster-ebsstorageinfo-volumesize
            """
            return self._values.get("volume_size")

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EBSStorageInfoProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk-experiment.aws_msk.CfnCluster.EncryptionAtRestProperty",
        jsii_struct_bases=[],
        name_mapping={"data_volume_kms_key_id": "dataVolumeKmsKeyId"},
    )
    class EncryptionAtRestProperty:
        def __init__(self, *, data_volume_kms_key_id: str) -> None:
            """
            :param data_volume_kms_key_id: ``CfnCluster.EncryptionAtRestProperty.DataVolumeKMSKeyId``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-encryptionatrest.html
            """
            self._values = {
                "data_volume_kms_key_id": data_volume_kms_key_id,
            }

        @builtins.property
        def data_volume_kms_key_id(self) -> str:
            """``CfnCluster.EncryptionAtRestProperty.DataVolumeKMSKeyId``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-encryptionatrest.html#cfn-msk-cluster-encryptionatrest-datavolumekmskeyid
            """
            return self._values.get("data_volume_kms_key_id")

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EncryptionAtRestProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk-experiment.aws_msk.CfnCluster.EncryptionInTransitProperty",
        jsii_struct_bases=[],
        name_mapping={"client_broker": "clientBroker", "in_cluster": "inCluster"},
    )
    class EncryptionInTransitProperty:
        def __init__(
            self,
            *,
            client_broker: typing.Optional[str] = None,
            in_cluster: typing.Optional[
                typing.Union[bool, _IResolvable_9ceae33e]
            ] = None,
        ) -> None:
            """
            :param client_broker: ``CfnCluster.EncryptionInTransitProperty.ClientBroker``.
            :param in_cluster: ``CfnCluster.EncryptionInTransitProperty.InCluster``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-encryptionintransit.html
            """
            self._values = {}
            if client_broker is not None:
                self._values["client_broker"] = client_broker
            if in_cluster is not None:
                self._values["in_cluster"] = in_cluster

        @builtins.property
        def client_broker(self) -> typing.Optional[str]:
            """``CfnCluster.EncryptionInTransitProperty.ClientBroker``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-encryptionintransit.html#cfn-msk-cluster-encryptionintransit-clientbroker
            """
            return self._values.get("client_broker")

        @builtins.property
        def in_cluster(
            self,
        ) -> typing.Optional[typing.Union[bool, _IResolvable_9ceae33e]]:
            """``CfnCluster.EncryptionInTransitProperty.InCluster``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-encryptionintransit.html#cfn-msk-cluster-encryptionintransit-incluster
            """
            return self._values.get("in_cluster")

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EncryptionInTransitProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk-experiment.aws_msk.CfnCluster.EncryptionInfoProperty",
        jsii_struct_bases=[],
        name_mapping={
            "encryption_at_rest": "encryptionAtRest",
            "encryption_in_transit": "encryptionInTransit",
        },
    )
    class EncryptionInfoProperty:
        def __init__(
            self,
            *,
            encryption_at_rest: typing.Optional[
                typing.Union[
                    "CfnCluster.EncryptionAtRestProperty", _IResolvable_9ceae33e
                ]
            ] = None,
            encryption_in_transit: typing.Optional[
                typing.Union[
                    "CfnCluster.EncryptionInTransitProperty", _IResolvable_9ceae33e
                ]
            ] = None,
        ) -> None:
            """
            :param encryption_at_rest: ``CfnCluster.EncryptionInfoProperty.EncryptionAtRest``.
            :param encryption_in_transit: ``CfnCluster.EncryptionInfoProperty.EncryptionInTransit``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-encryptioninfo.html
            """
            self._values = {}
            if encryption_at_rest is not None:
                self._values["encryption_at_rest"] = encryption_at_rest
            if encryption_in_transit is not None:
                self._values["encryption_in_transit"] = encryption_in_transit

        @builtins.property
        def encryption_at_rest(
            self,
        ) -> typing.Optional[
            typing.Union["CfnCluster.EncryptionAtRestProperty", _IResolvable_9ceae33e]
        ]:
            """``CfnCluster.EncryptionInfoProperty.EncryptionAtRest``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-encryptioninfo.html#cfn-msk-cluster-encryptioninfo-encryptionatrest
            """
            return self._values.get("encryption_at_rest")

        @builtins.property
        def encryption_in_transit(
            self,
        ) -> typing.Optional[
            typing.Union[
                "CfnCluster.EncryptionInTransitProperty", _IResolvable_9ceae33e
            ]
        ]:
            """``CfnCluster.EncryptionInfoProperty.EncryptionInTransit``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-encryptioninfo.html#cfn-msk-cluster-encryptioninfo-encryptionintransit
            """
            return self._values.get("encryption_in_transit")

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EncryptionInfoProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk-experiment.aws_msk.CfnCluster.FirehoseProperty",
        jsii_struct_bases=[],
        name_mapping={"enabled": "enabled", "delivery_stream": "deliveryStream"},
    )
    class FirehoseProperty:
        def __init__(
            self,
            *,
            enabled: typing.Union[bool, _IResolvable_9ceae33e],
            delivery_stream: typing.Optional[str] = None,
        ) -> None:
            """
            :param enabled: ``CfnCluster.FirehoseProperty.Enabled``.
            :param delivery_stream: ``CfnCluster.FirehoseProperty.DeliveryStream``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-firehose.html
            """
            self._values = {
                "enabled": enabled,
            }
            if delivery_stream is not None:
                self._values["delivery_stream"] = delivery_stream

        @builtins.property
        def enabled(self) -> typing.Union[bool, _IResolvable_9ceae33e]:
            """``CfnCluster.FirehoseProperty.Enabled``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-firehose.html#cfn-msk-cluster-firehose-enabled
            """
            return self._values.get("enabled")

        @builtins.property
        def delivery_stream(self) -> typing.Optional[str]:
            """``CfnCluster.FirehoseProperty.DeliveryStream``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-firehose.html#cfn-msk-cluster-firehose-deliverystream
            """
            return self._values.get("delivery_stream")

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FirehoseProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk-experiment.aws_msk.CfnCluster.JmxExporterProperty",
        jsii_struct_bases=[],
        name_mapping={"enabled_in_broker": "enabledInBroker"},
    )
    class JmxExporterProperty:
        def __init__(
            self, *, enabled_in_broker: typing.Union[bool, _IResolvable_9ceae33e]
        ) -> None:
            """
            :param enabled_in_broker: ``CfnCluster.JmxExporterProperty.EnabledInBroker``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-jmxexporter.html
            """
            self._values = {
                "enabled_in_broker": enabled_in_broker,
            }

        @builtins.property
        def enabled_in_broker(self) -> typing.Union[bool, _IResolvable_9ceae33e]:
            """``CfnCluster.JmxExporterProperty.EnabledInBroker``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-jmxexporter.html#cfn-msk-cluster-jmxexporter-enabledinbroker
            """
            return self._values.get("enabled_in_broker")

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "JmxExporterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk-experiment.aws_msk.CfnCluster.LoggingInfoProperty",
        jsii_struct_bases=[],
        name_mapping={"broker_logs": "brokerLogs"},
    )
    class LoggingInfoProperty:
        def __init__(
            self,
            *,
            broker_logs: typing.Union[
                "CfnCluster.BrokerLogsProperty", _IResolvable_9ceae33e
            ],
        ) -> None:
            """
            :param broker_logs: ``CfnCluster.LoggingInfoProperty.BrokerLogs``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-logginginfo.html
            """
            self._values = {
                "broker_logs": broker_logs,
            }

        @builtins.property
        def broker_logs(
            self,
        ) -> typing.Union["CfnCluster.BrokerLogsProperty", _IResolvable_9ceae33e]:
            """``CfnCluster.LoggingInfoProperty.BrokerLogs``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-logginginfo.html#cfn-msk-cluster-logginginfo-brokerlogs
            """
            return self._values.get("broker_logs")

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LoggingInfoProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk-experiment.aws_msk.CfnCluster.NodeExporterProperty",
        jsii_struct_bases=[],
        name_mapping={"enabled_in_broker": "enabledInBroker"},
    )
    class NodeExporterProperty:
        def __init__(
            self, *, enabled_in_broker: typing.Union[bool, _IResolvable_9ceae33e]
        ) -> None:
            """
            :param enabled_in_broker: ``CfnCluster.NodeExporterProperty.EnabledInBroker``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-nodeexporter.html
            """
            self._values = {
                "enabled_in_broker": enabled_in_broker,
            }

        @builtins.property
        def enabled_in_broker(self) -> typing.Union[bool, _IResolvable_9ceae33e]:
            """``CfnCluster.NodeExporterProperty.EnabledInBroker``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-nodeexporter.html#cfn-msk-cluster-nodeexporter-enabledinbroker
            """
            return self._values.get("enabled_in_broker")

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NodeExporterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk-experiment.aws_msk.CfnCluster.OpenMonitoringProperty",
        jsii_struct_bases=[],
        name_mapping={"prometheus": "prometheus"},
    )
    class OpenMonitoringProperty:
        def __init__(
            self,
            *,
            prometheus: typing.Union[
                "CfnCluster.PrometheusProperty", _IResolvable_9ceae33e
            ],
        ) -> None:
            """
            :param prometheus: ``CfnCluster.OpenMonitoringProperty.Prometheus``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-openmonitoring.html
            """
            self._values = {
                "prometheus": prometheus,
            }

        @builtins.property
        def prometheus(
            self,
        ) -> typing.Union["CfnCluster.PrometheusProperty", _IResolvable_9ceae33e]:
            """``CfnCluster.OpenMonitoringProperty.Prometheus``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-openmonitoring.html#cfn-msk-cluster-openmonitoring-prometheus
            """
            return self._values.get("prometheus")

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OpenMonitoringProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk-experiment.aws_msk.CfnCluster.PrometheusProperty",
        jsii_struct_bases=[],
        name_mapping={"jmx_exporter": "jmxExporter", "node_exporter": "nodeExporter"},
    )
    class PrometheusProperty:
        def __init__(
            self,
            *,
            jmx_exporter: typing.Optional[
                typing.Union["CfnCluster.JmxExporterProperty", _IResolvable_9ceae33e]
            ] = None,
            node_exporter: typing.Optional[
                typing.Union["CfnCluster.NodeExporterProperty", _IResolvable_9ceae33e]
            ] = None,
        ) -> None:
            """
            :param jmx_exporter: ``CfnCluster.PrometheusProperty.JmxExporter``.
            :param node_exporter: ``CfnCluster.PrometheusProperty.NodeExporter``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-prometheus.html
            """
            self._values = {}
            if jmx_exporter is not None:
                self._values["jmx_exporter"] = jmx_exporter
            if node_exporter is not None:
                self._values["node_exporter"] = node_exporter

        @builtins.property
        def jmx_exporter(
            self,
        ) -> typing.Optional[
            typing.Union["CfnCluster.JmxExporterProperty", _IResolvable_9ceae33e]
        ]:
            """``CfnCluster.PrometheusProperty.JmxExporter``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-prometheus.html#cfn-msk-cluster-prometheus-jmxexporter
            """
            return self._values.get("jmx_exporter")

        @builtins.property
        def node_exporter(
            self,
        ) -> typing.Optional[
            typing.Union["CfnCluster.NodeExporterProperty", _IResolvable_9ceae33e]
        ]:
            """``CfnCluster.PrometheusProperty.NodeExporter``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-prometheus.html#cfn-msk-cluster-prometheus-nodeexporter
            """
            return self._values.get("node_exporter")

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PrometheusProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk-experiment.aws_msk.CfnCluster.S3Property",
        jsii_struct_bases=[],
        name_mapping={"enabled": "enabled", "bucket": "bucket", "prefix": "prefix"},
    )
    class S3Property:
        def __init__(
            self,
            *,
            enabled: typing.Union[bool, _IResolvable_9ceae33e],
            bucket: typing.Optional[str] = None,
            prefix: typing.Optional[str] = None,
        ) -> None:
            """
            :param enabled: ``CfnCluster.S3Property.Enabled``.
            :param bucket: ``CfnCluster.S3Property.Bucket``.
            :param prefix: ``CfnCluster.S3Property.Prefix``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-s3.html
            """
            self._values = {
                "enabled": enabled,
            }
            if bucket is not None:
                self._values["bucket"] = bucket
            if prefix is not None:
                self._values["prefix"] = prefix

        @builtins.property
        def enabled(self) -> typing.Union[bool, _IResolvable_9ceae33e]:
            """``CfnCluster.S3Property.Enabled``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-s3.html#cfn-msk-cluster-s3-enabled
            """
            return self._values.get("enabled")

        @builtins.property
        def bucket(self) -> typing.Optional[str]:
            """``CfnCluster.S3Property.Bucket``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-s3.html#cfn-msk-cluster-s3-bucket
            """
            return self._values.get("bucket")

        @builtins.property
        def prefix(self) -> typing.Optional[str]:
            """``CfnCluster.S3Property.Prefix``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-s3.html#cfn-msk-cluster-s3-prefix
            """
            return self._values.get("prefix")

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3Property(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk-experiment.aws_msk.CfnCluster.StorageInfoProperty",
        jsii_struct_bases=[],
        name_mapping={"ebs_storage_info": "ebsStorageInfo"},
    )
    class StorageInfoProperty:
        def __init__(
            self,
            *,
            ebs_storage_info: typing.Optional[
                typing.Union["CfnCluster.EBSStorageInfoProperty", _IResolvable_9ceae33e]
            ] = None,
        ) -> None:
            """
            :param ebs_storage_info: ``CfnCluster.StorageInfoProperty.EBSStorageInfo``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-storageinfo.html
            """
            self._values = {}
            if ebs_storage_info is not None:
                self._values["ebs_storage_info"] = ebs_storage_info

        @builtins.property
        def ebs_storage_info(
            self,
        ) -> typing.Optional[
            typing.Union["CfnCluster.EBSStorageInfoProperty", _IResolvable_9ceae33e]
        ]:
            """``CfnCluster.StorageInfoProperty.EBSStorageInfo``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-storageinfo.html#cfn-msk-cluster-storageinfo-ebsstorageinfo
            """
            return self._values.get("ebs_storage_info")

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StorageInfoProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk-experiment.aws_msk.CfnCluster.TlsProperty",
        jsii_struct_bases=[],
        name_mapping={"certificate_authority_arn_list": "certificateAuthorityArnList"},
    )
    class TlsProperty:
        def __init__(
            self,
            *,
            certificate_authority_arn_list: typing.Optional[typing.List[str]] = None,
        ) -> None:
            """
            :param certificate_authority_arn_list: ``CfnCluster.TlsProperty.CertificateAuthorityArnList``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-tls.html
            """
            self._values = {}
            if certificate_authority_arn_list is not None:
                self._values[
                    "certificate_authority_arn_list"
                ] = certificate_authority_arn_list

        @builtins.property
        def certificate_authority_arn_list(self) -> typing.Optional[typing.List[str]]:
            """``CfnCluster.TlsProperty.CertificateAuthorityArnList``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-tls.html#cfn-msk-cluster-tls-certificateauthorityarnlist
            """
            return self._values.get("certificate_authority_arn_list")

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TlsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="monocdk-experiment.aws_msk.CfnClusterProps",
    jsii_struct_bases=[],
    name_mapping={
        "broker_node_group_info": "brokerNodeGroupInfo",
        "cluster_name": "clusterName",
        "kafka_version": "kafkaVersion",
        "number_of_broker_nodes": "numberOfBrokerNodes",
        "client_authentication": "clientAuthentication",
        "configuration_info": "configurationInfo",
        "encryption_info": "encryptionInfo",
        "enhanced_monitoring": "enhancedMonitoring",
        "logging_info": "loggingInfo",
        "open_monitoring": "openMonitoring",
        "tags": "tags",
    },
)
class CfnClusterProps:
    def __init__(
        self,
        *,
        broker_node_group_info: typing.Union[
            "CfnCluster.BrokerNodeGroupInfoProperty", _IResolvable_9ceae33e
        ],
        cluster_name: str,
        kafka_version: str,
        number_of_broker_nodes: jsii.Number,
        client_authentication: typing.Optional[
            typing.Union[
                "CfnCluster.ClientAuthenticationProperty", _IResolvable_9ceae33e
            ]
        ] = None,
        configuration_info: typing.Optional[
            typing.Union["CfnCluster.ConfigurationInfoProperty", _IResolvable_9ceae33e]
        ] = None,
        encryption_info: typing.Optional[
            typing.Union["CfnCluster.EncryptionInfoProperty", _IResolvable_9ceae33e]
        ] = None,
        enhanced_monitoring: typing.Optional[str] = None,
        logging_info: typing.Optional[
            typing.Union["CfnCluster.LoggingInfoProperty", _IResolvable_9ceae33e]
        ] = None,
        open_monitoring: typing.Optional[
            typing.Union["CfnCluster.OpenMonitoringProperty", _IResolvable_9ceae33e]
        ] = None,
        tags: typing.Any = None,
    ) -> None:
        """Properties for defining a ``AWS::MSK::Cluster``.

        :param broker_node_group_info: ``AWS::MSK::Cluster.BrokerNodeGroupInfo``.
        :param cluster_name: ``AWS::MSK::Cluster.ClusterName``.
        :param kafka_version: ``AWS::MSK::Cluster.KafkaVersion``.
        :param number_of_broker_nodes: ``AWS::MSK::Cluster.NumberOfBrokerNodes``.
        :param client_authentication: ``AWS::MSK::Cluster.ClientAuthentication``.
        :param configuration_info: ``AWS::MSK::Cluster.ConfigurationInfo``.
        :param encryption_info: ``AWS::MSK::Cluster.EncryptionInfo``.
        :param enhanced_monitoring: ``AWS::MSK::Cluster.EnhancedMonitoring``.
        :param logging_info: ``AWS::MSK::Cluster.LoggingInfo``.
        :param open_monitoring: ``AWS::MSK::Cluster.OpenMonitoring``.
        :param tags: ``AWS::MSK::Cluster.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html
        """
        self._values = {
            "broker_node_group_info": broker_node_group_info,
            "cluster_name": cluster_name,
            "kafka_version": kafka_version,
            "number_of_broker_nodes": number_of_broker_nodes,
        }
        if client_authentication is not None:
            self._values["client_authentication"] = client_authentication
        if configuration_info is not None:
            self._values["configuration_info"] = configuration_info
        if encryption_info is not None:
            self._values["encryption_info"] = encryption_info
        if enhanced_monitoring is not None:
            self._values["enhanced_monitoring"] = enhanced_monitoring
        if logging_info is not None:
            self._values["logging_info"] = logging_info
        if open_monitoring is not None:
            self._values["open_monitoring"] = open_monitoring
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def broker_node_group_info(
        self,
    ) -> typing.Union["CfnCluster.BrokerNodeGroupInfoProperty", _IResolvable_9ceae33e]:
        """``AWS::MSK::Cluster.BrokerNodeGroupInfo``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html#cfn-msk-cluster-brokernodegroupinfo
        """
        return self._values.get("broker_node_group_info")

    @builtins.property
    def cluster_name(self) -> str:
        """``AWS::MSK::Cluster.ClusterName``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html#cfn-msk-cluster-clustername
        """
        return self._values.get("cluster_name")

    @builtins.property
    def kafka_version(self) -> str:
        """``AWS::MSK::Cluster.KafkaVersion``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html#cfn-msk-cluster-kafkaversion
        """
        return self._values.get("kafka_version")

    @builtins.property
    def number_of_broker_nodes(self) -> jsii.Number:
        """``AWS::MSK::Cluster.NumberOfBrokerNodes``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html#cfn-msk-cluster-numberofbrokernodes
        """
        return self._values.get("number_of_broker_nodes")

    @builtins.property
    def client_authentication(
        self,
    ) -> typing.Optional[
        typing.Union["CfnCluster.ClientAuthenticationProperty", _IResolvable_9ceae33e]
    ]:
        """``AWS::MSK::Cluster.ClientAuthentication``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html#cfn-msk-cluster-clientauthentication
        """
        return self._values.get("client_authentication")

    @builtins.property
    def configuration_info(
        self,
    ) -> typing.Optional[
        typing.Union["CfnCluster.ConfigurationInfoProperty", _IResolvable_9ceae33e]
    ]:
        """``AWS::MSK::Cluster.ConfigurationInfo``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html#cfn-msk-cluster-configurationinfo
        """
        return self._values.get("configuration_info")

    @builtins.property
    def encryption_info(
        self,
    ) -> typing.Optional[
        typing.Union["CfnCluster.EncryptionInfoProperty", _IResolvable_9ceae33e]
    ]:
        """``AWS::MSK::Cluster.EncryptionInfo``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html#cfn-msk-cluster-encryptioninfo
        """
        return self._values.get("encryption_info")

    @builtins.property
    def enhanced_monitoring(self) -> typing.Optional[str]:
        """``AWS::MSK::Cluster.EnhancedMonitoring``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html#cfn-msk-cluster-enhancedmonitoring
        """
        return self._values.get("enhanced_monitoring")

    @builtins.property
    def logging_info(
        self,
    ) -> typing.Optional[
        typing.Union["CfnCluster.LoggingInfoProperty", _IResolvable_9ceae33e]
    ]:
        """``AWS::MSK::Cluster.LoggingInfo``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html#cfn-msk-cluster-logginginfo
        """
        return self._values.get("logging_info")

    @builtins.property
    def open_monitoring(
        self,
    ) -> typing.Optional[
        typing.Union["CfnCluster.OpenMonitoringProperty", _IResolvable_9ceae33e]
    ]:
        """``AWS::MSK::Cluster.OpenMonitoring``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html#cfn-msk-cluster-openmonitoring
        """
        return self._values.get("open_monitoring")

    @builtins.property
    def tags(self) -> typing.Any:
        """``AWS::MSK::Cluster.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html#cfn-msk-cluster-tags
        """
        return self._values.get("tags")

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnClusterProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnCluster",
    "CfnClusterProps",
]

publication.publish()
