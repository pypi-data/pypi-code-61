"""
## AWS Security Hub Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_securityhub as securityhub
```
"""
import abc
import builtins
import datetime
import enum
import typing

import jsii
import jsii.compat
import publication

from ._jsii import *

import aws_cdk.core


@jsii.implements(aws_cdk.core.IInspectable)
class CfnHub(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-securityhub.CfnHub",
):
    """A CloudFormation ``AWS::SecurityHub::Hub``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityhub-hub.html
    cloudformationResource:
    :cloudformationResource:: AWS::SecurityHub::Hub
    """

    def __init__(
        self, scope: aws_cdk.core.Construct, id: str, *, tags: typing.Any = None
    ) -> None:
        """Create a new ``AWS::SecurityHub::Hub``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param tags: ``AWS::SecurityHub::Hub.Tags``.
        """
        props = CfnHubProps(tags=tags)

        jsii.create(CfnHub, self, [scope, id, props])

    @jsii.member(jsii_name="fromCloudFormation")
    @builtins.classmethod
    def from_cloud_formation(
        cls,
        scope: aws_cdk.core.Construct,
        id: str,
        resource_attributes: typing.Any,
        *,
        finder: aws_cdk.core.ICfnFinder,
    ) -> "CfnHub":
        """A factory method that creates a new instance of this class from an object containing the CloudFormation properties of this resource.

        Used in the @aws-cdk/cloudformation-include module.

        :param scope: -
        :param id: -
        :param resource_attributes: -
        :param finder: The finder interface used to resolve references across the template.

        stability
        :stability: experimental
        """
        options = aws_cdk.core.FromCloudFormationOptions(finder=finder)

        return jsii.sinvoke(
            cls, "fromCloudFormation", [scope, id, resource_attributes, options]
        )

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
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
    def tags(self) -> aws_cdk.core.TagManager:
        """``AWS::SecurityHub::Hub.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityhub-hub.html#cfn-securityhub-hub-tags
        """
        return jsii.get(self, "tags")


@jsii.data_type(
    jsii_type="@aws-cdk/aws-securityhub.CfnHubProps",
    jsii_struct_bases=[],
    name_mapping={"tags": "tags"},
)
class CfnHubProps:
    def __init__(self, *, tags: typing.Any = None) -> None:
        """Properties for defining a ``AWS::SecurityHub::Hub``.

        :param tags: ``AWS::SecurityHub::Hub.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityhub-hub.html
        """
        self._values = {}
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def tags(self) -> typing.Any:
        """``AWS::SecurityHub::Hub.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityhub-hub.html#cfn-securityhub-hub-tags
        """
        return self._values.get("tags")

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnHubProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnHub",
    "CfnHubProps",
]

publication.publish()
