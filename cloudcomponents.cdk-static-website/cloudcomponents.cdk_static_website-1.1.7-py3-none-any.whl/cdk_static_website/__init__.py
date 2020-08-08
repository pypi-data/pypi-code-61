"""
[![cloudcomponents Logo](https://raw.githubusercontent.com/cloudcomponents/cdk-constructs/master/logo.png)](https://github.com/cloudcomponents/cdk-constructs)

# @cloudcomponents/cdk-static-website

[![Build Status](https://travis-ci.org/cloudcomponents/cdk-constructs.svg?branch=master)](https://travis-ci.org/cloudcomponents/cdk-constructs)
[![cdkdx](https://img.shields.io/badge/buildtool-cdkdx-blue.svg)](https://github.com/hupe1980/cdkdx)
[![typescript](https://img.shields.io/badge/jsii-typescript-blueviolet.svg)](https://www.npmjs.com/package/@cloudcomponents/cdk-static-website)
[![python](https://img.shields.io/badge/jsii-python-blueviolet.svg)](https://pypi.org/project/cloudcomponents.cdk-static-website/)

> Cdk component that creates a static website using S3, configures CloudFront (CDN) and maps a custom domain via Route53 (DNS)

## Install

TypeScript/JavaScript:

```bash
npm i @cloudcomponents/cdk-static-website
```

Python:

```bash
pip install cloudcomponents.cdk-static-website
```

## How to use

### Example 1: With an existing certificate

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

### Example 2: Cloudfront URL with existing sources and up to date Securitypolicy

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
from aws_cdk.core import Construct, RemovalPolicy, Stack, StackProps
from aws_cdk.aws_ssm import StringParameter
from cloudcomponents.cdk_static_website import StaticWebsite
from aws_cdk.aws_cloudfront import SecurityPolicyProtocol

class StaticWebsiteWithExistingSourcesAndSecurityPolicyStack(Stack):
    def __init__(self, scope, id, *, description=None, env=None, stackName=None, tags=None, synthesizer=None, terminationProtection=None):
        super().__init__(scope, id, description=description, env=env, stackName=stackName, tags=tags, synthesizer=synthesizer, terminationProtection=terminationProtection)

        certificate_arn = StringParameter.value_from_lookup(self, "/certificate/cloudcomponents.org")

        StaticWebsite(self, "StaticWebsite",
            bucket_configuration=WebsiteBucketProps(
                source="../path/to/your/static/webpage",
                removal_policy=RemovalPolicy.DESTROY
            ),
            alias_configuration=AliasProps(
                domain_name="cloudcomponents.org",
                names=["www.cloudcomponents.org", "cloudcomponents.org"],
                acm_cert_ref=certificate_arn,
                security_policy=SecurityPolicyProtocol.TLS_V1_2_2018
            )
        )
```

### Lambda@Edge function

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
website.add_lambda_function_association(
    event_type=LambdaEdgeEventType.ORIGIN_REQUEST,
    lambda_function=Version.from_version_arn(stack, "LambdaEdge", "arn:aws:lambda:us-east-1:123456789012:function:my-function:1")
)
```

## API Reference

See [API.md](https://github.com/cloudcomponents/cdk-constructs/tree/master/packages/cdk-static-website/API.md).

## Example

See more complete [examples](https://github.com/cloudcomponents/cdk-constructs/tree/master/examples).

## License

[MIT](https://github.com/cloudcomponents/cdk-constructs/tree/master/packages/cdk-static-website/LICENSE)
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
import aws_cdk.aws_lambda
import aws_cdk.aws_route53
import aws_cdk.core


@jsii.data_type(
    jsii_type="@cloudcomponents/cdk-static-website.AliasProps",
    jsii_struct_bases=[aws_cdk.aws_cloudfront.AliasConfiguration],
    name_mapping={
        "acm_cert_ref": "acmCertRef",
        "names": "names",
        "security_policy": "securityPolicy",
        "ssl_method": "sslMethod",
        "domain_name": "domainName",
    },
)
class AliasProps(aws_cdk.aws_cloudfront.AliasConfiguration):
    def __init__(
        self,
        *,
        acm_cert_ref: str,
        names: typing.List[str],
        security_policy: typing.Optional[
            aws_cdk.aws_cloudfront.SecurityPolicyProtocol
        ] = None,
        ssl_method: typing.Optional[aws_cdk.aws_cloudfront.SSLMethod] = None,
        domain_name: str,
    ) -> None:
        """
        :param acm_cert_ref: ARN of an AWS Certificate Manager (ACM) certificate.
        :param names: Domain names on the certificate. Both main domain name and Subject Alternative Names.
        :param security_policy: The minimum version of the SSL protocol that you want CloudFront to use for HTTPS connections. CloudFront serves your objects only to browsers or devices that support at least the SSL version that you specify. Default: - SSLv3 if sslMethod VIP, TLSv1 if sslMethod SNI
        :param ssl_method: How CloudFront should serve HTTPS requests. See the notes on SSLMethod if you wish to use other SSL termination types. Default: SSLMethod.SNI
        :param domain_name: The domain name for the site like 'example.com'.
        """
        self._values = {
            "acm_cert_ref": acm_cert_ref,
            "names": names,
            "domain_name": domain_name,
        }
        if security_policy is not None:
            self._values["security_policy"] = security_policy
        if ssl_method is not None:
            self._values["ssl_method"] = ssl_method

    @builtins.property
    def acm_cert_ref(self) -> str:
        """ARN of an AWS Certificate Manager (ACM) certificate.

        stability
        :stability: experimental
        """
        return self._values.get("acm_cert_ref")

    @builtins.property
    def names(self) -> typing.List[str]:
        """Domain names on the certificate.

        Both main domain name and Subject Alternative Names.

        stability
        :stability: experimental
        """
        return self._values.get("names")

    @builtins.property
    def security_policy(
        self,
    ) -> typing.Optional[aws_cdk.aws_cloudfront.SecurityPolicyProtocol]:
        """The minimum version of the SSL protocol that you want CloudFront to use for HTTPS connections.

        CloudFront serves your objects only to browsers or devices that support at
        least the SSL version that you specify.

        default
        :default: - SSLv3 if sslMethod VIP, TLSv1 if sslMethod SNI

        stability
        :stability: experimental
        """
        return self._values.get("security_policy")

    @builtins.property
    def ssl_method(self) -> typing.Optional[aws_cdk.aws_cloudfront.SSLMethod]:
        """How CloudFront should serve HTTPS requests.

        See the notes on SSLMethod if you wish to use other SSL termination types.

        default
        :default: SSLMethod.SNI

        see
        :see: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ViewerCertificate.html
        stability
        :stability: experimental
        """
        return self._values.get("ssl_method")

    @builtins.property
    def domain_name(self) -> str:
        """The domain name for the site like 'example.com'."""
        return self._values.get("domain_name")

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AliasProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class StaticWebsite(
    aws_cdk.core.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cloudcomponents/cdk-static-website.StaticWebsite",
):
    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: str,
        *,
        alias_configuration: typing.Optional["AliasProps"] = None,
        bucket_configuration: typing.Optional["WebsiteBucketProps"] = None,
        disable_i_pv6: typing.Optional[bool] = None,
        web_acl_id: typing.Optional[str] = None,
        bucket_name: typing.Optional[str] = None,
        disable_upload: typing.Optional[bool] = None,
        removal_policy: typing.Optional[aws_cdk.core.RemovalPolicy] = None,
        source: typing.Optional[str] = None,
        website_error_document: typing.Optional[str] = None,
        website_index_document: typing.Optional[str] = None,
    ) -> None:
        """
        :param scope: -
        :param id: -
        :param alias_configuration: AliasConfiguration is used to configured CloudFront to respond to requests on custom domain names. Default: - No custom domain names are set up
        :param bucket_configuration: BucketConfiguration is used to configured the S3 website bucket. Default: - The website bucket is provided with default values
        :param disable_i_pv6: An override flag that allows you to turn off support for IPv6 if required. Default: - Cloudfront IPv6 support is enabled and if you've supplied an aliasConfiguration, an AAAA record will be created for your service, set this to true to switch this off.
        :param web_acl_id: AWS WAF WebACL to associate with this CloudFront distribution. Default: - No AWS Web Application Firewall web access control list (web ACL)
        :param bucket_name: Name of the bucket. Default: - Assigned by CloudFormation (recommended).
        :param disable_upload: Disable website deployment. Default: - false
        :param removal_policy: Policy to apply when the bucket is removed from this stack. Default: - The bucket will be orphaned.
        :param source: The source from which to deploy the website. Default: - Dummy placeholder
        :param website_error_document: The error page for the site like 'error.html'. Default: - error.html
        :param website_index_document: The index page for the site like 'index.html'. Default: - index.html
        """
        props = StaticWebsiteProps(
            alias_configuration=alias_configuration,
            bucket_configuration=bucket_configuration,
            disable_i_pv6=disable_i_pv6,
            web_acl_id=web_acl_id,
            bucket_name=bucket_name,
            disable_upload=disable_upload,
            removal_policy=removal_policy,
            source=source,
            website_error_document=website_error_document,
            website_index_document=website_index_document,
        )

        jsii.create(StaticWebsite, self, [scope, id, props])

    @jsii.member(jsii_name="addLambdaFunctionAssociation")
    def add_lambda_function_association(
        self,
        *,
        event_type: aws_cdk.aws_cloudfront.LambdaEdgeEventType,
        lambda_function: aws_cdk.aws_lambda.IVersion,
    ) -> None:
        """
        :param event_type: The lambda event type defines at which event the lambda is called during the request lifecycle.
        :param lambda_function: A version of the lambda to associate.
        """
        assosiation = aws_cdk.aws_cloudfront.LambdaFunctionAssociation(
            event_type=event_type, lambda_function=lambda_function
        )

        return jsii.invoke(self, "addLambdaFunctionAssociation", [assosiation])

    @jsii.member(jsii_name="addLambdaFunctionAssociations")
    def add_lambda_function_associations(
        self,
        assosiations: typing.List[aws_cdk.aws_cloudfront.LambdaFunctionAssociation],
    ) -> None:
        """
        :param assosiations: -
        """
        return jsii.invoke(self, "addLambdaFunctionAssociations", [assosiations])


class WebsiteAliasRecord(
    aws_cdk.core.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cloudcomponents/cdk-static-website.WebsiteAliasRecord",
):
    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: str,
        *,
        domain_name: str,
        record_names: typing.List[str],
        target: aws_cdk.aws_route53.IAliasRecordTarget,
        disable_i_pv6: typing.Optional[bool] = None,
    ) -> None:
        """
        :param scope: -
        :param id: -
        :param domain_name: The domain name for the site like 'example.com'.
        :param record_names: Names for the records.
        :param target: Target for the alias record.
        :param disable_i_pv6: We support IPv6 and add an AAAA record by default, but you can turn it off.
        """
        props = WebsiteAliasRecordProps(
            domain_name=domain_name,
            record_names=record_names,
            target=target,
            disable_i_pv6=disable_i_pv6,
        )

        jsii.create(WebsiteAliasRecord, self, [scope, id, props])


@jsii.data_type(
    jsii_type="@cloudcomponents/cdk-static-website.WebsiteAliasRecordProps",
    jsii_struct_bases=[],
    name_mapping={
        "domain_name": "domainName",
        "record_names": "recordNames",
        "target": "target",
        "disable_i_pv6": "disableIPv6",
    },
)
class WebsiteAliasRecordProps:
    def __init__(
        self,
        *,
        domain_name: str,
        record_names: typing.List[str],
        target: aws_cdk.aws_route53.IAliasRecordTarget,
        disable_i_pv6: typing.Optional[bool] = None,
    ) -> None:
        """
        :param domain_name: The domain name for the site like 'example.com'.
        :param record_names: Names for the records.
        :param target: Target for the alias record.
        :param disable_i_pv6: We support IPv6 and add an AAAA record by default, but you can turn it off.
        """
        self._values = {
            "domain_name": domain_name,
            "record_names": record_names,
            "target": target,
        }
        if disable_i_pv6 is not None:
            self._values["disable_i_pv6"] = disable_i_pv6

    @builtins.property
    def domain_name(self) -> str:
        """The domain name for the site like 'example.com'."""
        return self._values.get("domain_name")

    @builtins.property
    def record_names(self) -> typing.List[str]:
        """Names for the records."""
        return self._values.get("record_names")

    @builtins.property
    def target(self) -> aws_cdk.aws_route53.IAliasRecordTarget:
        """Target for the alias record."""
        return self._values.get("target")

    @builtins.property
    def disable_i_pv6(self) -> typing.Optional[bool]:
        """We support IPv6 and add an AAAA record by default, but you can turn it off."""
        return self._values.get("disable_i_pv6")

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WebsiteAliasRecordProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WebsiteBucket(
    aws_cdk.core.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cloudcomponents/cdk-static-website.WebsiteBucket",
):
    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: str,
        *,
        bucket_name: typing.Optional[str] = None,
        disable_upload: typing.Optional[bool] = None,
        removal_policy: typing.Optional[aws_cdk.core.RemovalPolicy] = None,
        source: typing.Optional[str] = None,
        website_error_document: typing.Optional[str] = None,
        website_index_document: typing.Optional[str] = None,
    ) -> None:
        """
        :param scope: -
        :param id: -
        :param bucket_name: Name of the bucket. Default: - Assigned by CloudFormation (recommended).
        :param disable_upload: Disable website deployment. Default: - false
        :param removal_policy: Policy to apply when the bucket is removed from this stack. Default: - The bucket will be orphaned.
        :param source: The source from which to deploy the website. Default: - Dummy placeholder
        :param website_error_document: The error page for the site like 'error.html'. Default: - error.html
        :param website_index_document: The index page for the site like 'index.html'. Default: - index.html
        """
        props = WebsiteBucketProps(
            bucket_name=bucket_name,
            disable_upload=disable_upload,
            removal_policy=removal_policy,
            source=source,
            website_error_document=website_error_document,
            website_index_document=website_index_document,
        )

        jsii.create(WebsiteBucket, self, [scope, id, props])

    @builtins.property
    @jsii.member(jsii_name="s3OriginConfig")
    def s3_origin_config(self) -> aws_cdk.aws_cloudfront.S3OriginConfig:
        return jsii.get(self, "s3OriginConfig")


@jsii.data_type(
    jsii_type="@cloudcomponents/cdk-static-website.WebsiteBucketProps",
    jsii_struct_bases=[],
    name_mapping={
        "bucket_name": "bucketName",
        "disable_upload": "disableUpload",
        "removal_policy": "removalPolicy",
        "source": "source",
        "website_error_document": "websiteErrorDocument",
        "website_index_document": "websiteIndexDocument",
    },
)
class WebsiteBucketProps:
    def __init__(
        self,
        *,
        bucket_name: typing.Optional[str] = None,
        disable_upload: typing.Optional[bool] = None,
        removal_policy: typing.Optional[aws_cdk.core.RemovalPolicy] = None,
        source: typing.Optional[str] = None,
        website_error_document: typing.Optional[str] = None,
        website_index_document: typing.Optional[str] = None,
    ) -> None:
        """
        :param bucket_name: Name of the bucket. Default: - Assigned by CloudFormation (recommended).
        :param disable_upload: Disable website deployment. Default: - false
        :param removal_policy: Policy to apply when the bucket is removed from this stack. Default: - The bucket will be orphaned.
        :param source: The source from which to deploy the website. Default: - Dummy placeholder
        :param website_error_document: The error page for the site like 'error.html'. Default: - error.html
        :param website_index_document: The index page for the site like 'index.html'. Default: - index.html
        """
        self._values = {}
        if bucket_name is not None:
            self._values["bucket_name"] = bucket_name
        if disable_upload is not None:
            self._values["disable_upload"] = disable_upload
        if removal_policy is not None:
            self._values["removal_policy"] = removal_policy
        if source is not None:
            self._values["source"] = source
        if website_error_document is not None:
            self._values["website_error_document"] = website_error_document
        if website_index_document is not None:
            self._values["website_index_document"] = website_index_document

    @builtins.property
    def bucket_name(self) -> typing.Optional[str]:
        """Name of the bucket.

        default
        :default: - Assigned by CloudFormation (recommended).
        """
        return self._values.get("bucket_name")

    @builtins.property
    def disable_upload(self) -> typing.Optional[bool]:
        """Disable website deployment.

        default
        :default: - false
        """
        return self._values.get("disable_upload")

    @builtins.property
    def removal_policy(self) -> typing.Optional[aws_cdk.core.RemovalPolicy]:
        """Policy to apply when the bucket is removed from this stack.

        default
        :default: - The bucket will be orphaned.
        """
        return self._values.get("removal_policy")

    @builtins.property
    def source(self) -> typing.Optional[str]:
        """The source from which to deploy the website.

        default
        :default: - Dummy placeholder
        """
        return self._values.get("source")

    @builtins.property
    def website_error_document(self) -> typing.Optional[str]:
        """The error page for the site like 'error.html'.

        default
        :default: - error.html
        """
        return self._values.get("website_error_document")

    @builtins.property
    def website_index_document(self) -> typing.Optional[str]:
        """The index page for the site like 'index.html'.

        default
        :default: - index.html
        """
        return self._values.get("website_index_document")

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WebsiteBucketProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cloudcomponents/cdk-static-website.StaticWebsiteProps",
    jsii_struct_bases=[WebsiteBucketProps],
    name_mapping={
        "bucket_name": "bucketName",
        "disable_upload": "disableUpload",
        "removal_policy": "removalPolicy",
        "source": "source",
        "website_error_document": "websiteErrorDocument",
        "website_index_document": "websiteIndexDocument",
        "alias_configuration": "aliasConfiguration",
        "bucket_configuration": "bucketConfiguration",
        "disable_i_pv6": "disableIPv6",
        "web_acl_id": "webACLId",
    },
)
class StaticWebsiteProps(WebsiteBucketProps):
    def __init__(
        self,
        *,
        bucket_name: typing.Optional[str] = None,
        disable_upload: typing.Optional[bool] = None,
        removal_policy: typing.Optional[aws_cdk.core.RemovalPolicy] = None,
        source: typing.Optional[str] = None,
        website_error_document: typing.Optional[str] = None,
        website_index_document: typing.Optional[str] = None,
        alias_configuration: typing.Optional["AliasProps"] = None,
        bucket_configuration: typing.Optional["WebsiteBucketProps"] = None,
        disable_i_pv6: typing.Optional[bool] = None,
        web_acl_id: typing.Optional[str] = None,
    ) -> None:
        """
        :param bucket_name: Name of the bucket. Default: - Assigned by CloudFormation (recommended).
        :param disable_upload: Disable website deployment. Default: - false
        :param removal_policy: Policy to apply when the bucket is removed from this stack. Default: - The bucket will be orphaned.
        :param source: The source from which to deploy the website. Default: - Dummy placeholder
        :param website_error_document: The error page for the site like 'error.html'. Default: - error.html
        :param website_index_document: The index page for the site like 'index.html'. Default: - index.html
        :param alias_configuration: AliasConfiguration is used to configured CloudFront to respond to requests on custom domain names. Default: - No custom domain names are set up
        :param bucket_configuration: BucketConfiguration is used to configured the S3 website bucket. Default: - The website bucket is provided with default values
        :param disable_i_pv6: An override flag that allows you to turn off support for IPv6 if required. Default: - Cloudfront IPv6 support is enabled and if you've supplied an aliasConfiguration, an AAAA record will be created for your service, set this to true to switch this off.
        :param web_acl_id: AWS WAF WebACL to associate with this CloudFront distribution. Default: - No AWS Web Application Firewall web access control list (web ACL)
        """
        if isinstance(alias_configuration, dict):
            alias_configuration = AliasProps(**alias_configuration)
        if isinstance(bucket_configuration, dict):
            bucket_configuration = WebsiteBucketProps(**bucket_configuration)
        self._values = {}
        if bucket_name is not None:
            self._values["bucket_name"] = bucket_name
        if disable_upload is not None:
            self._values["disable_upload"] = disable_upload
        if removal_policy is not None:
            self._values["removal_policy"] = removal_policy
        if source is not None:
            self._values["source"] = source
        if website_error_document is not None:
            self._values["website_error_document"] = website_error_document
        if website_index_document is not None:
            self._values["website_index_document"] = website_index_document
        if alias_configuration is not None:
            self._values["alias_configuration"] = alias_configuration
        if bucket_configuration is not None:
            self._values["bucket_configuration"] = bucket_configuration
        if disable_i_pv6 is not None:
            self._values["disable_i_pv6"] = disable_i_pv6
        if web_acl_id is not None:
            self._values["web_acl_id"] = web_acl_id

    @builtins.property
    def bucket_name(self) -> typing.Optional[str]:
        """Name of the bucket.

        default
        :default: - Assigned by CloudFormation (recommended).
        """
        return self._values.get("bucket_name")

    @builtins.property
    def disable_upload(self) -> typing.Optional[bool]:
        """Disable website deployment.

        default
        :default: - false
        """
        return self._values.get("disable_upload")

    @builtins.property
    def removal_policy(self) -> typing.Optional[aws_cdk.core.RemovalPolicy]:
        """Policy to apply when the bucket is removed from this stack.

        default
        :default: - The bucket will be orphaned.
        """
        return self._values.get("removal_policy")

    @builtins.property
    def source(self) -> typing.Optional[str]:
        """The source from which to deploy the website.

        default
        :default: - Dummy placeholder
        """
        return self._values.get("source")

    @builtins.property
    def website_error_document(self) -> typing.Optional[str]:
        """The error page for the site like 'error.html'.

        default
        :default: - error.html
        """
        return self._values.get("website_error_document")

    @builtins.property
    def website_index_document(self) -> typing.Optional[str]:
        """The index page for the site like 'index.html'.

        default
        :default: - index.html
        """
        return self._values.get("website_index_document")

    @builtins.property
    def alias_configuration(self) -> typing.Optional["AliasProps"]:
        """AliasConfiguration is used to configured CloudFront to respond to requests on custom domain names.

        default
        :default: - No custom domain names are set up
        """
        return self._values.get("alias_configuration")

    @builtins.property
    def bucket_configuration(self) -> typing.Optional["WebsiteBucketProps"]:
        """BucketConfiguration is used to configured the S3 website bucket.

        default
        :default: - The website bucket is provided with default values
        """
        return self._values.get("bucket_configuration")

    @builtins.property
    def disable_i_pv6(self) -> typing.Optional[bool]:
        """An override flag that allows you to turn off support for IPv6 if required.

        default
        :default:

        - Cloudfront IPv6 support is enabled and if you've supplied an aliasConfiguration, an
          AAAA record will be created for your service, set this to true to switch this off.
        """
        return self._values.get("disable_i_pv6")

    @builtins.property
    def web_acl_id(self) -> typing.Optional[str]:
        """AWS WAF WebACL to associate with this CloudFront distribution.

        default
        :default: - No AWS Web Application Firewall web access control list (web ACL)
        """
        return self._values.get("web_acl_id")

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StaticWebsiteProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AliasProps",
    "StaticWebsite",
    "StaticWebsiteProps",
    "WebsiteAliasRecord",
    "WebsiteAliasRecordProps",
    "WebsiteBucket",
    "WebsiteBucketProps",
]

publication.publish()
