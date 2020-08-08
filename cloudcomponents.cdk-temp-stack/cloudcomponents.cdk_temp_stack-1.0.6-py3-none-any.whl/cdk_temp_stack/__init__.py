"""
[![cloudcomponents Logo](https://raw.githubusercontent.com/cloudcomponents/cdk-constructs/master/logo.png)](https://github.com/cloudcomponents/cdk-constructs)

# @cloudcomponents/cdk-temp-stack

[![Build Status](https://travis-ci.org/cloudcomponents/cdk-constructs.svg?branch=master)](https://travis-ci.org/cloudcomponents/cdk-constructs)
[![cdkdx](https://img.shields.io/badge/buildtool-cdkdx-blue.svg)](https://github.com/hupe1980/cdkdx)
[![typescript](https://img.shields.io/badge/jsii-typescript-blueviolet.svg)](https://www.npmjs.com/package/@cloudcomponents/cdk-temp-stack)
[![python](https://img.shields.io/badge/jsii-python-blueviolet.svg)](https://pypi.org/project/cloudcomponents.cdk-temp-stack/)

> A stack that destroys itself after a given time (ttl)

## Install

TypeScript/JavaScript:

```bash
npm i @cloudcomponents/cdk-temp-stack
```

Python:

```bash
pip install cloudcomponents.cdk-temp-stack
```

## How to use

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
~/usr/bin / envnode

from source_map_support.register import
from aws_cdk.core import App, Duration

from ..temp_infra_stack import TempInfraStack

app = App()

TempInfraStack(app, "TempInfraStack",
    env=Environment(
        region=process.env.DEFAULT_REGION,
        account=process.env.CDK_DEFAULT_ACCOUNT
    ),
    ttl=Duration.minutes(10)
)

# temp-infra-stack.ts

from aws_cdk.core import Construct
from aws_cdk.aws_ec2 import Vpc
from cloudcomponents.cdk_temp_stack import TempStack, TempStackProps

class TempInfraStack(TempStack):
    def __init__(self, scope, id, *, ttl, description=None, env=None, stackName=None, tags=None, synthesizer=None, terminationProtection=None):
        super().__init__(scope, id, ttl=ttl, description=description, env=env, stackName=stackName, tags=tags, synthesizer=synthesizer, terminationProtection=terminationProtection)

        Vpc(self, "VPC")
```

## TimeToLive Construct

Alternatively, you can also add the TimeToLive construct to your stack

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
# your stack

from aws_cdk.core import Construct, Stack, StackProps, Duration
from cloudcomponents.cdk_temp_stack import TimeToLive

class YourStack(Stack):
    def __init__(self, scope, id, *, description=None, env=None, stackName=None, tags=None, synthesizer=None, terminationProtection=None):
        super().__init__(scope, id, description=description, env=env, stackName=stackName, tags=tags, synthesizer=synthesizer, terminationProtection=terminationProtection)

        TimeToLive(self, "TimeToLive",
            ttl=Duration.minutes(10)
        )
```

## API Reference

See [API.md](https://github.com/cloudcomponents/cdk-constructs/tree/master/packages/cdk-temp-stack/API.md).

## Example

See more complete [examples](https://github.com/cloudcomponents/cdk-constructs/tree/master/examples).

## License

[MIT](https://github.com/cloudcomponents/cdk-constructs/tree/master/packages/cdk-temp-stack/LICENSE)
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


class TempStack(
    aws_cdk.core.Stack,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cloudcomponents/cdk-temp-stack.TempStack",
):
    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: str,
        *,
        ttl: aws_cdk.core.Duration,
        description: typing.Optional[str] = None,
        env: typing.Optional[aws_cdk.core.Environment] = None,
        stack_name: typing.Optional[str] = None,
        synthesizer: typing.Optional[aws_cdk.core.IStackSynthesizer] = None,
        tags: typing.Optional[typing.Mapping[str, str]] = None,
        termination_protection: typing.Optional[bool] = None,
    ) -> None:
        """
        :param scope: -
        :param id: -
        :param ttl: Specifies the Time to Live (TTL) settings for the stack.
        :param description: A description of the stack. Default: - No description.
        :param env: The AWS environment (account/region) where this stack will be deployed. Set the ``region``/``account`` fields of ``env`` to either a concrete value to select the indicated environment (recommended for production stacks), or to the values of environment variables ``CDK_DEFAULT_REGION``/``CDK_DEFAULT_ACCOUNT`` to let the target environment depend on the AWS credentials/configuration that the CDK CLI is executed under (recommended for development stacks). If the ``Stack`` is instantiated inside a ``Stage``, any undefined ``region``/``account`` fields from ``env`` will default to the same field on the encompassing ``Stage``, if configured there. If either ``region`` or ``account`` are not set nor inherited from ``Stage``, the Stack will be considered "*environment-agnostic*"". Environment-agnostic stacks can be deployed to any environment but may not be able to take advantage of all features of the CDK. For example, they will not be able to use environmental context lookups such as ``ec2.Vpc.fromLookup`` and will not automatically translate Service Principals to the right format based on the environment's AWS partition, and other such enhancements. Default: - The environment of the containing ``Stage`` if available, otherwise create the stack will be environment-agnostic.
        :param stack_name: Name to deploy the stack with. Default: - Derived from construct path.
        :param synthesizer: Synthesis method to use while deploying this stack. Default: - ``DefaultStackSynthesizer`` if the ``@aws-cdk/core:newStyleStackSynthesis`` feature flag is set, ``LegacyStackSynthesizer`` otherwise.
        :param tags: Stack tags that will be applied to all the taggable resources and the stack itself. Default: {}
        :param termination_protection: Whether to enable termination protection for this stack. Default: false
        """
        props = TempStackProps(
            ttl=ttl,
            description=description,
            env=env,
            stack_name=stack_name,
            synthesizer=synthesizer,
            tags=tags,
            termination_protection=termination_protection,
        )

        jsii.create(TempStack, self, [scope, id, props])


@jsii.data_type(
    jsii_type="@cloudcomponents/cdk-temp-stack.TempStackProps",
    jsii_struct_bases=[aws_cdk.core.StackProps],
    name_mapping={
        "description": "description",
        "env": "env",
        "stack_name": "stackName",
        "synthesizer": "synthesizer",
        "tags": "tags",
        "termination_protection": "terminationProtection",
        "ttl": "ttl",
    },
)
class TempStackProps(aws_cdk.core.StackProps):
    def __init__(
        self,
        *,
        description: typing.Optional[str] = None,
        env: typing.Optional[aws_cdk.core.Environment] = None,
        stack_name: typing.Optional[str] = None,
        synthesizer: typing.Optional[aws_cdk.core.IStackSynthesizer] = None,
        tags: typing.Optional[typing.Mapping[str, str]] = None,
        termination_protection: typing.Optional[bool] = None,
        ttl: aws_cdk.core.Duration,
    ) -> None:
        """
        :param description: A description of the stack. Default: - No description.
        :param env: The AWS environment (account/region) where this stack will be deployed. Set the ``region``/``account`` fields of ``env`` to either a concrete value to select the indicated environment (recommended for production stacks), or to the values of environment variables ``CDK_DEFAULT_REGION``/``CDK_DEFAULT_ACCOUNT`` to let the target environment depend on the AWS credentials/configuration that the CDK CLI is executed under (recommended for development stacks). If the ``Stack`` is instantiated inside a ``Stage``, any undefined ``region``/``account`` fields from ``env`` will default to the same field on the encompassing ``Stage``, if configured there. If either ``region`` or ``account`` are not set nor inherited from ``Stage``, the Stack will be considered "*environment-agnostic*"". Environment-agnostic stacks can be deployed to any environment but may not be able to take advantage of all features of the CDK. For example, they will not be able to use environmental context lookups such as ``ec2.Vpc.fromLookup`` and will not automatically translate Service Principals to the right format based on the environment's AWS partition, and other such enhancements. Default: - The environment of the containing ``Stage`` if available, otherwise create the stack will be environment-agnostic.
        :param stack_name: Name to deploy the stack with. Default: - Derived from construct path.
        :param synthesizer: Synthesis method to use while deploying this stack. Default: - ``DefaultStackSynthesizer`` if the ``@aws-cdk/core:newStyleStackSynthesis`` feature flag is set, ``LegacyStackSynthesizer`` otherwise.
        :param tags: Stack tags that will be applied to all the taggable resources and the stack itself. Default: {}
        :param termination_protection: Whether to enable termination protection for this stack. Default: false
        :param ttl: Specifies the Time to Live (TTL) settings for the stack.
        """
        if isinstance(env, dict):
            env = aws_cdk.core.Environment(**env)
        self._values = {
            "ttl": ttl,
        }
        if description is not None:
            self._values["description"] = description
        if env is not None:
            self._values["env"] = env
        if stack_name is not None:
            self._values["stack_name"] = stack_name
        if synthesizer is not None:
            self._values["synthesizer"] = synthesizer
        if tags is not None:
            self._values["tags"] = tags
        if termination_protection is not None:
            self._values["termination_protection"] = termination_protection

    @builtins.property
    def description(self) -> typing.Optional[str]:
        """A description of the stack.

        default
        :default: - No description.
        """
        return self._values.get("description")

    @builtins.property
    def env(self) -> typing.Optional[aws_cdk.core.Environment]:
        """The AWS environment (account/region) where this stack will be deployed.

        Set the ``region``/``account`` fields of ``env`` to either a concrete value to
        select the indicated environment (recommended for production stacks), or to
        the values of environment variables
        ``CDK_DEFAULT_REGION``/``CDK_DEFAULT_ACCOUNT`` to let the target environment
        depend on the AWS credentials/configuration that the CDK CLI is executed
        under (recommended for development stacks).

        If the ``Stack`` is instantiated inside a ``Stage``, any undefined
        ``region``/``account`` fields from ``env`` will default to the same field on the
        encompassing ``Stage``, if configured there.

        If either ``region`` or ``account`` are not set nor inherited from ``Stage``, the
        Stack will be considered "*environment-agnostic*"". Environment-agnostic
        stacks can be deployed to any environment but may not be able to take
        advantage of all features of the CDK. For example, they will not be able to
        use environmental context lookups such as ``ec2.Vpc.fromLookup`` and will not
        automatically translate Service Principals to the right format based on the
        environment's AWS partition, and other such enhancements.

        default
        :default:

        - The environment of the containing ``Stage`` if available,
          otherwise create the stack will be environment-agnostic.

        Example::

            # Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
            # Use a concrete account and region to deploy this stack to:
            # `.account` and `.region` will simply return these values.
            MyStack(app, "Stack1",
                env={
                    "account": "123456789012",
                    "region": "us-east-1"
                }
            )
            
            # Use the CLI's current credentials to determine the target environment:
            # `.account` and `.region` will reflect the account+region the CLI
            # is configured to use (based on the user CLI credentials)
            MyStack(app, "Stack2",
                env={
                    "account": process.env.CDK_DEFAULT_ACCOUNT,
                    "region": process.env.CDK_DEFAULT_REGION
                }
            )
            
            # Define multiple stacks stage associated with an environment
            my_stage = Stage(app, "MyStage",
                env={
                    "account": "123456789012",
                    "region": "us-east-1"
                }
            )
            
            # both of these stacks will use the stage's account/region:
            # `.account` and `.region` will resolve to the concrete values as above
            MyStack(my_stage, "Stack1")
            YourStack(my_stage, "Stack1")
            
            # Define an environment-agnostic stack:
            # `.account` and `.region` will resolve to `{ "Ref": "AWS::AccountId" }` and `{ "Ref": "AWS::Region" }` respectively.
            # which will only resolve to actual values by CloudFormation during deployment.
            MyStack(app, "Stack1")
        """
        return self._values.get("env")

    @builtins.property
    def stack_name(self) -> typing.Optional[str]:
        """Name to deploy the stack with.

        default
        :default: - Derived from construct path.
        """
        return self._values.get("stack_name")

    @builtins.property
    def synthesizer(self) -> typing.Optional[aws_cdk.core.IStackSynthesizer]:
        """Synthesis method to use while deploying this stack.

        default
        :default:

        - ``DefaultStackSynthesizer`` if the ``@aws-cdk/core:newStyleStackSynthesis`` feature flag
          is set, ``LegacyStackSynthesizer`` otherwise.
        """
        return self._values.get("synthesizer")

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[str, str]]:
        """Stack tags that will be applied to all the taggable resources and the stack itself.

        default
        :default: {}
        """
        return self._values.get("tags")

    @builtins.property
    def termination_protection(self) -> typing.Optional[bool]:
        """Whether to enable termination protection for this stack.

        default
        :default: false
        """
        return self._values.get("termination_protection")

    @builtins.property
    def ttl(self) -> aws_cdk.core.Duration:
        """Specifies the Time to Live (TTL) settings for the stack."""
        return self._values.get("ttl")

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TempStackProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class TimeToLive(
    aws_cdk.core.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cloudcomponents/cdk-temp-stack.TimeToLive",
):
    def __init__(
        self, scope: aws_cdk.core.Construct, id: str, *, ttl: aws_cdk.core.Duration
    ) -> None:
        """
        :param scope: -
        :param id: -
        :param ttl: Specifies the Time to Live (TTL) settings for the stack.
        """
        props = TimeToLiveProps(ttl=ttl)

        jsii.create(TimeToLive, self, [scope, id, props])

    @jsii.member(jsii_name="onPrepare")
    def _on_prepare(self) -> None:
        """Perform final modifications before synthesis.

        This method can be implemented by derived constructs in order to perform
        final changes before synthesis. prepare() will be called after child
        constructs have been prepared.

        This is an advanced framework feature. Only use this if you
        understand the implications.
        """
        return jsii.invoke(self, "onPrepare", [])

    @jsii.member(jsii_name="validate")
    def _validate(self) -> typing.List[str]:
        """Validate the current construct.

        This method can be implemented by derived constructs in order to perform
        validation logic. It is called on all constructs before synthesis.
        """
        return jsii.invoke(self, "validate", [])


@jsii.data_type(
    jsii_type="@cloudcomponents/cdk-temp-stack.TimeToLiveProps",
    jsii_struct_bases=[],
    name_mapping={"ttl": "ttl"},
)
class TimeToLiveProps:
    def __init__(self, *, ttl: aws_cdk.core.Duration) -> None:
        """
        :param ttl: Specifies the Time to Live (TTL) settings for the stack.
        """
        self._values = {
            "ttl": ttl,
        }

    @builtins.property
    def ttl(self) -> aws_cdk.core.Duration:
        """Specifies the Time to Live (TTL) settings for the stack."""
        return self._values.get("ttl")

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TimeToLiveProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "TempStack",
    "TempStackProps",
    "TimeToLive",
    "TimeToLiveProps",
]

publication.publish()
