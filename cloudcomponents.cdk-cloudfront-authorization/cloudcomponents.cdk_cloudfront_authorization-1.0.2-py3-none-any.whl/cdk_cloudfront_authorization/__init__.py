"""
[![cloudcomponents Logo](https://raw.githubusercontent.com/cloudcomponents/cdk-constructs/master/logo.png)](https://github.com/cloudcomponents/cdk-constructs)

# @cloudcomponents/cdk-cloudfront-authorization

[![Build Status](https://travis-ci.org/cloudcomponents/cdk-constructs.svg?branch=master)](https://travis-ci.org/cloudcomponents/cdk-constructs)
[![cdkdx](https://img.shields.io/badge/buildtool-cdkdx-blue.svg)](https://github.com/hupe1980/cdkdx)
[![typescript](https://img.shields.io/badge/jsii-typescript-blueviolet.svg)](https://www.npmjs.com/package/@cloudcomponents/cdk-cloudfront-authorization)
[![python](https://img.shields.io/badge/jsii-python-blueviolet.svg)](https://pypi.org/project/cloudcomponents.cdk-cloudfront-authorization/)

> CloudFront with Cognito authentication using Lambda@Edge

This construct is based on https://github.com/aws-samples/cloudfront-authorization-at-edge.

## Install

TypeScript/JavaScript:

```bash
npm i @cloudcomponents/cdk-cloudfront-authorization
```

Python:

```bash
pip install cloudcomponents.cdk-cloudfront-authorization
```

## How to use SPA

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
from aws_cdk.core import Construct, Stack, StackProps
from aws_cdk.aws_cognito import UserPool
from cloudcomponents.cdk_cloudfront_authorization import SpaAuthorization, SpaDistribution

class CloudFrontAuthorizationStack(Stack):
    def __init__(self, scope, id, *, description=None, env=None, stackName=None, tags=None, synthesizer=None, terminationProtection=None):
        super().__init__(scope, id, description=description, env=env, stackName=stackName, tags=tags, synthesizer=synthesizer, terminationProtection=terminationProtection)

        user_pool = UserPool(self, "UserPool",
            self_sign_up_enabled=False,
            user_pool_name="cloudfront-authorization-userpool"
        )

        # UserPool must have a domain!
        user_pool.add_domain("Domain",
            cognito_domain=CognitoDomainOptions(
                domain_prefix="cloudcomponents"
            )
        )

        authorization = SpaAuthorization(self, "Authorization",
            user_pool=user_pool
        )

        SpaDistribution(self, "Distribution",
            authorization=authorization
        )
```

## How to use StaticSite

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
from aws_cdk.core import Construct, Stack, StackProps
from aws_cdk.aws_cognito import UserPool
from cloudcomponents.cdk_cloudfront_authorization import StaticSiteAuthorization, StaticSiteDistribution

class CloudFrontAuthorizationStack(Stack):
    def __init__(self, scope, id, *, description=None, env=None, stackName=None, tags=None, synthesizer=None, terminationProtection=None):
        super().__init__(scope, id, description=description, env=env, stackName=stackName, tags=tags, synthesizer=synthesizer, terminationProtection=terminationProtection)

        user_pool = UserPool(self, "UserPool",
            self_sign_up_enabled=False,
            user_pool_name="cloudfront-authorization-userpool"
        )

        # UserPool must have a domain!
        user_pool.add_domain("Domain",
            cognito_domain=CognitoDomainOptions(
                domain_prefix="cloudcomponents"
            )
        )

        authorization = StaticSiteAuthorization(self, "Authorization",
            user_pool=user_pool
        )

        StaticSiteDistribution(self, "Distribution",
            authorization=authorization
        )
```

## Legacy CloudFrontWebDistribution

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
from aws_cdk.aws_cloudfront import CloudFrontWebDistribution, OriginAccessIdentity
from aws_cdk.aws_cognito import UserPool
from aws_cdk.core import Construct, Stack, StackProps
from cloudcomponents.cdk_cloudfront_authorization import SpaAuthorization
from cloudcomponents.cdk_deletable_bucket import DeletableBucket

class CloudFrontAuthorizationStack(Stack):
    def __init__(self, scope, id, *, description=None, env=None, stackName=None, tags=None, synthesizer=None, terminationProtection=None):
        super().__init__(scope, id, description=description, env=env, stackName=stackName, tags=tags, synthesizer=synthesizer, terminationProtection=terminationProtection)

        user_pool = UserPool(self, "UserPool",
            self_sign_up_enabled=False,
            user_pool_name="cloudfront-authorization-userpool"
        )

        user_pool.add_domain("Domain",
            cognito_domain=CognitoDomainOptions(
                domain_prefix="cloudcomponents"
            )
        )

        authorization = SpaAuthorization(self, "Authorization",
            user_pool=user_pool
        )

        bucket = DeletableBucket(self, "Bucket",
            force_delete=True
        )

        origin_access_identity = OriginAccessIdentity(self, "OriginAccessIdentity",
            comment=f"CloudFront OriginAccessIdentity for {bucket.bucketName}"
        )

        CloudFrontWebDistribution(self, "Distribution",
            origin_configs=[SourceConfiguration(
                s3_origin_source=S3OriginConfig(
                    s3_bucket_source=bucket,
                    origin_access_identity=origin_access_identity
                ),
                behaviors=[authorization.create_legacy_default_behavior(), (SpreadElement ...authorization.createLegacyAdditionalBehaviors()
                  authorization.create_legacy_additional_behaviors())]
            )
            ]
        )
```

## SPA mode vs. Static Site mode

### SPA

* User Pool client does not use a client secret
* The cookies with JWT's are not "http only", so that they can be read and used by the SPA (e.g. to display the user name, or to refresh tokens)
* 404's (page not found on S3) will return index.html, to enable SPA-routing

### Static Site

* Enforce use of a client secret
* Set cookies to be http only by default (unless you've provided other cookie settings explicitly)
* No special error handling

## API Reference

See [API.md](https://github.com/cloudcomponents/cdk-constructs/tree/master/packages/cdk-cloudfront-authorization/API.md).

## Example

See more complete [examples](https://github.com/cloudcomponents/cdk-constructs/tree/master/examples).

## License

[MIT](https://github.com/cloudcomponents/cdk-constructs/tree/master/packages/cdk-cloudfront-authorization/LICENSE)
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

import aws_cdk.aws_certificatemanager
import aws_cdk.aws_cloudfront
import aws_cdk.aws_cognito
import aws_cdk.core
import cloudcomponents.cdk_lambda_at_edge_pattern


class AuthFlow(
    aws_cdk.core.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cloudcomponents/cdk-cloudfront-authorization.AuthFlow",
):
    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: str,
        *,
        cognito_auth_domain: str,
        cookie_settings: typing.Mapping[str, str],
        http_headers: typing.Mapping[str, str],
        log_level: cloudcomponents.cdk_lambda_at_edge_pattern.LogLevel,
        nonce_signing_secret: str,
        oauth_scopes: typing.List[aws_cdk.aws_cognito.OAuthScope],
        redirect_paths: "RedirectPaths",
        user_pool: aws_cdk.aws_cognito.IUserPool,
        user_pool_client: aws_cdk.aws_cognito.IUserPoolClient,
        client_secret: typing.Optional[str] = None,
    ) -> None:
        """
        :param scope: -
        :param id: -
        :param cognito_auth_domain: -
        :param cookie_settings: -
        :param http_headers: -
        :param log_level: -
        :param nonce_signing_secret: -
        :param oauth_scopes: -
        :param redirect_paths: -
        :param user_pool: -
        :param user_pool_client: -
        :param client_secret: -
        """
        props = AuthFlowProps(
            cognito_auth_domain=cognito_auth_domain,
            cookie_settings=cookie_settings,
            http_headers=http_headers,
            log_level=log_level,
            nonce_signing_secret=nonce_signing_secret,
            oauth_scopes=oauth_scopes,
            redirect_paths=redirect_paths,
            user_pool=user_pool,
            user_pool_client=user_pool_client,
            client_secret=client_secret,
        )

        jsii.create(AuthFlow, self, [scope, id, props])

    @builtins.property
    @jsii.member(jsii_name="checkAuth")
    def check_auth(self) -> cloudcomponents.cdk_lambda_at_edge_pattern.EdgeFunction:
        return jsii.get(self, "checkAuth")

    @builtins.property
    @jsii.member(jsii_name="httpHeaders")
    def http_headers(self) -> cloudcomponents.cdk_lambda_at_edge_pattern.EdgeFunction:
        return jsii.get(self, "httpHeaders")

    @builtins.property
    @jsii.member(jsii_name="parseAuth")
    def parse_auth(self) -> cloudcomponents.cdk_lambda_at_edge_pattern.EdgeFunction:
        return jsii.get(self, "parseAuth")

    @builtins.property
    @jsii.member(jsii_name="refreshAuth")
    def refresh_auth(self) -> cloudcomponents.cdk_lambda_at_edge_pattern.EdgeFunction:
        return jsii.get(self, "refreshAuth")

    @builtins.property
    @jsii.member(jsii_name="signOut")
    def sign_out(self) -> cloudcomponents.cdk_lambda_at_edge_pattern.EdgeFunction:
        return jsii.get(self, "signOut")


@jsii.data_type(
    jsii_type="@cloudcomponents/cdk-cloudfront-authorization.AuthFlowProps",
    jsii_struct_bases=[],
    name_mapping={
        "cognito_auth_domain": "cognitoAuthDomain",
        "cookie_settings": "cookieSettings",
        "http_headers": "httpHeaders",
        "log_level": "logLevel",
        "nonce_signing_secret": "nonceSigningSecret",
        "oauth_scopes": "oauthScopes",
        "redirect_paths": "redirectPaths",
        "user_pool": "userPool",
        "user_pool_client": "userPoolClient",
        "client_secret": "clientSecret",
    },
)
class AuthFlowProps:
    def __init__(
        self,
        *,
        cognito_auth_domain: str,
        cookie_settings: typing.Mapping[str, str],
        http_headers: typing.Mapping[str, str],
        log_level: cloudcomponents.cdk_lambda_at_edge_pattern.LogLevel,
        nonce_signing_secret: str,
        oauth_scopes: typing.List[aws_cdk.aws_cognito.OAuthScope],
        redirect_paths: "RedirectPaths",
        user_pool: aws_cdk.aws_cognito.IUserPool,
        user_pool_client: aws_cdk.aws_cognito.IUserPoolClient,
        client_secret: typing.Optional[str] = None,
    ) -> None:
        """
        :param cognito_auth_domain: -
        :param cookie_settings: -
        :param http_headers: -
        :param log_level: -
        :param nonce_signing_secret: -
        :param oauth_scopes: -
        :param redirect_paths: -
        :param user_pool: -
        :param user_pool_client: -
        :param client_secret: -
        """
        if isinstance(redirect_paths, dict):
            redirect_paths = RedirectPaths(**redirect_paths)
        self._values = {
            "cognito_auth_domain": cognito_auth_domain,
            "cookie_settings": cookie_settings,
            "http_headers": http_headers,
            "log_level": log_level,
            "nonce_signing_secret": nonce_signing_secret,
            "oauth_scopes": oauth_scopes,
            "redirect_paths": redirect_paths,
            "user_pool": user_pool,
            "user_pool_client": user_pool_client,
        }
        if client_secret is not None:
            self._values["client_secret"] = client_secret

    @builtins.property
    def cognito_auth_domain(self) -> str:
        return self._values.get("cognito_auth_domain")

    @builtins.property
    def cookie_settings(self) -> typing.Mapping[str, str]:
        return self._values.get("cookie_settings")

    @builtins.property
    def http_headers(self) -> typing.Mapping[str, str]:
        return self._values.get("http_headers")

    @builtins.property
    def log_level(self) -> cloudcomponents.cdk_lambda_at_edge_pattern.LogLevel:
        return self._values.get("log_level")

    @builtins.property
    def nonce_signing_secret(self) -> str:
        return self._values.get("nonce_signing_secret")

    @builtins.property
    def oauth_scopes(self) -> typing.List[aws_cdk.aws_cognito.OAuthScope]:
        return self._values.get("oauth_scopes")

    @builtins.property
    def redirect_paths(self) -> "RedirectPaths":
        return self._values.get("redirect_paths")

    @builtins.property
    def user_pool(self) -> aws_cdk.aws_cognito.IUserPool:
        return self._values.get("user_pool")

    @builtins.property
    def user_pool_client(self) -> aws_cdk.aws_cognito.IUserPoolClient:
        return self._values.get("user_pool_client")

    @builtins.property
    def client_secret(self) -> typing.Optional[str]:
        return self._values.get("client_secret")

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AuthFlowProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Authorization(
    aws_cdk.core.Construct,
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="@cloudcomponents/cdk-cloudfront-authorization.Authorization",
):
    @builtins.staticmethod
    def __jsii_proxy_class__():
        return _AuthorizationProxy

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: str,
        *,
        user_pool: aws_cdk.aws_cognito.IUserPool,
        cookie_settings: typing.Optional[typing.Mapping[str, str]] = None,
        http_headers: typing.Optional[typing.Mapping[str, str]] = None,
        log_level: typing.Optional[
            cloudcomponents.cdk_lambda_at_edge_pattern.LogLevel
        ] = None,
        oauth_scopes: typing.Optional[
            typing.List[aws_cdk.aws_cognito.OAuthScope]
        ] = None,
        redirect_paths: typing.Optional["RedirectPaths"] = None,
        sign_out_url: typing.Optional[str] = None,
    ) -> None:
        """
        :param scope: -
        :param id: -
        :param user_pool: -
        :param cookie_settings: -
        :param http_headers: -
        :param log_level: -
        :param oauth_scopes: -
        :param redirect_paths: -
        :param sign_out_url: -
        """
        props = AuthorizationProps(
            user_pool=user_pool,
            cookie_settings=cookie_settings,
            http_headers=http_headers,
            log_level=log_level,
            oauth_scopes=oauth_scopes,
            redirect_paths=redirect_paths,
            sign_out_url=sign_out_url,
        )

        jsii.create(Authorization, self, [scope, id, props])

    @jsii.member(jsii_name="createAdditionalBehaviors")
    def create_additional_behaviors(
        self, origin: aws_cdk.aws_cloudfront.IOrigin
    ) -> typing.Mapping[str, aws_cdk.aws_cloudfront.BehaviorOptions]:
        """
        :param origin: -
        """
        return jsii.invoke(self, "createAdditionalBehaviors", [origin])

    @jsii.member(jsii_name="createAuthFlow")
    @abc.abstractmethod
    def _create_auth_flow(
        self, log_level: cloudcomponents.cdk_lambda_at_edge_pattern.LogLevel
    ) -> "AuthFlow":
        """
        :param log_level: -
        """
        ...

    @jsii.member(jsii_name="createDefaultBehavior")
    def create_default_behavior(
        self, origin: aws_cdk.aws_cloudfront.IOrigin
    ) -> aws_cdk.aws_cloudfront.BehaviorOptions:
        """
        :param origin: -
        """
        return jsii.invoke(self, "createDefaultBehavior", [origin])

    @jsii.member(jsii_name="createLegacyAdditionalBehaviors")
    def create_legacy_additional_behaviors(
        self,
    ) -> typing.List[aws_cdk.aws_cloudfront.Behavior]:
        return jsii.invoke(self, "createLegacyAdditionalBehaviors", [])

    @jsii.member(jsii_name="createLegacyDefaultBehavior")
    def create_legacy_default_behavior(self) -> aws_cdk.aws_cloudfront.Behavior:
        return jsii.invoke(self, "createLegacyDefaultBehavior", [])

    @jsii.member(jsii_name="createUserPoolClient")
    @abc.abstractmethod
    def _create_user_pool_client(self) -> aws_cdk.aws_cognito.IUserPoolClient:
        ...

    @jsii.member(jsii_name="updateUserPoolClientCallbacks")
    def update_user_pool_client_callbacks(
        self, *, callback_urls: typing.List[str], logout_urls: typing.List[str]
    ) -> None:
        """
        :param callback_urls: A list of allowed redirect (callback) URLs for the identity providers.
        :param logout_urls: A list of allowed logout URLs for the identity providers.
        """
        redirects = UserPoolClientCallbackUrls(
            callback_urls=callback_urls, logout_urls=logout_urls
        )

        return jsii.invoke(self, "updateUserPoolClientCallbacks", [redirects])

    @builtins.property
    @jsii.member(jsii_name="authFlow")
    def auth_flow(self) -> "AuthFlow":
        return jsii.get(self, "authFlow")

    @builtins.property
    @jsii.member(jsii_name="cognitoAuthDomain")
    def _cognito_auth_domain(self) -> str:
        return jsii.get(self, "cognitoAuthDomain")

    @builtins.property
    @jsii.member(jsii_name="httpHeaders")
    def _http_headers(self) -> typing.Mapping[str, str]:
        return jsii.get(self, "httpHeaders")

    @builtins.property
    @jsii.member(jsii_name="nonceSigningSecret")
    def _nonce_signing_secret(self) -> str:
        return jsii.get(self, "nonceSigningSecret")

    @builtins.property
    @jsii.member(jsii_name="oauthScopes")
    def _oauth_scopes(self) -> typing.List[aws_cdk.aws_cognito.OAuthScope]:
        return jsii.get(self, "oauthScopes")

    @builtins.property
    @jsii.member(jsii_name="redirectPaths")
    def redirect_paths(self) -> "RedirectPaths":
        return jsii.get(self, "redirectPaths")

    @builtins.property
    @jsii.member(jsii_name="signOutUrlPath")
    def sign_out_url_path(self) -> str:
        return jsii.get(self, "signOutUrlPath")

    @builtins.property
    @jsii.member(jsii_name="userPool")
    def _user_pool(self) -> aws_cdk.aws_cognito.IUserPool:
        return jsii.get(self, "userPool")

    @builtins.property
    @jsii.member(jsii_name="userPoolClient")
    def _user_pool_client(self) -> aws_cdk.aws_cognito.IUserPoolClient:
        return jsii.get(self, "userPoolClient")

    @builtins.property
    @jsii.member(jsii_name="cookieSettings")
    def _cookie_settings(self) -> typing.Optional[typing.Mapping[str, str]]:
        return jsii.get(self, "cookieSettings")


class _AuthorizationProxy(Authorization):
    @jsii.member(jsii_name="createAuthFlow")
    def _create_auth_flow(
        self, log_level: cloudcomponents.cdk_lambda_at_edge_pattern.LogLevel
    ) -> "AuthFlow":
        """
        :param log_level: -
        """
        return jsii.invoke(self, "createAuthFlow", [log_level])

    @jsii.member(jsii_name="createUserPoolClient")
    def _create_user_pool_client(self) -> aws_cdk.aws_cognito.IUserPoolClient:
        return jsii.invoke(self, "createUserPoolClient", [])


@jsii.data_type(
    jsii_type="@cloudcomponents/cdk-cloudfront-authorization.AuthorizationProps",
    jsii_struct_bases=[],
    name_mapping={
        "user_pool": "userPool",
        "cookie_settings": "cookieSettings",
        "http_headers": "httpHeaders",
        "log_level": "logLevel",
        "oauth_scopes": "oauthScopes",
        "redirect_paths": "redirectPaths",
        "sign_out_url": "signOutUrl",
    },
)
class AuthorizationProps:
    def __init__(
        self,
        *,
        user_pool: aws_cdk.aws_cognito.IUserPool,
        cookie_settings: typing.Optional[typing.Mapping[str, str]] = None,
        http_headers: typing.Optional[typing.Mapping[str, str]] = None,
        log_level: typing.Optional[
            cloudcomponents.cdk_lambda_at_edge_pattern.LogLevel
        ] = None,
        oauth_scopes: typing.Optional[
            typing.List[aws_cdk.aws_cognito.OAuthScope]
        ] = None,
        redirect_paths: typing.Optional["RedirectPaths"] = None,
        sign_out_url: typing.Optional[str] = None,
    ) -> None:
        """
        :param user_pool: -
        :param cookie_settings: -
        :param http_headers: -
        :param log_level: -
        :param oauth_scopes: -
        :param redirect_paths: -
        :param sign_out_url: -
        """
        if isinstance(redirect_paths, dict):
            redirect_paths = RedirectPaths(**redirect_paths)
        self._values = {
            "user_pool": user_pool,
        }
        if cookie_settings is not None:
            self._values["cookie_settings"] = cookie_settings
        if http_headers is not None:
            self._values["http_headers"] = http_headers
        if log_level is not None:
            self._values["log_level"] = log_level
        if oauth_scopes is not None:
            self._values["oauth_scopes"] = oauth_scopes
        if redirect_paths is not None:
            self._values["redirect_paths"] = redirect_paths
        if sign_out_url is not None:
            self._values["sign_out_url"] = sign_out_url

    @builtins.property
    def user_pool(self) -> aws_cdk.aws_cognito.IUserPool:
        return self._values.get("user_pool")

    @builtins.property
    def cookie_settings(self) -> typing.Optional[typing.Mapping[str, str]]:
        return self._values.get("cookie_settings")

    @builtins.property
    def http_headers(self) -> typing.Optional[typing.Mapping[str, str]]:
        return self._values.get("http_headers")

    @builtins.property
    def log_level(
        self,
    ) -> typing.Optional[cloudcomponents.cdk_lambda_at_edge_pattern.LogLevel]:
        return self._values.get("log_level")

    @builtins.property
    def oauth_scopes(
        self,
    ) -> typing.Optional[typing.List[aws_cdk.aws_cognito.OAuthScope]]:
        return self._values.get("oauth_scopes")

    @builtins.property
    def redirect_paths(self) -> typing.Optional["RedirectPaths"]:
        return self._values.get("redirect_paths")

    @builtins.property
    def sign_out_url(self) -> typing.Optional[str]:
        return self._values.get("sign_out_url")

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AuthorizationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class BaseDistribution(
    aws_cdk.core.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cloudcomponents/cdk-cloudfront-authorization.BaseDistribution",
):
    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: str,
        *,
        authorization: "IAuthorization",
        error_responses: typing.Optional[
            typing.List[aws_cdk.aws_cloudfront.ErrorResponse]
        ] = None,
        certificate: typing.Optional[
            aws_cdk.aws_certificatemanager.ICertificate
        ] = None,
        origin: typing.Optional[aws_cdk.aws_cloudfront.IOrigin] = None,
        price_class: typing.Optional[aws_cdk.aws_cloudfront.PriceClass] = None,
        removal_policy: typing.Optional[aws_cdk.core.RemovalPolicy] = None,
    ) -> None:
        """
        :param scope: -
        :param id: -
        :param authorization: -
        :param error_responses: -
        :param certificate: -
        :param origin: -
        :param price_class: -
        :param removal_policy: -
        """
        props = BaseDistributionProps(
            authorization=authorization,
            error_responses=error_responses,
            certificate=certificate,
            origin=origin,
            price_class=price_class,
            removal_policy=removal_policy,
        )

        jsii.create(BaseDistribution, self, [scope, id, props])


@jsii.data_type(
    jsii_type="@cloudcomponents/cdk-cloudfront-authorization.CommonDistributionProps",
    jsii_struct_bases=[],
    name_mapping={
        "certificate": "certificate",
        "origin": "origin",
        "price_class": "priceClass",
        "removal_policy": "removalPolicy",
    },
)
class CommonDistributionProps:
    def __init__(
        self,
        *,
        certificate: typing.Optional[
            aws_cdk.aws_certificatemanager.ICertificate
        ] = None,
        origin: typing.Optional[aws_cdk.aws_cloudfront.IOrigin] = None,
        price_class: typing.Optional[aws_cdk.aws_cloudfront.PriceClass] = None,
        removal_policy: typing.Optional[aws_cdk.core.RemovalPolicy] = None,
    ) -> None:
        """
        :param certificate: -
        :param origin: -
        :param price_class: -
        :param removal_policy: -
        """
        self._values = {}
        if certificate is not None:
            self._values["certificate"] = certificate
        if origin is not None:
            self._values["origin"] = origin
        if price_class is not None:
            self._values["price_class"] = price_class
        if removal_policy is not None:
            self._values["removal_policy"] = removal_policy

    @builtins.property
    def certificate(
        self,
    ) -> typing.Optional[aws_cdk.aws_certificatemanager.ICertificate]:
        return self._values.get("certificate")

    @builtins.property
    def origin(self) -> typing.Optional[aws_cdk.aws_cloudfront.IOrigin]:
        return self._values.get("origin")

    @builtins.property
    def price_class(self) -> typing.Optional[aws_cdk.aws_cloudfront.PriceClass]:
        return self._values.get("price_class")

    @builtins.property
    def removal_policy(self) -> typing.Optional[aws_cdk.core.RemovalPolicy]:
        return self._values.get("removal_policy")

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CommonDistributionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(
    jsii_type="@cloudcomponents/cdk-cloudfront-authorization.IAuthorization"
)
class IAuthorization(jsii.compat.Protocol):
    @builtins.staticmethod
    def __jsii_proxy_class__():
        return _IAuthorizationProxy

    @builtins.property
    @jsii.member(jsii_name="redirectPaths")
    def redirect_paths(self) -> "RedirectPaths":
        ...

    @builtins.property
    @jsii.member(jsii_name="signOutUrlPath")
    def sign_out_url_path(self) -> str:
        ...

    @jsii.member(jsii_name="createAdditionalBehaviors")
    def create_additional_behaviors(
        self, origin: aws_cdk.aws_cloudfront.IOrigin
    ) -> typing.Mapping[str, aws_cdk.aws_cloudfront.BehaviorOptions]:
        """
        :param origin: -
        """
        ...

    @jsii.member(jsii_name="createDefaultBehavior")
    def create_default_behavior(
        self, origin: aws_cdk.aws_cloudfront.IOrigin
    ) -> aws_cdk.aws_cloudfront.BehaviorOptions:
        """
        :param origin: -
        """
        ...

    @jsii.member(jsii_name="createLegacyAdditionalBehaviors")
    def create_legacy_additional_behaviors(
        self,
    ) -> typing.List[aws_cdk.aws_cloudfront.Behavior]:
        ...

    @jsii.member(jsii_name="createLegacyDefaultBehavior")
    def create_legacy_default_behavior(self) -> aws_cdk.aws_cloudfront.Behavior:
        ...

    @jsii.member(jsii_name="updateUserPoolClientCallbacks")
    def update_user_pool_client_callbacks(
        self, *, callback_urls: typing.List[str], logout_urls: typing.List[str]
    ) -> None:
        """
        :param callback_urls: A list of allowed redirect (callback) URLs for the identity providers.
        :param logout_urls: A list of allowed logout URLs for the identity providers.
        """
        ...


class _IAuthorizationProxy:
    __jsii_type__ = "@cloudcomponents/cdk-cloudfront-authorization.IAuthorization"

    @builtins.property
    @jsii.member(jsii_name="redirectPaths")
    def redirect_paths(self) -> "RedirectPaths":
        return jsii.get(self, "redirectPaths")

    @builtins.property
    @jsii.member(jsii_name="signOutUrlPath")
    def sign_out_url_path(self) -> str:
        return jsii.get(self, "signOutUrlPath")

    @jsii.member(jsii_name="createAdditionalBehaviors")
    def create_additional_behaviors(
        self, origin: aws_cdk.aws_cloudfront.IOrigin
    ) -> typing.Mapping[str, aws_cdk.aws_cloudfront.BehaviorOptions]:
        """
        :param origin: -
        """
        return jsii.invoke(self, "createAdditionalBehaviors", [origin])

    @jsii.member(jsii_name="createDefaultBehavior")
    def create_default_behavior(
        self, origin: aws_cdk.aws_cloudfront.IOrigin
    ) -> aws_cdk.aws_cloudfront.BehaviorOptions:
        """
        :param origin: -
        """
        return jsii.invoke(self, "createDefaultBehavior", [origin])

    @jsii.member(jsii_name="createLegacyAdditionalBehaviors")
    def create_legacy_additional_behaviors(
        self,
    ) -> typing.List[aws_cdk.aws_cloudfront.Behavior]:
        return jsii.invoke(self, "createLegacyAdditionalBehaviors", [])

    @jsii.member(jsii_name="createLegacyDefaultBehavior")
    def create_legacy_default_behavior(self) -> aws_cdk.aws_cloudfront.Behavior:
        return jsii.invoke(self, "createLegacyDefaultBehavior", [])

    @jsii.member(jsii_name="updateUserPoolClientCallbacks")
    def update_user_pool_client_callbacks(
        self, *, callback_urls: typing.List[str], logout_urls: typing.List[str]
    ) -> None:
        """
        :param callback_urls: A list of allowed redirect (callback) URLs for the identity providers.
        :param logout_urls: A list of allowed logout URLs for the identity providers.
        """
        redirects = UserPoolClientCallbackUrls(
            callback_urls=callback_urls, logout_urls=logout_urls
        )

        return jsii.invoke(self, "updateUserPoolClientCallbacks", [redirects])


@jsii.interface(
    jsii_type="@cloudcomponents/cdk-cloudfront-authorization.ISpaAuthorization"
)
class ISpaAuthorization(IAuthorization, jsii.compat.Protocol):
    @builtins.staticmethod
    def __jsii_proxy_class__():
        return _ISpaAuthorizationProxy

    @builtins.property
    @jsii.member(jsii_name="mode")
    def mode(self) -> "Mode":
        ...


class _ISpaAuthorizationProxy(jsii.proxy_for(IAuthorization)):
    __jsii_type__ = "@cloudcomponents/cdk-cloudfront-authorization.ISpaAuthorization"

    @builtins.property
    @jsii.member(jsii_name="mode")
    def mode(self) -> "Mode":
        return jsii.get(self, "mode")


@jsii.interface(
    jsii_type="@cloudcomponents/cdk-cloudfront-authorization.IStaticSiteAuthorization"
)
class IStaticSiteAuthorization(IAuthorization, jsii.compat.Protocol):
    @builtins.staticmethod
    def __jsii_proxy_class__():
        return _IStaticSiteAuthorizationProxy

    @builtins.property
    @jsii.member(jsii_name="mode")
    def mode(self) -> "Mode":
        ...


class _IStaticSiteAuthorizationProxy(jsii.proxy_for(IAuthorization)):
    __jsii_type__ = (
        "@cloudcomponents/cdk-cloudfront-authorization.IStaticSiteAuthorization"
    )

    @builtins.property
    @jsii.member(jsii_name="mode")
    def mode(self) -> "Mode":
        return jsii.get(self, "mode")


@jsii.enum(jsii_type="@cloudcomponents/cdk-cloudfront-authorization.Mode")
class Mode(enum.Enum):
    SPA = "SPA"
    STATIC_SITE = "STATIC_SITE"


@jsii.data_type(
    jsii_type="@cloudcomponents/cdk-cloudfront-authorization.RedirectPaths",
    jsii_struct_bases=[],
    name_mapping={
        "auth_refresh": "authRefresh",
        "sign_in": "signIn",
        "sign_out": "signOut",
    },
)
class RedirectPaths:
    def __init__(self, *, auth_refresh: str, sign_in: str, sign_out: str) -> None:
        """
        :param auth_refresh: -
        :param sign_in: -
        :param sign_out: -
        """
        self._values = {
            "auth_refresh": auth_refresh,
            "sign_in": sign_in,
            "sign_out": sign_out,
        }

    @builtins.property
    def auth_refresh(self) -> str:
        return self._values.get("auth_refresh")

    @builtins.property
    def sign_in(self) -> str:
        return self._values.get("sign_in")

    @builtins.property
    def sign_out(self) -> str:
        return self._values.get("sign_out")

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RedirectPaths(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RetrieveUserPoolClientSecret(
    aws_cdk.core.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cloudcomponents/cdk-cloudfront-authorization.RetrieveUserPoolClientSecret",
):
    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: str,
        *,
        user_pool: aws_cdk.aws_cognito.IUserPool,
        user_pool_client: aws_cdk.aws_cognito.IUserPoolClient,
    ) -> None:
        """
        :param scope: -
        :param id: -
        :param user_pool: -
        :param user_pool_client: -
        """
        props = RetrieveUserPoolClientSecretProps(
            user_pool=user_pool, user_pool_client=user_pool_client
        )

        jsii.create(RetrieveUserPoolClientSecret, self, [scope, id, props])

    @builtins.property
    @jsii.member(jsii_name="clientSecret")
    def client_secret(self) -> str:
        return jsii.get(self, "clientSecret")

    @client_secret.setter
    def client_secret(self, value: str) -> None:
        jsii.set(self, "clientSecret", value)


@jsii.data_type(
    jsii_type="@cloudcomponents/cdk-cloudfront-authorization.RetrieveUserPoolClientSecretProps",
    jsii_struct_bases=[],
    name_mapping={"user_pool": "userPool", "user_pool_client": "userPoolClient"},
)
class RetrieveUserPoolClientSecretProps:
    def __init__(
        self,
        *,
        user_pool: aws_cdk.aws_cognito.IUserPool,
        user_pool_client: aws_cdk.aws_cognito.IUserPoolClient,
    ) -> None:
        """
        :param user_pool: -
        :param user_pool_client: -
        """
        self._values = {
            "user_pool": user_pool,
            "user_pool_client": user_pool_client,
        }

    @builtins.property
    def user_pool(self) -> aws_cdk.aws_cognito.IUserPool:
        return self._values.get("user_pool")

    @builtins.property
    def user_pool_client(self) -> aws_cdk.aws_cognito.IUserPoolClient:
        return self._values.get("user_pool_client")

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RetrieveUserPoolClientSecretProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SecretGenerator(
    aws_cdk.core.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cloudcomponents/cdk-cloudfront-authorization.SecretGenerator",
):
    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: str,
        *,
        allowed_characters: typing.Optional[str] = None,
        length: typing.Optional[jsii.Number] = None,
    ) -> None:
        """
        :param scope: -
        :param id: -
        :param allowed_characters: -
        :param length: -
        """
        props = SecretGeneratorProps(
            allowed_characters=allowed_characters, length=length
        )

        jsii.create(SecretGenerator, self, [scope, id, props])

    @builtins.property
    @jsii.member(jsii_name="secret")
    def secret(self) -> str:
        return jsii.get(self, "secret")


@jsii.data_type(
    jsii_type="@cloudcomponents/cdk-cloudfront-authorization.SecretGeneratorProps",
    jsii_struct_bases=[],
    name_mapping={"allowed_characters": "allowedCharacters", "length": "length"},
)
class SecretGeneratorProps:
    def __init__(
        self,
        *,
        allowed_characters: typing.Optional[str] = None,
        length: typing.Optional[jsii.Number] = None,
    ) -> None:
        """
        :param allowed_characters: -
        :param length: -
        """
        self._values = {}
        if allowed_characters is not None:
            self._values["allowed_characters"] = allowed_characters
        if length is not None:
            self._values["length"] = length

    @builtins.property
    def allowed_characters(self) -> typing.Optional[str]:
        return self._values.get("allowed_characters")

    @builtins.property
    def length(self) -> typing.Optional[jsii.Number]:
        return self._values.get("length")

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SecretGeneratorProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(ISpaAuthorization)
class SpaAuthorization(
    Authorization,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cloudcomponents/cdk-cloudfront-authorization.SpaAuthorization",
):
    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: str,
        *,
        user_pool: aws_cdk.aws_cognito.IUserPool,
        cookie_settings: typing.Optional[typing.Mapping[str, str]] = None,
        http_headers: typing.Optional[typing.Mapping[str, str]] = None,
        log_level: typing.Optional[
            cloudcomponents.cdk_lambda_at_edge_pattern.LogLevel
        ] = None,
        oauth_scopes: typing.Optional[
            typing.List[aws_cdk.aws_cognito.OAuthScope]
        ] = None,
        redirect_paths: typing.Optional["RedirectPaths"] = None,
        sign_out_url: typing.Optional[str] = None,
    ) -> None:
        """
        :param scope: -
        :param id: -
        :param user_pool: -
        :param cookie_settings: -
        :param http_headers: -
        :param log_level: -
        :param oauth_scopes: -
        :param redirect_paths: -
        :param sign_out_url: -
        """
        props = AuthorizationProps(
            user_pool=user_pool,
            cookie_settings=cookie_settings,
            http_headers=http_headers,
            log_level=log_level,
            oauth_scopes=oauth_scopes,
            redirect_paths=redirect_paths,
            sign_out_url=sign_out_url,
        )

        jsii.create(SpaAuthorization, self, [scope, id, props])

    @jsii.member(jsii_name="createAuthFlow")
    def _create_auth_flow(
        self, log_level: cloudcomponents.cdk_lambda_at_edge_pattern.LogLevel
    ) -> "AuthFlow":
        """
        :param log_level: -
        """
        return jsii.invoke(self, "createAuthFlow", [log_level])

    @jsii.member(jsii_name="createUserPoolClient")
    def _create_user_pool_client(self) -> aws_cdk.aws_cognito.IUserPoolClient:
        return jsii.invoke(self, "createUserPoolClient", [])

    @builtins.property
    @jsii.member(jsii_name="mode")
    def mode(self) -> "Mode":
        return jsii.get(self, "mode")


class SpaDistribution(
    BaseDistribution,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cloudcomponents/cdk-cloudfront-authorization.SpaDistribution",
):
    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: str,
        *,
        authorization: "ISpaAuthorization",
        ttl: typing.Optional[aws_cdk.core.Duration] = None,
        certificate: typing.Optional[
            aws_cdk.aws_certificatemanager.ICertificate
        ] = None,
        origin: typing.Optional[aws_cdk.aws_cloudfront.IOrigin] = None,
        price_class: typing.Optional[aws_cdk.aws_cloudfront.PriceClass] = None,
        removal_policy: typing.Optional[aws_cdk.core.RemovalPolicy] = None,
    ) -> None:
        """
        :param scope: -
        :param id: -
        :param authorization: -
        :param ttl: The minimum amount of time, in seconds, that you want CloudFront to cache the HTTP status code specified in ErrorCode. Default: 300 seconds
        :param certificate: -
        :param origin: -
        :param price_class: -
        :param removal_policy: -
        """
        props = SpaDistributionProps(
            authorization=authorization,
            ttl=ttl,
            certificate=certificate,
            origin=origin,
            price_class=price_class,
            removal_policy=removal_policy,
        )

        jsii.create(SpaDistribution, self, [scope, id, props])


@jsii.data_type(
    jsii_type="@cloudcomponents/cdk-cloudfront-authorization.SpaDistributionProps",
    jsii_struct_bases=[CommonDistributionProps],
    name_mapping={
        "certificate": "certificate",
        "origin": "origin",
        "price_class": "priceClass",
        "removal_policy": "removalPolicy",
        "authorization": "authorization",
        "ttl": "ttl",
    },
)
class SpaDistributionProps(CommonDistributionProps):
    def __init__(
        self,
        *,
        certificate: typing.Optional[
            aws_cdk.aws_certificatemanager.ICertificate
        ] = None,
        origin: typing.Optional[aws_cdk.aws_cloudfront.IOrigin] = None,
        price_class: typing.Optional[aws_cdk.aws_cloudfront.PriceClass] = None,
        removal_policy: typing.Optional[aws_cdk.core.RemovalPolicy] = None,
        authorization: "ISpaAuthorization",
        ttl: typing.Optional[aws_cdk.core.Duration] = None,
    ) -> None:
        """
        :param certificate: -
        :param origin: -
        :param price_class: -
        :param removal_policy: -
        :param authorization: -
        :param ttl: The minimum amount of time, in seconds, that you want CloudFront to cache the HTTP status code specified in ErrorCode. Default: 300 seconds
        """
        self._values = {
            "authorization": authorization,
        }
        if certificate is not None:
            self._values["certificate"] = certificate
        if origin is not None:
            self._values["origin"] = origin
        if price_class is not None:
            self._values["price_class"] = price_class
        if removal_policy is not None:
            self._values["removal_policy"] = removal_policy
        if ttl is not None:
            self._values["ttl"] = ttl

    @builtins.property
    def certificate(
        self,
    ) -> typing.Optional[aws_cdk.aws_certificatemanager.ICertificate]:
        return self._values.get("certificate")

    @builtins.property
    def origin(self) -> typing.Optional[aws_cdk.aws_cloudfront.IOrigin]:
        return self._values.get("origin")

    @builtins.property
    def price_class(self) -> typing.Optional[aws_cdk.aws_cloudfront.PriceClass]:
        return self._values.get("price_class")

    @builtins.property
    def removal_policy(self) -> typing.Optional[aws_cdk.core.RemovalPolicy]:
        return self._values.get("removal_policy")

    @builtins.property
    def authorization(self) -> "ISpaAuthorization":
        return self._values.get("authorization")

    @builtins.property
    def ttl(self) -> typing.Optional[aws_cdk.core.Duration]:
        """The minimum amount of time, in seconds, that you want CloudFront to cache the HTTP status code specified in ErrorCode.

        default
        :default: 300 seconds
        """
        return self._values.get("ttl")

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SpaDistributionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IStaticSiteAuthorization)
class StaticSiteAuthorization(
    Authorization,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cloudcomponents/cdk-cloudfront-authorization.StaticSiteAuthorization",
):
    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: str,
        *,
        user_pool: aws_cdk.aws_cognito.IUserPool,
        cookie_settings: typing.Optional[typing.Mapping[str, str]] = None,
        http_headers: typing.Optional[typing.Mapping[str, str]] = None,
        log_level: typing.Optional[
            cloudcomponents.cdk_lambda_at_edge_pattern.LogLevel
        ] = None,
        oauth_scopes: typing.Optional[
            typing.List[aws_cdk.aws_cognito.OAuthScope]
        ] = None,
        redirect_paths: typing.Optional["RedirectPaths"] = None,
        sign_out_url: typing.Optional[str] = None,
    ) -> None:
        """
        :param scope: -
        :param id: -
        :param user_pool: -
        :param cookie_settings: -
        :param http_headers: -
        :param log_level: -
        :param oauth_scopes: -
        :param redirect_paths: -
        :param sign_out_url: -
        """
        props = AuthorizationProps(
            user_pool=user_pool,
            cookie_settings=cookie_settings,
            http_headers=http_headers,
            log_level=log_level,
            oauth_scopes=oauth_scopes,
            redirect_paths=redirect_paths,
            sign_out_url=sign_out_url,
        )

        jsii.create(StaticSiteAuthorization, self, [scope, id, props])

    @jsii.member(jsii_name="createAuthFlow")
    def _create_auth_flow(
        self, log_level: cloudcomponents.cdk_lambda_at_edge_pattern.LogLevel
    ) -> "AuthFlow":
        """
        :param log_level: -
        """
        return jsii.invoke(self, "createAuthFlow", [log_level])

    @jsii.member(jsii_name="createUserPoolClient")
    def _create_user_pool_client(self) -> aws_cdk.aws_cognito.IUserPoolClient:
        return jsii.invoke(self, "createUserPoolClient", [])

    @builtins.property
    @jsii.member(jsii_name="mode")
    def mode(self) -> "Mode":
        return jsii.get(self, "mode")


class StaticSiteDistribution(
    BaseDistribution,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cloudcomponents/cdk-cloudfront-authorization.StaticSiteDistribution",
):
    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: str,
        *,
        authorization: "IStaticSiteAuthorization",
        error_responses: typing.Optional[
            typing.List[aws_cdk.aws_cloudfront.ErrorResponse]
        ] = None,
        certificate: typing.Optional[
            aws_cdk.aws_certificatemanager.ICertificate
        ] = None,
        origin: typing.Optional[aws_cdk.aws_cloudfront.IOrigin] = None,
        price_class: typing.Optional[aws_cdk.aws_cloudfront.PriceClass] = None,
        removal_policy: typing.Optional[aws_cdk.core.RemovalPolicy] = None,
    ) -> None:
        """
        :param scope: -
        :param id: -
        :param authorization: -
        :param error_responses: -
        :param certificate: -
        :param origin: -
        :param price_class: -
        :param removal_policy: -
        """
        props = StaticSiteDistributionProps(
            authorization=authorization,
            error_responses=error_responses,
            certificate=certificate,
            origin=origin,
            price_class=price_class,
            removal_policy=removal_policy,
        )

        jsii.create(StaticSiteDistribution, self, [scope, id, props])


@jsii.data_type(
    jsii_type="@cloudcomponents/cdk-cloudfront-authorization.StaticSiteDistributionProps",
    jsii_struct_bases=[CommonDistributionProps],
    name_mapping={
        "certificate": "certificate",
        "origin": "origin",
        "price_class": "priceClass",
        "removal_policy": "removalPolicy",
        "authorization": "authorization",
        "error_responses": "errorResponses",
    },
)
class StaticSiteDistributionProps(CommonDistributionProps):
    def __init__(
        self,
        *,
        certificate: typing.Optional[
            aws_cdk.aws_certificatemanager.ICertificate
        ] = None,
        origin: typing.Optional[aws_cdk.aws_cloudfront.IOrigin] = None,
        price_class: typing.Optional[aws_cdk.aws_cloudfront.PriceClass] = None,
        removal_policy: typing.Optional[aws_cdk.core.RemovalPolicy] = None,
        authorization: "IStaticSiteAuthorization",
        error_responses: typing.Optional[
            typing.List[aws_cdk.aws_cloudfront.ErrorResponse]
        ] = None,
    ) -> None:
        """
        :param certificate: -
        :param origin: -
        :param price_class: -
        :param removal_policy: -
        :param authorization: -
        :param error_responses: -
        """
        self._values = {
            "authorization": authorization,
        }
        if certificate is not None:
            self._values["certificate"] = certificate
        if origin is not None:
            self._values["origin"] = origin
        if price_class is not None:
            self._values["price_class"] = price_class
        if removal_policy is not None:
            self._values["removal_policy"] = removal_policy
        if error_responses is not None:
            self._values["error_responses"] = error_responses

    @builtins.property
    def certificate(
        self,
    ) -> typing.Optional[aws_cdk.aws_certificatemanager.ICertificate]:
        return self._values.get("certificate")

    @builtins.property
    def origin(self) -> typing.Optional[aws_cdk.aws_cloudfront.IOrigin]:
        return self._values.get("origin")

    @builtins.property
    def price_class(self) -> typing.Optional[aws_cdk.aws_cloudfront.PriceClass]:
        return self._values.get("price_class")

    @builtins.property
    def removal_policy(self) -> typing.Optional[aws_cdk.core.RemovalPolicy]:
        return self._values.get("removal_policy")

    @builtins.property
    def authorization(self) -> "IStaticSiteAuthorization":
        return self._values.get("authorization")

    @builtins.property
    def error_responses(
        self,
    ) -> typing.Optional[typing.List[aws_cdk.aws_cloudfront.ErrorResponse]]:
        return self._values.get("error_responses")

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StaticSiteDistributionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cloudcomponents/cdk-cloudfront-authorization.UserPoolClientCallbackUrls",
    jsii_struct_bases=[],
    name_mapping={"callback_urls": "callbackUrls", "logout_urls": "logoutUrls"},
)
class UserPoolClientCallbackUrls:
    def __init__(
        self, *, callback_urls: typing.List[str], logout_urls: typing.List[str]
    ) -> None:
        """
        :param callback_urls: A list of allowed redirect (callback) URLs for the identity providers.
        :param logout_urls: A list of allowed logout URLs for the identity providers.
        """
        self._values = {
            "callback_urls": callback_urls,
            "logout_urls": logout_urls,
        }

    @builtins.property
    def callback_urls(self) -> typing.List[str]:
        """A list of allowed redirect (callback) URLs for the identity providers."""
        return self._values.get("callback_urls")

    @builtins.property
    def logout_urls(self) -> typing.List[str]:
        """A list of allowed logout URLs for the identity providers."""
        return self._values.get("logout_urls")

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UserPoolClientCallbackUrls(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class UserPoolClientRedirects(
    aws_cdk.core.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cloudcomponents/cdk-cloudfront-authorization.UserPoolClientRedirects",
):
    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: str,
        *,
        callback_urls: typing.List[str],
        logout_urls: typing.List[str],
        oauth_scopes: typing.List[aws_cdk.aws_cognito.OAuthScope],
        user_pool: aws_cdk.aws_cognito.IUserPool,
        user_pool_client: aws_cdk.aws_cognito.IUserPoolClient,
    ) -> None:
        """
        :param scope: -
        :param id: -
        :param callback_urls: -
        :param logout_urls: -
        :param oauth_scopes: -
        :param user_pool: -
        :param user_pool_client: -
        """
        props = UserPoolClientRedirectsProps(
            callback_urls=callback_urls,
            logout_urls=logout_urls,
            oauth_scopes=oauth_scopes,
            user_pool=user_pool,
            user_pool_client=user_pool_client,
        )

        jsii.create(UserPoolClientRedirects, self, [scope, id, props])


@jsii.data_type(
    jsii_type="@cloudcomponents/cdk-cloudfront-authorization.UserPoolClientRedirectsProps",
    jsii_struct_bases=[],
    name_mapping={
        "callback_urls": "callbackUrls",
        "logout_urls": "logoutUrls",
        "oauth_scopes": "oauthScopes",
        "user_pool": "userPool",
        "user_pool_client": "userPoolClient",
    },
)
class UserPoolClientRedirectsProps:
    def __init__(
        self,
        *,
        callback_urls: typing.List[str],
        logout_urls: typing.List[str],
        oauth_scopes: typing.List[aws_cdk.aws_cognito.OAuthScope],
        user_pool: aws_cdk.aws_cognito.IUserPool,
        user_pool_client: aws_cdk.aws_cognito.IUserPoolClient,
    ) -> None:
        """
        :param callback_urls: -
        :param logout_urls: -
        :param oauth_scopes: -
        :param user_pool: -
        :param user_pool_client: -
        """
        self._values = {
            "callback_urls": callback_urls,
            "logout_urls": logout_urls,
            "oauth_scopes": oauth_scopes,
            "user_pool": user_pool,
            "user_pool_client": user_pool_client,
        }

    @builtins.property
    def callback_urls(self) -> typing.List[str]:
        return self._values.get("callback_urls")

    @builtins.property
    def logout_urls(self) -> typing.List[str]:
        return self._values.get("logout_urls")

    @builtins.property
    def oauth_scopes(self) -> typing.List[aws_cdk.aws_cognito.OAuthScope]:
        return self._values.get("oauth_scopes")

    @builtins.property
    def user_pool(self) -> aws_cdk.aws_cognito.IUserPool:
        return self._values.get("user_pool")

    @builtins.property
    def user_pool_client(self) -> aws_cdk.aws_cognito.IUserPoolClient:
        return self._values.get("user_pool_client")

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UserPoolClientRedirectsProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cloudcomponents/cdk-cloudfront-authorization.BaseDistributionProps",
    jsii_struct_bases=[CommonDistributionProps],
    name_mapping={
        "certificate": "certificate",
        "origin": "origin",
        "price_class": "priceClass",
        "removal_policy": "removalPolicy",
        "authorization": "authorization",
        "error_responses": "errorResponses",
    },
)
class BaseDistributionProps(CommonDistributionProps):
    def __init__(
        self,
        *,
        certificate: typing.Optional[
            aws_cdk.aws_certificatemanager.ICertificate
        ] = None,
        origin: typing.Optional[aws_cdk.aws_cloudfront.IOrigin] = None,
        price_class: typing.Optional[aws_cdk.aws_cloudfront.PriceClass] = None,
        removal_policy: typing.Optional[aws_cdk.core.RemovalPolicy] = None,
        authorization: "IAuthorization",
        error_responses: typing.Optional[
            typing.List[aws_cdk.aws_cloudfront.ErrorResponse]
        ] = None,
    ) -> None:
        """
        :param certificate: -
        :param origin: -
        :param price_class: -
        :param removal_policy: -
        :param authorization: -
        :param error_responses: -
        """
        self._values = {
            "authorization": authorization,
        }
        if certificate is not None:
            self._values["certificate"] = certificate
        if origin is not None:
            self._values["origin"] = origin
        if price_class is not None:
            self._values["price_class"] = price_class
        if removal_policy is not None:
            self._values["removal_policy"] = removal_policy
        if error_responses is not None:
            self._values["error_responses"] = error_responses

    @builtins.property
    def certificate(
        self,
    ) -> typing.Optional[aws_cdk.aws_certificatemanager.ICertificate]:
        return self._values.get("certificate")

    @builtins.property
    def origin(self) -> typing.Optional[aws_cdk.aws_cloudfront.IOrigin]:
        return self._values.get("origin")

    @builtins.property
    def price_class(self) -> typing.Optional[aws_cdk.aws_cloudfront.PriceClass]:
        return self._values.get("price_class")

    @builtins.property
    def removal_policy(self) -> typing.Optional[aws_cdk.core.RemovalPolicy]:
        return self._values.get("removal_policy")

    @builtins.property
    def authorization(self) -> "IAuthorization":
        return self._values.get("authorization")

    @builtins.property
    def error_responses(
        self,
    ) -> typing.Optional[typing.List[aws_cdk.aws_cloudfront.ErrorResponse]]:
        return self._values.get("error_responses")

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BaseDistributionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AuthFlow",
    "AuthFlowProps",
    "Authorization",
    "AuthorizationProps",
    "BaseDistribution",
    "BaseDistributionProps",
    "CommonDistributionProps",
    "IAuthorization",
    "ISpaAuthorization",
    "IStaticSiteAuthorization",
    "Mode",
    "RedirectPaths",
    "RetrieveUserPoolClientSecret",
    "RetrieveUserPoolClientSecretProps",
    "SecretGenerator",
    "SecretGeneratorProps",
    "SpaAuthorization",
    "SpaDistribution",
    "SpaDistributionProps",
    "StaticSiteAuthorization",
    "StaticSiteDistribution",
    "StaticSiteDistributionProps",
    "UserPoolClientCallbackUrls",
    "UserPoolClientRedirects",
    "UserPoolClientRedirectsProps",
]

publication.publish()
