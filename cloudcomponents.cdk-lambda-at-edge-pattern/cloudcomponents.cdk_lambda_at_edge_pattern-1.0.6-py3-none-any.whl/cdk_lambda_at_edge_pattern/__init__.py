"""
[![cloudcomponents Logo](https://raw.githubusercontent.com/cloudcomponents/cdk-constructs/master/logo.png)](https://github.com/cloudcomponents/cdk-constructs)

# @cloudcomponents/cdk-lambda-at-edge-pattern

[![Build Status](https://travis-ci.org/cloudcomponents/cdk-constructs.svg?branch=master)](https://travis-ci.org/cloudcomponents/cdk-constructs)
[![cdkdx](https://img.shields.io/badge/buildtool-cdkdx-blue.svg)](https://github.com/hupe1980/cdkdx)
[![typescript](https://img.shields.io/badge/jsii-typescript-blueviolet.svg)](https://www.npmjs.com/package/@cloudcomponents/cdk-lambda-at-edge-pattern)
[![python](https://img.shields.io/badge/jsii-python-blueviolet.svg)](https://pypi.org/project/cloudcomponents.cdk-lambda-at-edge-pattern/)

> CDK Constructs for Lambda@Edge pattern: HttpHeaders

## Install

TypeScript/JavaScript:

```bash
npm i @cloudcomponents/cdk-lambda-at-edge-pattern
```

Python:

```bash
pip install cloudcomponents.cdk-lambda-at-edge-pattern
```

## How to use

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
from aws_cdk.core import Construct, RemovalPolicy, Stack, StackProps
from aws_cdk.aws_ssm import StringParameter
from aws_cdk.aws_cloudfront import SecurityPolicyProtocol
from cloudcomponents.cdk_static_website import StaticWebsite
from cloudcomponents.cdk_lambda_at_edge_pattern import HttpHeaders

class StaticWebsiteStack(Stack):
    def __init__(self, scope, id, *, description=None, env=None, stackName=None, tags=None, synthesizer=None, terminationProtection=None):
        super().__init__(scope, id, description=description, env=env, stackName=stackName, tags=tags, synthesizer=synthesizer, terminationProtection=terminationProtection)

        certificate_arn = StringParameter.value_from_lookup(self, "/certificate/cloudcomponents.org")

        website = StaticWebsite(self, "StaticWebsite",
            bucket_configuration=WebsiteBucketProps(
                removal_policy=RemovalPolicy.DESTROY
            ),
            alias_configuration=AliasProps(
                domain_name="cloudcomponents.org",
                names=["www.cloudcomponents.org", "cloudcomponents.org"],
                acm_cert_ref=certificate_arn
            )
        )

        # A us-east-1 stack is generated under the hood
        http_headers = HttpHeaders(self, "HttpHeaders",
            http_headers={
                "Content-Security-Policy": "default-src 'none'; img-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'; object-src 'none'; connect-src 'self'",
                "Strict-Transport-Security": "max-age=31536000; includeSubdomains; preload",
                "Referrer-Policy": "same-origin",
                "X-XSS-Protection": "1; mode=block",
                "X-Frame-Options": "DENY",
                "X-Content-Type-Options": "nosniff",
                "Cache-Control": "no-cache"
            }
        )

        website.add_lambda_function_association(http_headers)
```

### Cloudfront Distribution

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
cloudfront.Distribution(self, "myDist",
    default_behavior={
        "origin": origins.S3Origin(my_bucket),
        "edge_lambdas": [http_headers]
    }
)
```

### Cloudfront WebDistribution

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
cloudfront.CloudFrontWebDistribution(self, "MyDistribution",
    origin_configs=[{
        "s3_origin_source": {
            "s3_bucket_source": source_bucket
        },
        "behaviors": [{
            "is_default_behavior": True,
            "lambda_function_associations": [http_headers]
        }
        ]
    }
    ]
)
```

## API Reference

See [API.md](https://github.com/cloudcomponents/cdk-constructs/tree/master/packages/cdk-lambda-at-edge-pattern/API.md).

## Example

See more complete [examples](https://github.com/cloudcomponents/cdk-constructs/tree/master/examples).

## License

[MIT](https://github.com/cloudcomponents/cdk-constructs/tree/master/packages/cdk-lambda-at-edge-pattern/LICENSE)
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

import aws_cdk.aws_cloudfront
import aws_cdk.aws_iam
import aws_cdk.aws_lambda
import aws_cdk.core


class BaseEdgeConstruct(
    aws_cdk.core.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cloudcomponents/cdk-lambda-at-edge-pattern.BaseEdgeConstruct",
):
    def __init__(self, scope: aws_cdk.core.Construct, id: str) -> None:
        """
        :param scope: -
        :param id: -
        """
        jsii.create(BaseEdgeConstruct, self, [scope, id])

    @builtins.property
    @jsii.member(jsii_name="edgeStack")
    def _edge_stack(self) -> aws_cdk.core.Stack:
        return jsii.get(self, "edgeStack")

    @builtins.property
    @jsii.member(jsii_name="stack")
    def _stack(self) -> aws_cdk.core.Stack:
        return jsii.get(self, "stack")


@jsii.data_type(
    jsii_type="@cloudcomponents/cdk-lambda-at-edge-pattern.CommonEdgeFunctionProps",
    jsii_struct_bases=[],
    name_mapping={"edge_role": "edgeRole", "parameter_name": "parameterName"},
)
class CommonEdgeFunctionProps:
    def __init__(
        self,
        *,
        edge_role: typing.Optional["IEdgeRole"] = None,
        parameter_name: typing.Optional[str] = None,
    ) -> None:
        """
        :param edge_role: -
        :param parameter_name: The name of the parameter.
        """
        self._values = {}
        if edge_role is not None:
            self._values["edge_role"] = edge_role
        if parameter_name is not None:
            self._values["parameter_name"] = parameter_name

    @builtins.property
    def edge_role(self) -> typing.Optional["IEdgeRole"]:
        return self._values.get("edge_role")

    @builtins.property
    def parameter_name(self) -> typing.Optional[str]:
        """The name of the parameter."""
        return self._values.get("parameter_name")

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CommonEdgeFunctionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cloudcomponents/cdk-lambda-at-edge-pattern.Configuration",
    jsii_struct_bases=[],
    name_mapping={"log_level": "logLevel"},
)
class Configuration:
    def __init__(self, *, log_level: "LogLevel") -> None:
        """
        :param log_level: -
        """
        self._values = {
            "log_level": log_level,
        }

    @builtins.property
    def log_level(self) -> "LogLevel":
        return self._values.get("log_level")

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Configuration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cloudcomponents/cdk-lambda-at-edge-pattern.EdgeFunctionProps",
    jsii_struct_bases=[CommonEdgeFunctionProps],
    name_mapping={
        "edge_role": "edgeRole",
        "parameter_name": "parameterName",
        "code": "code",
        "configuration": "configuration",
        "event_type": "eventType",
        "name": "name",
    },
)
class EdgeFunctionProps(CommonEdgeFunctionProps):
    def __init__(
        self,
        *,
        edge_role: typing.Optional["IEdgeRole"] = None,
        parameter_name: typing.Optional[str] = None,
        code: aws_cdk.aws_lambda.Code,
        configuration: "Configuration",
        event_type: aws_cdk.aws_cloudfront.LambdaEdgeEventType,
        name: str,
    ) -> None:
        """
        :param edge_role: -
        :param parameter_name: The name of the parameter.
        :param code: -
        :param configuration: -
        :param event_type: -
        :param name: -
        """
        if isinstance(configuration, dict):
            configuration = Configuration(**configuration)
        self._values = {
            "code": code,
            "configuration": configuration,
            "event_type": event_type,
            "name": name,
        }
        if edge_role is not None:
            self._values["edge_role"] = edge_role
        if parameter_name is not None:
            self._values["parameter_name"] = parameter_name

    @builtins.property
    def edge_role(self) -> typing.Optional["IEdgeRole"]:
        return self._values.get("edge_role")

    @builtins.property
    def parameter_name(self) -> typing.Optional[str]:
        """The name of the parameter."""
        return self._values.get("parameter_name")

    @builtins.property
    def code(self) -> aws_cdk.aws_lambda.Code:
        return self._values.get("code")

    @builtins.property
    def configuration(self) -> "Configuration":
        return self._values.get("configuration")

    @builtins.property
    def event_type(self) -> aws_cdk.aws_cloudfront.LambdaEdgeEventType:
        return self._values.get("event_type")

    @builtins.property
    def name(self) -> str:
        return self._values.get("name")

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EdgeFunctionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cloudcomponents/cdk-lambda-at-edge-pattern.EdgeRoleProps",
    jsii_struct_bases=[],
    name_mapping={"role_name": "roleName"},
)
class EdgeRoleProps:
    def __init__(self, *, role_name: typing.Optional[str] = None) -> None:
        """
        :param role_name: -
        """
        self._values = {}
        if role_name is not None:
            self._values["role_name"] = role_name

    @builtins.property
    def role_name(self) -> typing.Optional[str]:
        return self._values.get("role_name")

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EdgeRoleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cloudcomponents/cdk-lambda-at-edge-pattern.HttpHeadersProps",
    jsii_struct_bases=[CommonEdgeFunctionProps],
    name_mapping={
        "edge_role": "edgeRole",
        "parameter_name": "parameterName",
        "http_headers": "httpHeaders",
        "log_level": "logLevel",
    },
)
class HttpHeadersProps(CommonEdgeFunctionProps):
    def __init__(
        self,
        *,
        edge_role: typing.Optional["IEdgeRole"] = None,
        parameter_name: typing.Optional[str] = None,
        http_headers: typing.Mapping[str, str],
        log_level: typing.Optional["LogLevel"] = None,
    ) -> None:
        """
        :param edge_role: -
        :param parameter_name: The name of the parameter.
        :param http_headers: -
        :param log_level: -
        """
        self._values = {
            "http_headers": http_headers,
        }
        if edge_role is not None:
            self._values["edge_role"] = edge_role
        if parameter_name is not None:
            self._values["parameter_name"] = parameter_name
        if log_level is not None:
            self._values["log_level"] = log_level

    @builtins.property
    def edge_role(self) -> typing.Optional["IEdgeRole"]:
        return self._values.get("edge_role")

    @builtins.property
    def parameter_name(self) -> typing.Optional[str]:
        """The name of the parameter."""
        return self._values.get("parameter_name")

    @builtins.property
    def http_headers(self) -> typing.Mapping[str, str]:
        return self._values.get("http_headers")

    @builtins.property
    def log_level(self) -> typing.Optional["LogLevel"]:
        return self._values.get("log_level")

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HttpHeadersProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="@cloudcomponents/cdk-lambda-at-edge-pattern.IEdgeLambda")
class IEdgeLambda(jsii.compat.Protocol):
    @builtins.staticmethod
    def __jsii_proxy_class__():
        return _IEdgeLambdaProxy

    @builtins.property
    @jsii.member(jsii_name="eventType")
    def event_type(self) -> aws_cdk.aws_cloudfront.LambdaEdgeEventType:
        ...

    @builtins.property
    @jsii.member(jsii_name="functionVersion")
    def function_version(self) -> aws_cdk.aws_lambda.IVersion:
        ...


class _IEdgeLambdaProxy:
    __jsii_type__ = "@cloudcomponents/cdk-lambda-at-edge-pattern.IEdgeLambda"

    @builtins.property
    @jsii.member(jsii_name="eventType")
    def event_type(self) -> aws_cdk.aws_cloudfront.LambdaEdgeEventType:
        return jsii.get(self, "eventType")

    @builtins.property
    @jsii.member(jsii_name="functionVersion")
    def function_version(self) -> aws_cdk.aws_lambda.IVersion:
        return jsii.get(self, "functionVersion")


@jsii.interface(jsii_type="@cloudcomponents/cdk-lambda-at-edge-pattern.IEdgeRole")
class IEdgeRole(jsii.compat.Protocol):
    @builtins.staticmethod
    def __jsii_proxy_class__():
        return _IEdgeRoleProxy

    @builtins.property
    @jsii.member(jsii_name="role")
    def role(self) -> aws_cdk.aws_iam.IRole:
        ...

    @jsii.member(jsii_name="addToEdgeRolePolicy")
    def add_to_edge_role_policy(
        self, statement: aws_cdk.aws_iam.PolicyStatement
    ) -> None:
        """
        :param statement: -
        """
        ...


class _IEdgeRoleProxy:
    __jsii_type__ = "@cloudcomponents/cdk-lambda-at-edge-pattern.IEdgeRole"

    @builtins.property
    @jsii.member(jsii_name="role")
    def role(self) -> aws_cdk.aws_iam.IRole:
        return jsii.get(self, "role")

    @jsii.member(jsii_name="addToEdgeRolePolicy")
    def add_to_edge_role_policy(
        self, statement: aws_cdk.aws_iam.PolicyStatement
    ) -> None:
        """
        :param statement: -
        """
        return jsii.invoke(self, "addToEdgeRolePolicy", [statement])


@jsii.interface(
    jsii_type="@cloudcomponents/cdk-lambda-at-edge-pattern.ILambdaFunctionAssociation"
)
class ILambdaFunctionAssociation(jsii.compat.Protocol):
    @builtins.staticmethod
    def __jsii_proxy_class__():
        return _ILambdaFunctionAssociationProxy

    @builtins.property
    @jsii.member(jsii_name="eventType")
    def event_type(self) -> aws_cdk.aws_cloudfront.LambdaEdgeEventType:
        ...

    @builtins.property
    @jsii.member(jsii_name="lambdaFunction")
    def lambda_function(self) -> aws_cdk.aws_lambda.IVersion:
        ...


class _ILambdaFunctionAssociationProxy:
    __jsii_type__ = (
        "@cloudcomponents/cdk-lambda-at-edge-pattern.ILambdaFunctionAssociation"
    )

    @builtins.property
    @jsii.member(jsii_name="eventType")
    def event_type(self) -> aws_cdk.aws_cloudfront.LambdaEdgeEventType:
        return jsii.get(self, "eventType")

    @builtins.property
    @jsii.member(jsii_name="lambdaFunction")
    def lambda_function(self) -> aws_cdk.aws_lambda.IVersion:
        return jsii.get(self, "lambdaFunction")


@jsii.enum(jsii_type="@cloudcomponents/cdk-lambda-at-edge-pattern.LogLevel")
class LogLevel(enum.Enum):
    NONE = "NONE"
    INFO = "INFO"
    WARN = "WARN"
    ERROR = "ERROR"
    DEBUG = "DEBUG"


class WithConfiguration(
    aws_cdk.core.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cloudcomponents/cdk-lambda-at-edge-pattern.WithConfiguration",
):
    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: str,
        *,
        configuration: "Configuration",
        function: aws_cdk.aws_lambda.IFunction,
    ) -> None:
        """
        :param scope: -
        :param id: -
        :param configuration: -
        :param function: -
        """
        props = WithConfigurationProps(configuration=configuration, function=function)

        jsii.create(WithConfiguration, self, [scope, id, props])

    @builtins.property
    @jsii.member(jsii_name="functionVersion")
    def function_version(self) -> aws_cdk.aws_lambda.IVersion:
        return jsii.get(self, "functionVersion")


@jsii.data_type(
    jsii_type="@cloudcomponents/cdk-lambda-at-edge-pattern.WithConfigurationProps",
    jsii_struct_bases=[],
    name_mapping={"configuration": "configuration", "function": "function"},
)
class WithConfigurationProps:
    def __init__(
        self, *, configuration: "Configuration", function: aws_cdk.aws_lambda.IFunction
    ) -> None:
        """
        :param configuration: -
        :param function: -
        """
        if isinstance(configuration, dict):
            configuration = Configuration(**configuration)
        self._values = {
            "configuration": configuration,
            "function": function,
        }

    @builtins.property
    def configuration(self) -> "Configuration":
        return self._values.get("configuration")

    @builtins.property
    def function(self) -> aws_cdk.aws_lambda.IFunction:
        return self._values.get("function")

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WithConfigurationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(ILambdaFunctionAssociation, IEdgeLambda)
class EdgeFunction(
    BaseEdgeConstruct,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cloudcomponents/cdk-lambda-at-edge-pattern.EdgeFunction",
):
    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: str,
        *,
        code: aws_cdk.aws_lambda.Code,
        configuration: "Configuration",
        event_type: aws_cdk.aws_cloudfront.LambdaEdgeEventType,
        name: str,
        edge_role: typing.Optional["IEdgeRole"] = None,
        parameter_name: typing.Optional[str] = None,
    ) -> None:
        """
        :param scope: -
        :param id: -
        :param code: -
        :param configuration: -
        :param event_type: -
        :param name: -
        :param edge_role: -
        :param parameter_name: The name of the parameter.
        """
        props = EdgeFunctionProps(
            code=code,
            configuration=configuration,
            event_type=event_type,
            name=name,
            edge_role=edge_role,
            parameter_name=parameter_name,
        )

        jsii.create(EdgeFunction, self, [scope, id, props])

    @builtins.property
    @jsii.member(jsii_name="edgeRole")
    def edge_role(self) -> "IEdgeRole":
        return jsii.get(self, "edgeRole")

    @builtins.property
    @jsii.member(jsii_name="eventType")
    def event_type(self) -> aws_cdk.aws_cloudfront.LambdaEdgeEventType:
        return jsii.get(self, "eventType")

    @builtins.property
    @jsii.member(jsii_name="functionVersion")
    def function_version(self) -> aws_cdk.aws_lambda.IVersion:
        return jsii.get(self, "functionVersion")

    @builtins.property
    @jsii.member(jsii_name="lambdaFunction")
    def lambda_function(self) -> aws_cdk.aws_lambda.IVersion:
        return jsii.get(self, "lambdaFunction")


@jsii.implements(IEdgeRole)
class EdgeRole(
    BaseEdgeConstruct,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cloudcomponents/cdk-lambda-at-edge-pattern.EdgeRole",
):
    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: str,
        *,
        role_name: typing.Optional[str] = None,
    ) -> None:
        """
        :param scope: -
        :param id: -
        :param role_name: -
        """
        props = EdgeRoleProps(role_name=role_name)

        jsii.create(EdgeRole, self, [scope, id, props])

    @jsii.member(jsii_name="addToEdgeRolePolicy")
    def add_to_edge_role_policy(
        self, statement: aws_cdk.aws_iam.PolicyStatement
    ) -> None:
        """
        :param statement: -
        """
        return jsii.invoke(self, "addToEdgeRolePolicy", [statement])

    @builtins.property
    @jsii.member(jsii_name="role")
    def role(self) -> aws_cdk.aws_iam.IRole:
        return jsii.get(self, "role")


class HttpHeaders(
    EdgeFunction,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cloudcomponents/cdk-lambda-at-edge-pattern.HttpHeaders",
):
    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: str,
        *,
        http_headers: typing.Mapping[str, str],
        log_level: typing.Optional["LogLevel"] = None,
        edge_role: typing.Optional["IEdgeRole"] = None,
        parameter_name: typing.Optional[str] = None,
    ) -> None:
        """
        :param scope: -
        :param id: -
        :param http_headers: -
        :param log_level: -
        :param edge_role: -
        :param parameter_name: The name of the parameter.
        """
        props = HttpHeadersProps(
            http_headers=http_headers,
            log_level=log_level,
            edge_role=edge_role,
            parameter_name=parameter_name,
        )

        jsii.create(HttpHeaders, self, [scope, id, props])


__all__ = [
    "BaseEdgeConstruct",
    "CommonEdgeFunctionProps",
    "Configuration",
    "EdgeFunction",
    "EdgeFunctionProps",
    "EdgeRole",
    "EdgeRoleProps",
    "HttpHeaders",
    "HttpHeadersProps",
    "IEdgeLambda",
    "IEdgeRole",
    "ILambdaFunctionAssociation",
    "LogLevel",
    "WithConfiguration",
    "WithConfigurationProps",
]

publication.publish()
