"""
[![cloudcomponents Logo](https://raw.githubusercontent.com/cloudcomponents/cdk-constructs/master/logo.png)](https://github.com/cloudcomponents/cdk-constructs)

# @cloudcomponents/cdk-stripe-webhook

[![Build Status](https://travis-ci.org/cloudcomponents/cdk-constructs.svg?branch=master)](https://travis-ci.org/cloudcomponents/cdk-constructs)
[![cdkdx](https://img.shields.io/badge/buildtool-cdkdx-blue.svg)](https://github.com/hupe1980/cdkdx)
[![typescript](https://img.shields.io/badge/jsii-typescript-blueviolet.svg)](https://www.npmjs.com/package/@cloudcomponents/cdk-stripe-webhook)
[![python](https://img.shields.io/badge/jsii-python-blueviolet.svg)](https://pypi.org/project/cloudcomponents.cdk-stripe-webhook/)

> Create, update and delete stripe webhooks with your app deployment

## Install

TypeScript/JavaScript:

```bash
npm i @cloudcomponents/cdk-stripe-webhook
```

Python:

```bash
pip install cloudcomponents.cdk-stripe-webhook
```

## How to use

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
from aws_cdk.core import Construct, Stack, StackProps
from aws_cdk.aws_apigateway import RestApi
from cloudcomponents.cdk_stripe_webhook import StripeWebhook

class StripeWebhookStack(Stack):
    def __init__(self, scope, id, *, description=None, env=None, stackName=None, tags=None, synthesizer=None, terminationProtection=None):
        super().__init__(scope, id, description=description, env=env, stackName=stackName, tags=tags, synthesizer=synthesizer, terminationProtection=terminationProtection)

        api = RestApi(self, "Endpoint")
        api.root.add_method("POST")

        secret_key = process.env.SECRET_KEY

        events = ["charge.failed", "charge.succeeded"]

        StripeWebhook(self, "StripeWebhook",
            secret_key=secret_key,
            url=api.url,
            events=events,
            log_level="debug"
        )
```

## API Reference

See [API.md](https://github.com/cloudcomponents/cdk-constructs/tree/master/packages/cdk-stripe-webhook/API.md).

## Example

See more complete [examples](https://github.com/cloudcomponents/cdk-constructs/tree/master/examples).

## License

[MIT](https://github.com/cloudcomponents/cdk-constructs/tree/master/packages/cdk-stripe-webhook/LICENSE)
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


class StripeWebhook(
    aws_cdk.core.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cloudcomponents/cdk-stripe-webhook.StripeWebhook",
):
    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: str,
        *,
        events: typing.List[str],
        secret_key: str,
        url: str,
        log_level: typing.Optional[str] = None,
    ) -> None:
        """
        :param scope: -
        :param id: -
        :param events: -
        :param secret_key: -
        :param url: -
        :param log_level: -
        """
        props = StripeWebhookProps(
            events=events, secret_key=secret_key, url=url, log_level=log_level
        )

        jsii.create(StripeWebhook, self, [scope, id, props])


@jsii.data_type(
    jsii_type="@cloudcomponents/cdk-stripe-webhook.StripeWebhookProps",
    jsii_struct_bases=[],
    name_mapping={
        "events": "events",
        "secret_key": "secretKey",
        "url": "url",
        "log_level": "logLevel",
    },
)
class StripeWebhookProps:
    def __init__(
        self,
        *,
        events: typing.List[str],
        secret_key: str,
        url: str,
        log_level: typing.Optional[str] = None,
    ) -> None:
        """
        :param events: -
        :param secret_key: -
        :param url: -
        :param log_level: -
        """
        self._values = {
            "events": events,
            "secret_key": secret_key,
            "url": url,
        }
        if log_level is not None:
            self._values["log_level"] = log_level

    @builtins.property
    def events(self) -> typing.List[str]:
        return self._values.get("events")

    @builtins.property
    def secret_key(self) -> str:
        return self._values.get("secret_key")

    @builtins.property
    def url(self) -> str:
        return self._values.get("url")

    @builtins.property
    def log_level(self) -> typing.Optional[str]:
        return self._values.get("log_level")

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StripeWebhookProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "StripeWebhook",
    "StripeWebhookProps",
]

publication.publish()
