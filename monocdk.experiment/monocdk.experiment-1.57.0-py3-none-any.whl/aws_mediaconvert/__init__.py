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
class CfnJobTemplate(
    _CfnResource_7760e8e4,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk-experiment.aws_mediaconvert.CfnJobTemplate",
):
    """A CloudFormation ``AWS::MediaConvert::JobTemplate``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-jobtemplate.html
    cloudformationResource:
    :cloudformationResource:: AWS::MediaConvert::JobTemplate
    """

    def __init__(
        self,
        scope: _Construct_f50a3f53,
        id: str,
        *,
        settings_json: typing.Any,
        acceleration_settings: typing.Optional[
            typing.Union["AccelerationSettingsProperty", _IResolvable_9ceae33e]
        ] = None,
        category: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        hop_destinations: typing.Optional[
            typing.Union[
                _IResolvable_9ceae33e,
                typing.List[
                    typing.Union["HopDestinationProperty", _IResolvable_9ceae33e]
                ],
            ]
        ] = None,
        name: typing.Optional[str] = None,
        priority: typing.Optional[jsii.Number] = None,
        queue: typing.Optional[str] = None,
        status_update_interval: typing.Optional[str] = None,
        tags: typing.Any = None,
    ) -> None:
        """Create a new ``AWS::MediaConvert::JobTemplate``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param settings_json: ``AWS::MediaConvert::JobTemplate.SettingsJson``.
        :param acceleration_settings: ``AWS::MediaConvert::JobTemplate.AccelerationSettings``.
        :param category: ``AWS::MediaConvert::JobTemplate.Category``.
        :param description: ``AWS::MediaConvert::JobTemplate.Description``.
        :param hop_destinations: ``AWS::MediaConvert::JobTemplate.HopDestinations``.
        :param name: ``AWS::MediaConvert::JobTemplate.Name``.
        :param priority: ``AWS::MediaConvert::JobTemplate.Priority``.
        :param queue: ``AWS::MediaConvert::JobTemplate.Queue``.
        :param status_update_interval: ``AWS::MediaConvert::JobTemplate.StatusUpdateInterval``.
        :param tags: ``AWS::MediaConvert::JobTemplate.Tags``.
        """
        props = CfnJobTemplateProps(
            settings_json=settings_json,
            acceleration_settings=acceleration_settings,
            category=category,
            description=description,
            hop_destinations=hop_destinations,
            name=name,
            priority=priority,
            queue=queue,
            status_update_interval=status_update_interval,
            tags=tags,
        )

        jsii.create(CfnJobTemplate, self, [scope, id, props])

    @jsii.member(jsii_name="fromCloudFormation")
    @builtins.classmethod
    def from_cloud_formation(
        cls,
        scope: _Construct_f50a3f53,
        id: str,
        resource_attributes: typing.Any,
        *,
        finder: _ICfnFinder_3b168f30,
    ) -> "CfnJobTemplate":
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
    @jsii.member(jsii_name="attrName")
    def attr_name(self) -> str:
        """
        cloudformationAttribute:
        :cloudformationAttribute:: Name
        """
        return jsii.get(self, "attrName")

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[str, typing.Any]:
        return jsii.get(self, "cfnProperties")

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_2508893f:
        """``AWS::MediaConvert::JobTemplate.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-jobtemplate.html#cfn-mediaconvert-jobtemplate-tags
        """
        return jsii.get(self, "tags")

    @builtins.property
    @jsii.member(jsii_name="settingsJson")
    def settings_json(self) -> typing.Any:
        """``AWS::MediaConvert::JobTemplate.SettingsJson``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-jobtemplate.html#cfn-mediaconvert-jobtemplate-settingsjson
        """
        return jsii.get(self, "settingsJson")

    @settings_json.setter
    def settings_json(self, value: typing.Any) -> None:
        jsii.set(self, "settingsJson", value)

    @builtins.property
    @jsii.member(jsii_name="accelerationSettings")
    def acceleration_settings(
        self,
    ) -> typing.Optional[
        typing.Union["AccelerationSettingsProperty", _IResolvable_9ceae33e]
    ]:
        """``AWS::MediaConvert::JobTemplate.AccelerationSettings``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-jobtemplate.html#cfn-mediaconvert-jobtemplate-accelerationsettings
        """
        return jsii.get(self, "accelerationSettings")

    @acceleration_settings.setter
    def acceleration_settings(
        self,
        value: typing.Optional[
            typing.Union["AccelerationSettingsProperty", _IResolvable_9ceae33e]
        ],
    ) -> None:
        jsii.set(self, "accelerationSettings", value)

    @builtins.property
    @jsii.member(jsii_name="category")
    def category(self) -> typing.Optional[str]:
        """``AWS::MediaConvert::JobTemplate.Category``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-jobtemplate.html#cfn-mediaconvert-jobtemplate-category
        """
        return jsii.get(self, "category")

    @category.setter
    def category(self, value: typing.Optional[str]) -> None:
        jsii.set(self, "category", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[str]:
        """``AWS::MediaConvert::JobTemplate.Description``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-jobtemplate.html#cfn-mediaconvert-jobtemplate-description
        """
        return jsii.get(self, "description")

    @description.setter
    def description(self, value: typing.Optional[str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="hopDestinations")
    def hop_destinations(
        self,
    ) -> typing.Optional[
        typing.Union[
            _IResolvable_9ceae33e,
            typing.List[typing.Union["HopDestinationProperty", _IResolvable_9ceae33e]],
        ]
    ]:
        """``AWS::MediaConvert::JobTemplate.HopDestinations``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-jobtemplate.html#cfn-mediaconvert-jobtemplate-hopdestinations
        """
        return jsii.get(self, "hopDestinations")

    @hop_destinations.setter
    def hop_destinations(
        self,
        value: typing.Optional[
            typing.Union[
                _IResolvable_9ceae33e,
                typing.List[
                    typing.Union["HopDestinationProperty", _IResolvable_9ceae33e]
                ],
            ]
        ],
    ) -> None:
        jsii.set(self, "hopDestinations", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[str]:
        """``AWS::MediaConvert::JobTemplate.Name``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-jobtemplate.html#cfn-mediaconvert-jobtemplate-name
        """
        return jsii.get(self, "name")

    @name.setter
    def name(self, value: typing.Optional[str]) -> None:
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="priority")
    def priority(self) -> typing.Optional[jsii.Number]:
        """``AWS::MediaConvert::JobTemplate.Priority``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-jobtemplate.html#cfn-mediaconvert-jobtemplate-priority
        """
        return jsii.get(self, "priority")

    @priority.setter
    def priority(self, value: typing.Optional[jsii.Number]) -> None:
        jsii.set(self, "priority", value)

    @builtins.property
    @jsii.member(jsii_name="queue")
    def queue(self) -> typing.Optional[str]:
        """``AWS::MediaConvert::JobTemplate.Queue``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-jobtemplate.html#cfn-mediaconvert-jobtemplate-queue
        """
        return jsii.get(self, "queue")

    @queue.setter
    def queue(self, value: typing.Optional[str]) -> None:
        jsii.set(self, "queue", value)

    @builtins.property
    @jsii.member(jsii_name="statusUpdateInterval")
    def status_update_interval(self) -> typing.Optional[str]:
        """``AWS::MediaConvert::JobTemplate.StatusUpdateInterval``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-jobtemplate.html#cfn-mediaconvert-jobtemplate-statusupdateinterval
        """
        return jsii.get(self, "statusUpdateInterval")

    @status_update_interval.setter
    def status_update_interval(self, value: typing.Optional[str]) -> None:
        jsii.set(self, "statusUpdateInterval", value)

    @jsii.data_type(
        jsii_type="monocdk-experiment.aws_mediaconvert.CfnJobTemplate.AccelerationSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={"mode": "mode"},
    )
    class AccelerationSettingsProperty:
        def __init__(self, *, mode: str) -> None:
            """
            :param mode: ``CfnJobTemplate.AccelerationSettingsProperty.Mode``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconvert-jobtemplate-accelerationsettings.html
            """
            self._values = {
                "mode": mode,
            }

        @builtins.property
        def mode(self) -> str:
            """``CfnJobTemplate.AccelerationSettingsProperty.Mode``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconvert-jobtemplate-accelerationsettings.html#cfn-mediaconvert-jobtemplate-accelerationsettings-mode
            """
            return self._values.get("mode")

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AccelerationSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk-experiment.aws_mediaconvert.CfnJobTemplate.HopDestinationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "priority": "priority",
            "queue": "queue",
            "wait_minutes": "waitMinutes",
        },
    )
    class HopDestinationProperty:
        def __init__(
            self,
            *,
            priority: typing.Optional[jsii.Number] = None,
            queue: typing.Optional[str] = None,
            wait_minutes: typing.Optional[jsii.Number] = None,
        ) -> None:
            """
            :param priority: ``CfnJobTemplate.HopDestinationProperty.Priority``.
            :param queue: ``CfnJobTemplate.HopDestinationProperty.Queue``.
            :param wait_minutes: ``CfnJobTemplate.HopDestinationProperty.WaitMinutes``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconvert-jobtemplate-hopdestination.html
            """
            self._values = {}
            if priority is not None:
                self._values["priority"] = priority
            if queue is not None:
                self._values["queue"] = queue
            if wait_minutes is not None:
                self._values["wait_minutes"] = wait_minutes

        @builtins.property
        def priority(self) -> typing.Optional[jsii.Number]:
            """``CfnJobTemplate.HopDestinationProperty.Priority``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconvert-jobtemplate-hopdestination.html#cfn-mediaconvert-jobtemplate-hopdestination-priority
            """
            return self._values.get("priority")

        @builtins.property
        def queue(self) -> typing.Optional[str]:
            """``CfnJobTemplate.HopDestinationProperty.Queue``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconvert-jobtemplate-hopdestination.html#cfn-mediaconvert-jobtemplate-hopdestination-queue
            """
            return self._values.get("queue")

        @builtins.property
        def wait_minutes(self) -> typing.Optional[jsii.Number]:
            """``CfnJobTemplate.HopDestinationProperty.WaitMinutes``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconvert-jobtemplate-hopdestination.html#cfn-mediaconvert-jobtemplate-hopdestination-waitminutes
            """
            return self._values.get("wait_minutes")

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HopDestinationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="monocdk-experiment.aws_mediaconvert.CfnJobTemplateProps",
    jsii_struct_bases=[],
    name_mapping={
        "settings_json": "settingsJson",
        "acceleration_settings": "accelerationSettings",
        "category": "category",
        "description": "description",
        "hop_destinations": "hopDestinations",
        "name": "name",
        "priority": "priority",
        "queue": "queue",
        "status_update_interval": "statusUpdateInterval",
        "tags": "tags",
    },
)
class CfnJobTemplateProps:
    def __init__(
        self,
        *,
        settings_json: typing.Any,
        acceleration_settings: typing.Optional[
            typing.Union[
                "CfnJobTemplate.AccelerationSettingsProperty", _IResolvable_9ceae33e
            ]
        ] = None,
        category: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        hop_destinations: typing.Optional[
            typing.Union[
                _IResolvable_9ceae33e,
                typing.List[
                    typing.Union[
                        "CfnJobTemplate.HopDestinationProperty", _IResolvable_9ceae33e
                    ]
                ],
            ]
        ] = None,
        name: typing.Optional[str] = None,
        priority: typing.Optional[jsii.Number] = None,
        queue: typing.Optional[str] = None,
        status_update_interval: typing.Optional[str] = None,
        tags: typing.Any = None,
    ) -> None:
        """Properties for defining a ``AWS::MediaConvert::JobTemplate``.

        :param settings_json: ``AWS::MediaConvert::JobTemplate.SettingsJson``.
        :param acceleration_settings: ``AWS::MediaConvert::JobTemplate.AccelerationSettings``.
        :param category: ``AWS::MediaConvert::JobTemplate.Category``.
        :param description: ``AWS::MediaConvert::JobTemplate.Description``.
        :param hop_destinations: ``AWS::MediaConvert::JobTemplate.HopDestinations``.
        :param name: ``AWS::MediaConvert::JobTemplate.Name``.
        :param priority: ``AWS::MediaConvert::JobTemplate.Priority``.
        :param queue: ``AWS::MediaConvert::JobTemplate.Queue``.
        :param status_update_interval: ``AWS::MediaConvert::JobTemplate.StatusUpdateInterval``.
        :param tags: ``AWS::MediaConvert::JobTemplate.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-jobtemplate.html
        """
        self._values = {
            "settings_json": settings_json,
        }
        if acceleration_settings is not None:
            self._values["acceleration_settings"] = acceleration_settings
        if category is not None:
            self._values["category"] = category
        if description is not None:
            self._values["description"] = description
        if hop_destinations is not None:
            self._values["hop_destinations"] = hop_destinations
        if name is not None:
            self._values["name"] = name
        if priority is not None:
            self._values["priority"] = priority
        if queue is not None:
            self._values["queue"] = queue
        if status_update_interval is not None:
            self._values["status_update_interval"] = status_update_interval
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def settings_json(self) -> typing.Any:
        """``AWS::MediaConvert::JobTemplate.SettingsJson``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-jobtemplate.html#cfn-mediaconvert-jobtemplate-settingsjson
        """
        return self._values.get("settings_json")

    @builtins.property
    def acceleration_settings(
        self,
    ) -> typing.Optional[
        typing.Union[
            "CfnJobTemplate.AccelerationSettingsProperty", _IResolvable_9ceae33e
        ]
    ]:
        """``AWS::MediaConvert::JobTemplate.AccelerationSettings``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-jobtemplate.html#cfn-mediaconvert-jobtemplate-accelerationsettings
        """
        return self._values.get("acceleration_settings")

    @builtins.property
    def category(self) -> typing.Optional[str]:
        """``AWS::MediaConvert::JobTemplate.Category``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-jobtemplate.html#cfn-mediaconvert-jobtemplate-category
        """
        return self._values.get("category")

    @builtins.property
    def description(self) -> typing.Optional[str]:
        """``AWS::MediaConvert::JobTemplate.Description``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-jobtemplate.html#cfn-mediaconvert-jobtemplate-description
        """
        return self._values.get("description")

    @builtins.property
    def hop_destinations(
        self,
    ) -> typing.Optional[
        typing.Union[
            _IResolvable_9ceae33e,
            typing.List[
                typing.Union[
                    "CfnJobTemplate.HopDestinationProperty", _IResolvable_9ceae33e
                ]
            ],
        ]
    ]:
        """``AWS::MediaConvert::JobTemplate.HopDestinations``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-jobtemplate.html#cfn-mediaconvert-jobtemplate-hopdestinations
        """
        return self._values.get("hop_destinations")

    @builtins.property
    def name(self) -> typing.Optional[str]:
        """``AWS::MediaConvert::JobTemplate.Name``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-jobtemplate.html#cfn-mediaconvert-jobtemplate-name
        """
        return self._values.get("name")

    @builtins.property
    def priority(self) -> typing.Optional[jsii.Number]:
        """``AWS::MediaConvert::JobTemplate.Priority``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-jobtemplate.html#cfn-mediaconvert-jobtemplate-priority
        """
        return self._values.get("priority")

    @builtins.property
    def queue(self) -> typing.Optional[str]:
        """``AWS::MediaConvert::JobTemplate.Queue``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-jobtemplate.html#cfn-mediaconvert-jobtemplate-queue
        """
        return self._values.get("queue")

    @builtins.property
    def status_update_interval(self) -> typing.Optional[str]:
        """``AWS::MediaConvert::JobTemplate.StatusUpdateInterval``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-jobtemplate.html#cfn-mediaconvert-jobtemplate-statusupdateinterval
        """
        return self._values.get("status_update_interval")

    @builtins.property
    def tags(self) -> typing.Any:
        """``AWS::MediaConvert::JobTemplate.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-jobtemplate.html#cfn-mediaconvert-jobtemplate-tags
        """
        return self._values.get("tags")

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnJobTemplateProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_051e6ed8)
class CfnPreset(
    _CfnResource_7760e8e4,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk-experiment.aws_mediaconvert.CfnPreset",
):
    """A CloudFormation ``AWS::MediaConvert::Preset``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-preset.html
    cloudformationResource:
    :cloudformationResource:: AWS::MediaConvert::Preset
    """

    def __init__(
        self,
        scope: _Construct_f50a3f53,
        id: str,
        *,
        settings_json: typing.Any,
        category: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        tags: typing.Any = None,
    ) -> None:
        """Create a new ``AWS::MediaConvert::Preset``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param settings_json: ``AWS::MediaConvert::Preset.SettingsJson``.
        :param category: ``AWS::MediaConvert::Preset.Category``.
        :param description: ``AWS::MediaConvert::Preset.Description``.
        :param name: ``AWS::MediaConvert::Preset.Name``.
        :param tags: ``AWS::MediaConvert::Preset.Tags``.
        """
        props = CfnPresetProps(
            settings_json=settings_json,
            category=category,
            description=description,
            name=name,
            tags=tags,
        )

        jsii.create(CfnPreset, self, [scope, id, props])

    @jsii.member(jsii_name="fromCloudFormation")
    @builtins.classmethod
    def from_cloud_formation(
        cls,
        scope: _Construct_f50a3f53,
        id: str,
        resource_attributes: typing.Any,
        *,
        finder: _ICfnFinder_3b168f30,
    ) -> "CfnPreset":
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
    @jsii.member(jsii_name="attrName")
    def attr_name(self) -> str:
        """
        cloudformationAttribute:
        :cloudformationAttribute:: Name
        """
        return jsii.get(self, "attrName")

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[str, typing.Any]:
        return jsii.get(self, "cfnProperties")

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_2508893f:
        """``AWS::MediaConvert::Preset.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-preset.html#cfn-mediaconvert-preset-tags
        """
        return jsii.get(self, "tags")

    @builtins.property
    @jsii.member(jsii_name="settingsJson")
    def settings_json(self) -> typing.Any:
        """``AWS::MediaConvert::Preset.SettingsJson``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-preset.html#cfn-mediaconvert-preset-settingsjson
        """
        return jsii.get(self, "settingsJson")

    @settings_json.setter
    def settings_json(self, value: typing.Any) -> None:
        jsii.set(self, "settingsJson", value)

    @builtins.property
    @jsii.member(jsii_name="category")
    def category(self) -> typing.Optional[str]:
        """``AWS::MediaConvert::Preset.Category``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-preset.html#cfn-mediaconvert-preset-category
        """
        return jsii.get(self, "category")

    @category.setter
    def category(self, value: typing.Optional[str]) -> None:
        jsii.set(self, "category", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[str]:
        """``AWS::MediaConvert::Preset.Description``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-preset.html#cfn-mediaconvert-preset-description
        """
        return jsii.get(self, "description")

    @description.setter
    def description(self, value: typing.Optional[str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[str]:
        """``AWS::MediaConvert::Preset.Name``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-preset.html#cfn-mediaconvert-preset-name
        """
        return jsii.get(self, "name")

    @name.setter
    def name(self, value: typing.Optional[str]) -> None:
        jsii.set(self, "name", value)


@jsii.data_type(
    jsii_type="monocdk-experiment.aws_mediaconvert.CfnPresetProps",
    jsii_struct_bases=[],
    name_mapping={
        "settings_json": "settingsJson",
        "category": "category",
        "description": "description",
        "name": "name",
        "tags": "tags",
    },
)
class CfnPresetProps:
    def __init__(
        self,
        *,
        settings_json: typing.Any,
        category: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        tags: typing.Any = None,
    ) -> None:
        """Properties for defining a ``AWS::MediaConvert::Preset``.

        :param settings_json: ``AWS::MediaConvert::Preset.SettingsJson``.
        :param category: ``AWS::MediaConvert::Preset.Category``.
        :param description: ``AWS::MediaConvert::Preset.Description``.
        :param name: ``AWS::MediaConvert::Preset.Name``.
        :param tags: ``AWS::MediaConvert::Preset.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-preset.html
        """
        self._values = {
            "settings_json": settings_json,
        }
        if category is not None:
            self._values["category"] = category
        if description is not None:
            self._values["description"] = description
        if name is not None:
            self._values["name"] = name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def settings_json(self) -> typing.Any:
        """``AWS::MediaConvert::Preset.SettingsJson``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-preset.html#cfn-mediaconvert-preset-settingsjson
        """
        return self._values.get("settings_json")

    @builtins.property
    def category(self) -> typing.Optional[str]:
        """``AWS::MediaConvert::Preset.Category``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-preset.html#cfn-mediaconvert-preset-category
        """
        return self._values.get("category")

    @builtins.property
    def description(self) -> typing.Optional[str]:
        """``AWS::MediaConvert::Preset.Description``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-preset.html#cfn-mediaconvert-preset-description
        """
        return self._values.get("description")

    @builtins.property
    def name(self) -> typing.Optional[str]:
        """``AWS::MediaConvert::Preset.Name``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-preset.html#cfn-mediaconvert-preset-name
        """
        return self._values.get("name")

    @builtins.property
    def tags(self) -> typing.Any:
        """``AWS::MediaConvert::Preset.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-preset.html#cfn-mediaconvert-preset-tags
        """
        return self._values.get("tags")

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPresetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_051e6ed8)
class CfnQueue(
    _CfnResource_7760e8e4,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk-experiment.aws_mediaconvert.CfnQueue",
):
    """A CloudFormation ``AWS::MediaConvert::Queue``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-queue.html
    cloudformationResource:
    :cloudformationResource:: AWS::MediaConvert::Queue
    """

    def __init__(
        self,
        scope: _Construct_f50a3f53,
        id: str,
        *,
        description: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        pricing_plan: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        tags: typing.Any = None,
    ) -> None:
        """Create a new ``AWS::MediaConvert::Queue``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param description: ``AWS::MediaConvert::Queue.Description``.
        :param name: ``AWS::MediaConvert::Queue.Name``.
        :param pricing_plan: ``AWS::MediaConvert::Queue.PricingPlan``.
        :param status: ``AWS::MediaConvert::Queue.Status``.
        :param tags: ``AWS::MediaConvert::Queue.Tags``.
        """
        props = CfnQueueProps(
            description=description,
            name=name,
            pricing_plan=pricing_plan,
            status=status,
            tags=tags,
        )

        jsii.create(CfnQueue, self, [scope, id, props])

    @jsii.member(jsii_name="fromCloudFormation")
    @builtins.classmethod
    def from_cloud_formation(
        cls,
        scope: _Construct_f50a3f53,
        id: str,
        resource_attributes: typing.Any,
        *,
        finder: _ICfnFinder_3b168f30,
    ) -> "CfnQueue":
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
    @jsii.member(jsii_name="attrName")
    def attr_name(self) -> str:
        """
        cloudformationAttribute:
        :cloudformationAttribute:: Name
        """
        return jsii.get(self, "attrName")

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[str, typing.Any]:
        return jsii.get(self, "cfnProperties")

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_2508893f:
        """``AWS::MediaConvert::Queue.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-queue.html#cfn-mediaconvert-queue-tags
        """
        return jsii.get(self, "tags")

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[str]:
        """``AWS::MediaConvert::Queue.Description``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-queue.html#cfn-mediaconvert-queue-description
        """
        return jsii.get(self, "description")

    @description.setter
    def description(self, value: typing.Optional[str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[str]:
        """``AWS::MediaConvert::Queue.Name``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-queue.html#cfn-mediaconvert-queue-name
        """
        return jsii.get(self, "name")

    @name.setter
    def name(self, value: typing.Optional[str]) -> None:
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="pricingPlan")
    def pricing_plan(self) -> typing.Optional[str]:
        """``AWS::MediaConvert::Queue.PricingPlan``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-queue.html#cfn-mediaconvert-queue-pricingplan
        """
        return jsii.get(self, "pricingPlan")

    @pricing_plan.setter
    def pricing_plan(self, value: typing.Optional[str]) -> None:
        jsii.set(self, "pricingPlan", value)

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> typing.Optional[str]:
        """``AWS::MediaConvert::Queue.Status``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-queue.html#cfn-mediaconvert-queue-status
        """
        return jsii.get(self, "status")

    @status.setter
    def status(self, value: typing.Optional[str]) -> None:
        jsii.set(self, "status", value)


@jsii.data_type(
    jsii_type="monocdk-experiment.aws_mediaconvert.CfnQueueProps",
    jsii_struct_bases=[],
    name_mapping={
        "description": "description",
        "name": "name",
        "pricing_plan": "pricingPlan",
        "status": "status",
        "tags": "tags",
    },
)
class CfnQueueProps:
    def __init__(
        self,
        *,
        description: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        pricing_plan: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        tags: typing.Any = None,
    ) -> None:
        """Properties for defining a ``AWS::MediaConvert::Queue``.

        :param description: ``AWS::MediaConvert::Queue.Description``.
        :param name: ``AWS::MediaConvert::Queue.Name``.
        :param pricing_plan: ``AWS::MediaConvert::Queue.PricingPlan``.
        :param status: ``AWS::MediaConvert::Queue.Status``.
        :param tags: ``AWS::MediaConvert::Queue.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-queue.html
        """
        self._values = {}
        if description is not None:
            self._values["description"] = description
        if name is not None:
            self._values["name"] = name
        if pricing_plan is not None:
            self._values["pricing_plan"] = pricing_plan
        if status is not None:
            self._values["status"] = status
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def description(self) -> typing.Optional[str]:
        """``AWS::MediaConvert::Queue.Description``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-queue.html#cfn-mediaconvert-queue-description
        """
        return self._values.get("description")

    @builtins.property
    def name(self) -> typing.Optional[str]:
        """``AWS::MediaConvert::Queue.Name``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-queue.html#cfn-mediaconvert-queue-name
        """
        return self._values.get("name")

    @builtins.property
    def pricing_plan(self) -> typing.Optional[str]:
        """``AWS::MediaConvert::Queue.PricingPlan``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-queue.html#cfn-mediaconvert-queue-pricingplan
        """
        return self._values.get("pricing_plan")

    @builtins.property
    def status(self) -> typing.Optional[str]:
        """``AWS::MediaConvert::Queue.Status``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-queue.html#cfn-mediaconvert-queue-status
        """
        return self._values.get("status")

    @builtins.property
    def tags(self) -> typing.Any:
        """``AWS::MediaConvert::Queue.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-queue.html#cfn-mediaconvert-queue-tags
        """
        return self._values.get("tags")

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnQueueProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnJobTemplate",
    "CfnJobTemplateProps",
    "CfnPreset",
    "CfnPresetProps",
    "CfnQueue",
    "CfnQueueProps",
]

publication.publish()
