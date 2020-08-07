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
    CfnTag as _CfnTag_b4661f1a,
    FromCloudFormationOptions as _FromCloudFormationOptions_5f49f6f1,
    ICfnFinder as _ICfnFinder_3b168f30,
    TreeInspector as _TreeInspector_154f5999,
    TagManager as _TagManager_2508893f,
    IInspectable as _IInspectable_051e6ed8,
)


@jsii.implements(_IInspectable_051e6ed8)
class CfnLedger(
    _CfnResource_7760e8e4,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk-experiment.aws_qldb.CfnLedger",
):
    """A CloudFormation ``AWS::QLDB::Ledger``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-ledger.html
    cloudformationResource:
    :cloudformationResource:: AWS::QLDB::Ledger
    """

    def __init__(
        self,
        scope: _Construct_f50a3f53,
        id: str,
        *,
        permissions_mode: str,
        deletion_protection: typing.Optional[
            typing.Union[bool, _IResolvable_9ceae33e]
        ] = None,
        name: typing.Optional[str] = None,
        tags: typing.Optional[typing.List[_CfnTag_b4661f1a]] = None,
    ) -> None:
        """Create a new ``AWS::QLDB::Ledger``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param permissions_mode: ``AWS::QLDB::Ledger.PermissionsMode``.
        :param deletion_protection: ``AWS::QLDB::Ledger.DeletionProtection``.
        :param name: ``AWS::QLDB::Ledger.Name``.
        :param tags: ``AWS::QLDB::Ledger.Tags``.
        """
        props = CfnLedgerProps(
            permissions_mode=permissions_mode,
            deletion_protection=deletion_protection,
            name=name,
            tags=tags,
        )

        jsii.create(CfnLedger, self, [scope, id, props])

    @jsii.member(jsii_name="fromCloudFormation")
    @builtins.classmethod
    def from_cloud_formation(
        cls,
        scope: _Construct_f50a3f53,
        id: str,
        resource_attributes: typing.Any,
        *,
        finder: _ICfnFinder_3b168f30,
    ) -> "CfnLedger":
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
        """``AWS::QLDB::Ledger.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-ledger.html#cfn-qldb-ledger-tags
        """
        return jsii.get(self, "tags")

    @builtins.property
    @jsii.member(jsii_name="permissionsMode")
    def permissions_mode(self) -> str:
        """``AWS::QLDB::Ledger.PermissionsMode``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-ledger.html#cfn-qldb-ledger-permissionsmode
        """
        return jsii.get(self, "permissionsMode")

    @permissions_mode.setter
    def permissions_mode(self, value: str) -> None:
        jsii.set(self, "permissionsMode", value)

    @builtins.property
    @jsii.member(jsii_name="deletionProtection")
    def deletion_protection(
        self,
    ) -> typing.Optional[typing.Union[bool, _IResolvable_9ceae33e]]:
        """``AWS::QLDB::Ledger.DeletionProtection``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-ledger.html#cfn-qldb-ledger-deletionprotection
        """
        return jsii.get(self, "deletionProtection")

    @deletion_protection.setter
    def deletion_protection(
        self, value: typing.Optional[typing.Union[bool, _IResolvable_9ceae33e]]
    ) -> None:
        jsii.set(self, "deletionProtection", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[str]:
        """``AWS::QLDB::Ledger.Name``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-ledger.html#cfn-qldb-ledger-name
        """
        return jsii.get(self, "name")

    @name.setter
    def name(self, value: typing.Optional[str]) -> None:
        jsii.set(self, "name", value)


@jsii.data_type(
    jsii_type="monocdk-experiment.aws_qldb.CfnLedgerProps",
    jsii_struct_bases=[],
    name_mapping={
        "permissions_mode": "permissionsMode",
        "deletion_protection": "deletionProtection",
        "name": "name",
        "tags": "tags",
    },
)
class CfnLedgerProps:
    def __init__(
        self,
        *,
        permissions_mode: str,
        deletion_protection: typing.Optional[
            typing.Union[bool, _IResolvable_9ceae33e]
        ] = None,
        name: typing.Optional[str] = None,
        tags: typing.Optional[typing.List[_CfnTag_b4661f1a]] = None,
    ) -> None:
        """Properties for defining a ``AWS::QLDB::Ledger``.

        :param permissions_mode: ``AWS::QLDB::Ledger.PermissionsMode``.
        :param deletion_protection: ``AWS::QLDB::Ledger.DeletionProtection``.
        :param name: ``AWS::QLDB::Ledger.Name``.
        :param tags: ``AWS::QLDB::Ledger.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-ledger.html
        """
        self._values = {
            "permissions_mode": permissions_mode,
        }
        if deletion_protection is not None:
            self._values["deletion_protection"] = deletion_protection
        if name is not None:
            self._values["name"] = name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def permissions_mode(self) -> str:
        """``AWS::QLDB::Ledger.PermissionsMode``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-ledger.html#cfn-qldb-ledger-permissionsmode
        """
        return self._values.get("permissions_mode")

    @builtins.property
    def deletion_protection(
        self,
    ) -> typing.Optional[typing.Union[bool, _IResolvable_9ceae33e]]:
        """``AWS::QLDB::Ledger.DeletionProtection``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-ledger.html#cfn-qldb-ledger-deletionprotection
        """
        return self._values.get("deletion_protection")

    @builtins.property
    def name(self) -> typing.Optional[str]:
        """``AWS::QLDB::Ledger.Name``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-ledger.html#cfn-qldb-ledger-name
        """
        return self._values.get("name")

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_b4661f1a]]:
        """``AWS::QLDB::Ledger.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-ledger.html#cfn-qldb-ledger-tags
        """
        return self._values.get("tags")

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLedgerProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_051e6ed8)
class CfnStream(
    _CfnResource_7760e8e4,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk-experiment.aws_qldb.CfnStream",
):
    """A CloudFormation ``AWS::QLDB::Stream``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-stream.html
    cloudformationResource:
    :cloudformationResource:: AWS::QLDB::Stream
    """

    def __init__(
        self,
        scope: _Construct_f50a3f53,
        id: str,
        *,
        inclusive_start_time: str,
        kinesis_configuration: typing.Union[
            "KinesisConfigurationProperty", _IResolvable_9ceae33e
        ],
        ledger_name: str,
        role_arn: str,
        stream_name: str,
        exclusive_end_time: typing.Optional[str] = None,
        tags: typing.Optional[typing.List[_CfnTag_b4661f1a]] = None,
    ) -> None:
        """Create a new ``AWS::QLDB::Stream``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param inclusive_start_time: ``AWS::QLDB::Stream.InclusiveStartTime``.
        :param kinesis_configuration: ``AWS::QLDB::Stream.KinesisConfiguration``.
        :param ledger_name: ``AWS::QLDB::Stream.LedgerName``.
        :param role_arn: ``AWS::QLDB::Stream.RoleArn``.
        :param stream_name: ``AWS::QLDB::Stream.StreamName``.
        :param exclusive_end_time: ``AWS::QLDB::Stream.ExclusiveEndTime``.
        :param tags: ``AWS::QLDB::Stream.Tags``.
        """
        props = CfnStreamProps(
            inclusive_start_time=inclusive_start_time,
            kinesis_configuration=kinesis_configuration,
            ledger_name=ledger_name,
            role_arn=role_arn,
            stream_name=stream_name,
            exclusive_end_time=exclusive_end_time,
            tags=tags,
        )

        jsii.create(CfnStream, self, [scope, id, props])

    @jsii.member(jsii_name="fromCloudFormation")
    @builtins.classmethod
    def from_cloud_formation(
        cls,
        scope: _Construct_f50a3f53,
        id: str,
        resource_attributes: typing.Any,
        *,
        finder: _ICfnFinder_3b168f30,
    ) -> "CfnStream":
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
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> str:
        """
        cloudformationAttribute:
        :cloudformationAttribute:: Arn
        """
        return jsii.get(self, "attrArn")

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> str:
        """
        cloudformationAttribute:
        :cloudformationAttribute:: Id
        """
        return jsii.get(self, "attrId")

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[str, typing.Any]:
        return jsii.get(self, "cfnProperties")

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_2508893f:
        """``AWS::QLDB::Stream.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-stream.html#cfn-qldb-stream-tags
        """
        return jsii.get(self, "tags")

    @builtins.property
    @jsii.member(jsii_name="inclusiveStartTime")
    def inclusive_start_time(self) -> str:
        """``AWS::QLDB::Stream.InclusiveStartTime``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-stream.html#cfn-qldb-stream-inclusivestarttime
        """
        return jsii.get(self, "inclusiveStartTime")

    @inclusive_start_time.setter
    def inclusive_start_time(self, value: str) -> None:
        jsii.set(self, "inclusiveStartTime", value)

    @builtins.property
    @jsii.member(jsii_name="kinesisConfiguration")
    def kinesis_configuration(
        self,
    ) -> typing.Union["KinesisConfigurationProperty", _IResolvable_9ceae33e]:
        """``AWS::QLDB::Stream.KinesisConfiguration``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-stream.html#cfn-qldb-stream-kinesisconfiguration
        """
        return jsii.get(self, "kinesisConfiguration")

    @kinesis_configuration.setter
    def kinesis_configuration(
        self, value: typing.Union["KinesisConfigurationProperty", _IResolvable_9ceae33e]
    ) -> None:
        jsii.set(self, "kinesisConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="ledgerName")
    def ledger_name(self) -> str:
        """``AWS::QLDB::Stream.LedgerName``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-stream.html#cfn-qldb-stream-ledgername
        """
        return jsii.get(self, "ledgerName")

    @ledger_name.setter
    def ledger_name(self, value: str) -> None:
        jsii.set(self, "ledgerName", value)

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> str:
        """``AWS::QLDB::Stream.RoleArn``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-stream.html#cfn-qldb-stream-rolearn
        """
        return jsii.get(self, "roleArn")

    @role_arn.setter
    def role_arn(self, value: str) -> None:
        jsii.set(self, "roleArn", value)

    @builtins.property
    @jsii.member(jsii_name="streamName")
    def stream_name(self) -> str:
        """``AWS::QLDB::Stream.StreamName``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-stream.html#cfn-qldb-stream-streamname
        """
        return jsii.get(self, "streamName")

    @stream_name.setter
    def stream_name(self, value: str) -> None:
        jsii.set(self, "streamName", value)

    @builtins.property
    @jsii.member(jsii_name="exclusiveEndTime")
    def exclusive_end_time(self) -> typing.Optional[str]:
        """``AWS::QLDB::Stream.ExclusiveEndTime``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-stream.html#cfn-qldb-stream-exclusiveendtime
        """
        return jsii.get(self, "exclusiveEndTime")

    @exclusive_end_time.setter
    def exclusive_end_time(self, value: typing.Optional[str]) -> None:
        jsii.set(self, "exclusiveEndTime", value)

    @jsii.data_type(
        jsii_type="monocdk-experiment.aws_qldb.CfnStream.KinesisConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "aggregation_enabled": "aggregationEnabled",
            "stream_arn": "streamArn",
        },
    )
    class KinesisConfigurationProperty:
        def __init__(
            self,
            *,
            aggregation_enabled: typing.Optional[
                typing.Union[bool, _IResolvable_9ceae33e]
            ] = None,
            stream_arn: typing.Optional[str] = None,
        ) -> None:
            """
            :param aggregation_enabled: ``CfnStream.KinesisConfigurationProperty.AggregationEnabled``.
            :param stream_arn: ``CfnStream.KinesisConfigurationProperty.StreamArn``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qldb-stream-kinesisconfiguration.html
            """
            self._values = {}
            if aggregation_enabled is not None:
                self._values["aggregation_enabled"] = aggregation_enabled
            if stream_arn is not None:
                self._values["stream_arn"] = stream_arn

        @builtins.property
        def aggregation_enabled(
            self,
        ) -> typing.Optional[typing.Union[bool, _IResolvable_9ceae33e]]:
            """``CfnStream.KinesisConfigurationProperty.AggregationEnabled``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qldb-stream-kinesisconfiguration.html#cfn-qldb-stream-kinesisconfiguration-aggregationenabled
            """
            return self._values.get("aggregation_enabled")

        @builtins.property
        def stream_arn(self) -> typing.Optional[str]:
            """``CfnStream.KinesisConfigurationProperty.StreamArn``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qldb-stream-kinesisconfiguration.html#cfn-qldb-stream-kinesisconfiguration-streamarn
            """
            return self._values.get("stream_arn")

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "KinesisConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="monocdk-experiment.aws_qldb.CfnStreamProps",
    jsii_struct_bases=[],
    name_mapping={
        "inclusive_start_time": "inclusiveStartTime",
        "kinesis_configuration": "kinesisConfiguration",
        "ledger_name": "ledgerName",
        "role_arn": "roleArn",
        "stream_name": "streamName",
        "exclusive_end_time": "exclusiveEndTime",
        "tags": "tags",
    },
)
class CfnStreamProps:
    def __init__(
        self,
        *,
        inclusive_start_time: str,
        kinesis_configuration: typing.Union[
            "CfnStream.KinesisConfigurationProperty", _IResolvable_9ceae33e
        ],
        ledger_name: str,
        role_arn: str,
        stream_name: str,
        exclusive_end_time: typing.Optional[str] = None,
        tags: typing.Optional[typing.List[_CfnTag_b4661f1a]] = None,
    ) -> None:
        """Properties for defining a ``AWS::QLDB::Stream``.

        :param inclusive_start_time: ``AWS::QLDB::Stream.InclusiveStartTime``.
        :param kinesis_configuration: ``AWS::QLDB::Stream.KinesisConfiguration``.
        :param ledger_name: ``AWS::QLDB::Stream.LedgerName``.
        :param role_arn: ``AWS::QLDB::Stream.RoleArn``.
        :param stream_name: ``AWS::QLDB::Stream.StreamName``.
        :param exclusive_end_time: ``AWS::QLDB::Stream.ExclusiveEndTime``.
        :param tags: ``AWS::QLDB::Stream.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-stream.html
        """
        self._values = {
            "inclusive_start_time": inclusive_start_time,
            "kinesis_configuration": kinesis_configuration,
            "ledger_name": ledger_name,
            "role_arn": role_arn,
            "stream_name": stream_name,
        }
        if exclusive_end_time is not None:
            self._values["exclusive_end_time"] = exclusive_end_time
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def inclusive_start_time(self) -> str:
        """``AWS::QLDB::Stream.InclusiveStartTime``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-stream.html#cfn-qldb-stream-inclusivestarttime
        """
        return self._values.get("inclusive_start_time")

    @builtins.property
    def kinesis_configuration(
        self,
    ) -> typing.Union["CfnStream.KinesisConfigurationProperty", _IResolvable_9ceae33e]:
        """``AWS::QLDB::Stream.KinesisConfiguration``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-stream.html#cfn-qldb-stream-kinesisconfiguration
        """
        return self._values.get("kinesis_configuration")

    @builtins.property
    def ledger_name(self) -> str:
        """``AWS::QLDB::Stream.LedgerName``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-stream.html#cfn-qldb-stream-ledgername
        """
        return self._values.get("ledger_name")

    @builtins.property
    def role_arn(self) -> str:
        """``AWS::QLDB::Stream.RoleArn``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-stream.html#cfn-qldb-stream-rolearn
        """
        return self._values.get("role_arn")

    @builtins.property
    def stream_name(self) -> str:
        """``AWS::QLDB::Stream.StreamName``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-stream.html#cfn-qldb-stream-streamname
        """
        return self._values.get("stream_name")

    @builtins.property
    def exclusive_end_time(self) -> typing.Optional[str]:
        """``AWS::QLDB::Stream.ExclusiveEndTime``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-stream.html#cfn-qldb-stream-exclusiveendtime
        """
        return self._values.get("exclusive_end_time")

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_b4661f1a]]:
        """``AWS::QLDB::Stream.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-stream.html#cfn-qldb-stream-tags
        """
        return self._values.get("tags")

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnStreamProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnLedger",
    "CfnLedgerProps",
    "CfnStream",
    "CfnStreamProps",
]

publication.publish()
