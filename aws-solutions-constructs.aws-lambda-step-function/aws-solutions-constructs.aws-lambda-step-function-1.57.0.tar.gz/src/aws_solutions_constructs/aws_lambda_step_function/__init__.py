"""
# aws-lambda-step-function module

<!--BEGIN STABILITY BANNER-->---


![Stability: Experimental](https://img.shields.io/badge/stability-Experimental-important.svg?style=for-the-badge)

> All classes are under active development and subject to non-backward compatible changes or removal in any
> future version. These are not subject to the [Semantic Versioning](https://semver.org/) model.
> This means that while you may use them, you may need to update your source code when upgrading to a newer version of this package.

---
<!--END STABILITY BANNER-->

| **Reference Documentation**:| <span style="font-weight: normal">https://docs.aws.amazon.com/solutions/latest/constructs/</span>|
|:-------------|:-------------|

<div style="height:8px"></div>

| **Language**     | **Package**        |
|:-------------|-----------------|
|![Python Logo](https://docs.aws.amazon.com/cdk/api/latest/img/python32.png) Python|`aws_solutions_constructs.aws_lambda_step_function`|
|![Typescript Logo](https://docs.aws.amazon.com/cdk/api/latest/img/typescript32.png) Typescript|`@aws-solutions-constructs/aws-lambda-step-function`|
|![Java Logo](https://docs.aws.amazon.com/cdk/api/latest/img/java32.png) Java|`software.amazon.awsconstructs.services.lambdastepfunction`|

This AWS Solutions Construct implements an AWS Lambda function connected to an AWS Step Function.

Here is a minimal deployable pattern definition:

```javascript
const { LambdaToStepFunction } = require('@aws-solutions-constructs/aws-lambda-step-function');

new LambdaToStepFunction(stack, 'LambdaToStepFunctionPattern', {
    lambdaFunctionProps: {
        runtime: lambda.Runtime.NODEJS_12_X,
        handler: 'index.handler',
        code: lambda.Code.asset(`${__dirname}/lambda`)
    },
    stateMachineProps: {
      definition: startState
    }
});

```

## Initializer

```text
new LambdaToStepFunction(scope: Construct, id: string, props: LambdaToStepFunctionProps);
```

*Parameters*

* scope [`Construct`](https://docs.aws.amazon.com/cdk/api/latest/docs/@aws-cdk_core.Construct.html)
* id `string`
* props [`LambdaToStepFunctionProps`](#pattern-construct-props)

## Pattern Construct Props

| **Name**     | **Type**        | **Description** |
|:-------------|:----------------|-----------------|
|existingLambdaObj?|[`lambda.Function`](https://docs.aws.amazon.com/cdk/api/latest/docs/@aws-cdk_aws-lambda.Function.html)|Existing instance of Lambda Function object, if this is set then the lambdaFunctionProps is ignored.|
|lambdaFunctionProps?|[`lambda.FunctionProps`](https://docs.aws.amazon.com/cdk/api/latest/docs/@aws-cdk_aws-lambda.FunctionProps.html)|User provided props to override the default props for the Lambda function.|
|stateMachineProps|[`sfn.StateMachineProps`](https://docs.aws.amazon.com/cdk/api/latest/docs/@aws-cdk_aws-stepfunctions.StateMachineProps.html)|User provided props for the sfn.StateMachine.|

## Pattern Properties

| **Name**     | **Type**        | **Description** |
|:-------------|:----------------|-----------------|
|lambdaFunction|[`lambda.Function`](https://docs.aws.amazon.com/cdk/api/latest/docs/@aws-cdk_aws-lambda.Function.html)|Returns an instance of the Lambda function created by the pattern.|
|stateMachine|[`sfn.StateMachine`](https://docs.aws.amazon.com/cdk/api/latest/docs/@aws-cdk_aws-stepfunctions.StateMachine.html)|Returns an instance of StateMachine created by the construct.|
|stateMachineLogGroup|[`logs.LogGroup`](https://docs.aws.amazon.com/cdk/api/latest/docs/@aws-cdk_aws-logs.LogGroup.html)|Returns an instance of the LogGroup created by the construct for StateMachine|
|cloudwatchAlarms|[`cloudwatch.Alarm[]`](https://docs.aws.amazon.com/cdk/api/latest/docs/@aws-cdk_aws-cloudwatch.Alarm.html)|Returns a list of alarms created by the construct.

## Default settings

Out of the box implementation of the Construct without any override will set the following defaults:

### AWS Lambda Function

* Configure least privilege access IAM role for Lambda function
* Enable reusing connections with Keep-Alive for NodeJs Lambda function

### AWS Step Function

* Enable CloudWatch logging for API Gateway
* Deploy best practices CloudWatch Alarms for the Step Function

## Architecture

![Architecture Diagram](architecture.png)

---


© Copyright 2020 Amazon.com, Inc. or its affiliates. All Rights Reserved.
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

import aws_cdk.aws_cloudwatch
import aws_cdk.aws_lambda
import aws_cdk.aws_logs
import aws_cdk.aws_stepfunctions
import aws_cdk.core


class LambdaToStepFunction(
    aws_cdk.core.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-solutions-constructs/aws-lambda-step-function.LambdaToStepFunction",
):
    """
    summary:
    :summary:: The LambdaToStepFunctionProps class.
    """

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: str,
        *,
        state_machine_props: aws_cdk.aws_stepfunctions.StateMachineProps,
        existing_lambda_obj: typing.Optional[aws_cdk.aws_lambda.Function] = None,
        lambda_function_props: typing.Optional[aws_cdk.aws_lambda.FunctionProps] = None,
    ) -> None:
        """
        :param scope: - represents the scope for all the resources.
        :param id: - this is a a scope-unique id.
        :param state_machine_props: User provided StateMachineProps to override the defaults. Default: - None
        :param existing_lambda_obj: Existing instance of Lambda Function object, if this is set then the lambdaFunctionProps is ignored. Default: - None
        :param lambda_function_props: User provided props to override the default props for the Lambda function. Default: - Default properties are used.

        access:
        :access:: public
        since:
        :since:: 0.8.0
        summary:
        :summary:: Constructs a new instance of the LambdaToStepFunctionProps class.
        """
        props = LambdaToStepFunctionProps(
            state_machine_props=state_machine_props,
            existing_lambda_obj=existing_lambda_obj,
            lambda_function_props=lambda_function_props,
        )

        jsii.create(LambdaToStepFunction, self, [scope, id, props])

    @builtins.property
    @jsii.member(jsii_name="cloudwatchAlarms")
    def cloudwatch_alarms(self) -> typing.List[aws_cdk.aws_cloudwatch.Alarm]:
        return jsii.get(self, "cloudwatchAlarms")

    @builtins.property
    @jsii.member(jsii_name="lambdaFunction")
    def lambda_function(self) -> aws_cdk.aws_lambda.Function:
        return jsii.get(self, "lambdaFunction")

    @builtins.property
    @jsii.member(jsii_name="stateMachine")
    def state_machine(self) -> aws_cdk.aws_stepfunctions.StateMachine:
        return jsii.get(self, "stateMachine")

    @builtins.property
    @jsii.member(jsii_name="stateMachineLogGroup")
    def state_machine_log_group(self) -> aws_cdk.aws_logs.LogGroup:
        return jsii.get(self, "stateMachineLogGroup")


@jsii.data_type(
    jsii_type="@aws-solutions-constructs/aws-lambda-step-function.LambdaToStepFunctionProps",
    jsii_struct_bases=[],
    name_mapping={
        "state_machine_props": "stateMachineProps",
        "existing_lambda_obj": "existingLambdaObj",
        "lambda_function_props": "lambdaFunctionProps",
    },
)
class LambdaToStepFunctionProps:
    def __init__(
        self,
        *,
        state_machine_props: aws_cdk.aws_stepfunctions.StateMachineProps,
        existing_lambda_obj: typing.Optional[aws_cdk.aws_lambda.Function] = None,
        lambda_function_props: typing.Optional[aws_cdk.aws_lambda.FunctionProps] = None,
    ) -> None:
        """
        :param state_machine_props: User provided StateMachineProps to override the defaults. Default: - None
        :param existing_lambda_obj: Existing instance of Lambda Function object, if this is set then the lambdaFunctionProps is ignored. Default: - None
        :param lambda_function_props: User provided props to override the default props for the Lambda function. Default: - Default properties are used.

        summary:
        :summary:: Properties for the LambdaToStepFunction class.
        """
        if isinstance(state_machine_props, dict):
            state_machine_props = aws_cdk.aws_stepfunctions.StateMachineProps(
                **state_machine_props
            )
        if isinstance(lambda_function_props, dict):
            lambda_function_props = aws_cdk.aws_lambda.FunctionProps(
                **lambda_function_props
            )
        self._values = {
            "state_machine_props": state_machine_props,
        }
        if existing_lambda_obj is not None:
            self._values["existing_lambda_obj"] = existing_lambda_obj
        if lambda_function_props is not None:
            self._values["lambda_function_props"] = lambda_function_props

    @builtins.property
    def state_machine_props(self) -> aws_cdk.aws_stepfunctions.StateMachineProps:
        """User provided StateMachineProps to override the defaults.

        default
        :default: - None
        """
        return self._values.get("state_machine_props")

    @builtins.property
    def existing_lambda_obj(self) -> typing.Optional[aws_cdk.aws_lambda.Function]:
        """Existing instance of Lambda Function object, if this is set then the lambdaFunctionProps is ignored.

        default
        :default: - None
        """
        return self._values.get("existing_lambda_obj")

    @builtins.property
    def lambda_function_props(
        self,
    ) -> typing.Optional[aws_cdk.aws_lambda.FunctionProps]:
        """User provided props to override the default props for the Lambda function.

        default
        :default: - Default properties are used.
        """
        return self._values.get("lambda_function_props")

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LambdaToStepFunctionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "LambdaToStepFunction",
    "LambdaToStepFunctionProps",
]

publication.publish()
