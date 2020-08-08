"""
[![cloudcomponents Logo](https://raw.githubusercontent.com/cloudcomponents/cdk-constructs/master/logo.png)](https://github.com/cloudcomponents/cdk-constructs)

# @cloudcomponents/cdk-deletable-bucket

[![Build Status](https://travis-ci.org/cloudcomponents/cdk-constructs.svg?branch=master)](https://travis-ci.org/cloudcomponents/cdk-constructs)
[![cdkdx](https://img.shields.io/badge/buildtool-cdkdx-blue.svg)](https://github.com/hupe1980/cdkdx)
[![typescript](https://img.shields.io/badge/jsii-typescript-blueviolet.svg)](https://www.npmjs.com/package/@cloudcomponents/cdk-deletable-bucket)
[![python](https://img.shields.io/badge/jsii-python-blueviolet.svg)](https://pypi.org/project/cloudcomponents.cdk-deletable-bucket/)

> Bucket with content cleanup to allow bucket deletion when the stack will be destroyed

## Install

TypeScript/JavaScript:

```bash
npm i @cloudcomponents/cdk-deletable-bucket
```

Python:

```bash
pip install cloudcomponents.cdk-deletable-bucket
```

## How to use

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
from aws_cdk.core import Construct, Stack, StackProps
from cloudcomponents.cdk_deletable_bucket import DeletableBucket

class DeletableBucketStack(Stack):
    def __init__(self, scope, id, *, description=None, env=None, stackName=None, tags=None, synthesizer=None, terminationProtection=None):
        super().__init__(scope, id, description=description, env=env, stackName=stackName, tags=tags, synthesizer=synthesizer, terminationProtection=terminationProtection)

        DeletableBucket(self, "DeletableBucket",
            bucket_name="bucket2delete",
            force_delete=True
        )
```

## API Reference

See [API.md](https://github.com/cloudcomponents/cdk-constructs/tree/master/packages/cdk-deletable-bucket/API.md).

## Example

See more complete [examples](https://github.com/cloudcomponents/cdk-constructs/tree/master/examples).

## License

[MIT](https://github.com/cloudcomponents/cdk-constructs/tree/master/packages/cdk-deletable-bucket/LICENSE)
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

import aws_cdk.aws_kms
import aws_cdk.aws_s3
import aws_cdk.core


class DeletableBucket(
    aws_cdk.aws_s3.Bucket,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cloudcomponents/cdk-deletable-bucket.DeletableBucket",
):
    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: str,
        *,
        force_delete: typing.Optional[bool] = None,
        access_control: typing.Optional[aws_cdk.aws_s3.BucketAccessControl] = None,
        block_public_access: typing.Optional[aws_cdk.aws_s3.BlockPublicAccess] = None,
        bucket_name: typing.Optional[str] = None,
        cors: typing.Optional[typing.List[aws_cdk.aws_s3.CorsRule]] = None,
        encryption: typing.Optional[aws_cdk.aws_s3.BucketEncryption] = None,
        encryption_key: typing.Optional[aws_cdk.aws_kms.IKey] = None,
        inventories: typing.Optional[typing.List[aws_cdk.aws_s3.Inventory]] = None,
        lifecycle_rules: typing.Optional[
            typing.List[aws_cdk.aws_s3.LifecycleRule]
        ] = None,
        metrics: typing.Optional[typing.List[aws_cdk.aws_s3.BucketMetrics]] = None,
        public_read_access: typing.Optional[bool] = None,
        removal_policy: typing.Optional[aws_cdk.core.RemovalPolicy] = None,
        server_access_logs_bucket: typing.Optional[aws_cdk.aws_s3.IBucket] = None,
        server_access_logs_prefix: typing.Optional[str] = None,
        versioned: typing.Optional[bool] = None,
        website_error_document: typing.Optional[str] = None,
        website_index_document: typing.Optional[str] = None,
        website_redirect: typing.Optional[aws_cdk.aws_s3.RedirectTarget] = None,
        website_routing_rules: typing.Optional[
            typing.List[aws_cdk.aws_s3.RoutingRule]
        ] = None,
    ) -> None:
        """
        :param scope: -
        :param id: -
        :param force_delete: If the buckets contains objects, forces the deletion during stack deletion. Default: false
        :param access_control: Specifies a canned ACL that grants predefined permissions to the bucket. Default: BucketAccessControl.PRIVATE
        :param block_public_access: The block public access configuration of this bucket. Default: false New buckets and objects don't allow public access, but users can modify bucket policies or object permissions to allow public access.
        :param bucket_name: Physical name of this bucket. Default: - Assigned by CloudFormation (recommended).
        :param cors: The CORS configuration of this bucket. Default: - No CORS configuration.
        :param encryption: The kind of server-side encryption to apply to this bucket. If you choose KMS, you can specify a KMS key via ``encryptionKey``. If encryption key is not specified, a key will automatically be created. Default: - ``Kms`` if ``encryptionKey`` is specified, or ``Unencrypted`` otherwise.
        :param encryption_key: External KMS key to use for bucket encryption. The 'encryption' property must be either not specified or set to "Kms". An error will be emitted if encryption is set to "Unencrypted" or "Managed". Default: - If encryption is set to "Kms" and this property is undefined, a new KMS key will be created and associated with this bucket.
        :param inventories: The inventory configuration of the bucket. Default: - No inventory configuration
        :param lifecycle_rules: Rules that define how Amazon S3 manages objects during their lifetime. Default: - No lifecycle rules.
        :param metrics: The metrics configuration of this bucket. Default: - No metrics configuration.
        :param public_read_access: Grants public read access to all objects in the bucket. Similar to calling ``bucket.grantPublicAccess()`` Default: false
        :param removal_policy: Policy to apply when the bucket is removed from this stack. Default: - The bucket will be orphaned.
        :param server_access_logs_bucket: Destination bucket for the server access logs. Default: - If "serverAccessLogsPrefix" undefined - access logs disabled, otherwise - log to current bucket.
        :param server_access_logs_prefix: Optional log file prefix to use for the bucket's access logs. If defined without "serverAccessLogsBucket", enables access logs to current bucket with this prefix. Default: - No log file prefix
        :param versioned: Whether this bucket should have versioning turned on or not. Default: false
        :param website_error_document: The name of the error document (e.g. "404.html") for the website. ``websiteIndexDocument`` must also be set if this is set. Default: - No error document.
        :param website_index_document: The name of the index document (e.g. "index.html") for the website. Enables static website hosting for this bucket. Default: - No index document.
        :param website_redirect: Specifies the redirect behavior of all requests to a website endpoint of a bucket. If you specify this property, you can't specify "websiteIndexDocument", "websiteErrorDocument" nor , "websiteRoutingRules". Default: - No redirection.
        :param website_routing_rules: Rules that define when a redirect is applied and the redirect behavior. Default: - No redirection rules.
        """
        props = DeletableBucketProps(
            force_delete=force_delete,
            access_control=access_control,
            block_public_access=block_public_access,
            bucket_name=bucket_name,
            cors=cors,
            encryption=encryption,
            encryption_key=encryption_key,
            inventories=inventories,
            lifecycle_rules=lifecycle_rules,
            metrics=metrics,
            public_read_access=public_read_access,
            removal_policy=removal_policy,
            server_access_logs_bucket=server_access_logs_bucket,
            server_access_logs_prefix=server_access_logs_prefix,
            versioned=versioned,
            website_error_document=website_error_document,
            website_index_document=website_index_document,
            website_redirect=website_redirect,
            website_routing_rules=website_routing_rules,
        )

        jsii.create(DeletableBucket, self, [scope, id, props])


@jsii.data_type(
    jsii_type="@cloudcomponents/cdk-deletable-bucket.DeletableBucketProps",
    jsii_struct_bases=[aws_cdk.aws_s3.BucketProps],
    name_mapping={
        "access_control": "accessControl",
        "block_public_access": "blockPublicAccess",
        "bucket_name": "bucketName",
        "cors": "cors",
        "encryption": "encryption",
        "encryption_key": "encryptionKey",
        "inventories": "inventories",
        "lifecycle_rules": "lifecycleRules",
        "metrics": "metrics",
        "public_read_access": "publicReadAccess",
        "removal_policy": "removalPolicy",
        "server_access_logs_bucket": "serverAccessLogsBucket",
        "server_access_logs_prefix": "serverAccessLogsPrefix",
        "versioned": "versioned",
        "website_error_document": "websiteErrorDocument",
        "website_index_document": "websiteIndexDocument",
        "website_redirect": "websiteRedirect",
        "website_routing_rules": "websiteRoutingRules",
        "force_delete": "forceDelete",
    },
)
class DeletableBucketProps(aws_cdk.aws_s3.BucketProps):
    def __init__(
        self,
        *,
        access_control: typing.Optional[aws_cdk.aws_s3.BucketAccessControl] = None,
        block_public_access: typing.Optional[aws_cdk.aws_s3.BlockPublicAccess] = None,
        bucket_name: typing.Optional[str] = None,
        cors: typing.Optional[typing.List[aws_cdk.aws_s3.CorsRule]] = None,
        encryption: typing.Optional[aws_cdk.aws_s3.BucketEncryption] = None,
        encryption_key: typing.Optional[aws_cdk.aws_kms.IKey] = None,
        inventories: typing.Optional[typing.List[aws_cdk.aws_s3.Inventory]] = None,
        lifecycle_rules: typing.Optional[
            typing.List[aws_cdk.aws_s3.LifecycleRule]
        ] = None,
        metrics: typing.Optional[typing.List[aws_cdk.aws_s3.BucketMetrics]] = None,
        public_read_access: typing.Optional[bool] = None,
        removal_policy: typing.Optional[aws_cdk.core.RemovalPolicy] = None,
        server_access_logs_bucket: typing.Optional[aws_cdk.aws_s3.IBucket] = None,
        server_access_logs_prefix: typing.Optional[str] = None,
        versioned: typing.Optional[bool] = None,
        website_error_document: typing.Optional[str] = None,
        website_index_document: typing.Optional[str] = None,
        website_redirect: typing.Optional[aws_cdk.aws_s3.RedirectTarget] = None,
        website_routing_rules: typing.Optional[
            typing.List[aws_cdk.aws_s3.RoutingRule]
        ] = None,
        force_delete: typing.Optional[bool] = None,
    ) -> None:
        """
        :param access_control: Specifies a canned ACL that grants predefined permissions to the bucket. Default: BucketAccessControl.PRIVATE
        :param block_public_access: The block public access configuration of this bucket. Default: false New buckets and objects don't allow public access, but users can modify bucket policies or object permissions to allow public access.
        :param bucket_name: Physical name of this bucket. Default: - Assigned by CloudFormation (recommended).
        :param cors: The CORS configuration of this bucket. Default: - No CORS configuration.
        :param encryption: The kind of server-side encryption to apply to this bucket. If you choose KMS, you can specify a KMS key via ``encryptionKey``. If encryption key is not specified, a key will automatically be created. Default: - ``Kms`` if ``encryptionKey`` is specified, or ``Unencrypted`` otherwise.
        :param encryption_key: External KMS key to use for bucket encryption. The 'encryption' property must be either not specified or set to "Kms". An error will be emitted if encryption is set to "Unencrypted" or "Managed". Default: - If encryption is set to "Kms" and this property is undefined, a new KMS key will be created and associated with this bucket.
        :param inventories: The inventory configuration of the bucket. Default: - No inventory configuration
        :param lifecycle_rules: Rules that define how Amazon S3 manages objects during their lifetime. Default: - No lifecycle rules.
        :param metrics: The metrics configuration of this bucket. Default: - No metrics configuration.
        :param public_read_access: Grants public read access to all objects in the bucket. Similar to calling ``bucket.grantPublicAccess()`` Default: false
        :param removal_policy: Policy to apply when the bucket is removed from this stack. Default: - The bucket will be orphaned.
        :param server_access_logs_bucket: Destination bucket for the server access logs. Default: - If "serverAccessLogsPrefix" undefined - access logs disabled, otherwise - log to current bucket.
        :param server_access_logs_prefix: Optional log file prefix to use for the bucket's access logs. If defined without "serverAccessLogsBucket", enables access logs to current bucket with this prefix. Default: - No log file prefix
        :param versioned: Whether this bucket should have versioning turned on or not. Default: false
        :param website_error_document: The name of the error document (e.g. "404.html") for the website. ``websiteIndexDocument`` must also be set if this is set. Default: - No error document.
        :param website_index_document: The name of the index document (e.g. "index.html") for the website. Enables static website hosting for this bucket. Default: - No index document.
        :param website_redirect: Specifies the redirect behavior of all requests to a website endpoint of a bucket. If you specify this property, you can't specify "websiteIndexDocument", "websiteErrorDocument" nor , "websiteRoutingRules". Default: - No redirection.
        :param website_routing_rules: Rules that define when a redirect is applied and the redirect behavior. Default: - No redirection rules.
        :param force_delete: If the buckets contains objects, forces the deletion during stack deletion. Default: false
        """
        if isinstance(website_redirect, dict):
            website_redirect = aws_cdk.aws_s3.RedirectTarget(**website_redirect)
        self._values = {}
        if access_control is not None:
            self._values["access_control"] = access_control
        if block_public_access is not None:
            self._values["block_public_access"] = block_public_access
        if bucket_name is not None:
            self._values["bucket_name"] = bucket_name
        if cors is not None:
            self._values["cors"] = cors
        if encryption is not None:
            self._values["encryption"] = encryption
        if encryption_key is not None:
            self._values["encryption_key"] = encryption_key
        if inventories is not None:
            self._values["inventories"] = inventories
        if lifecycle_rules is not None:
            self._values["lifecycle_rules"] = lifecycle_rules
        if metrics is not None:
            self._values["metrics"] = metrics
        if public_read_access is not None:
            self._values["public_read_access"] = public_read_access
        if removal_policy is not None:
            self._values["removal_policy"] = removal_policy
        if server_access_logs_bucket is not None:
            self._values["server_access_logs_bucket"] = server_access_logs_bucket
        if server_access_logs_prefix is not None:
            self._values["server_access_logs_prefix"] = server_access_logs_prefix
        if versioned is not None:
            self._values["versioned"] = versioned
        if website_error_document is not None:
            self._values["website_error_document"] = website_error_document
        if website_index_document is not None:
            self._values["website_index_document"] = website_index_document
        if website_redirect is not None:
            self._values["website_redirect"] = website_redirect
        if website_routing_rules is not None:
            self._values["website_routing_rules"] = website_routing_rules
        if force_delete is not None:
            self._values["force_delete"] = force_delete

    @builtins.property
    def access_control(self) -> typing.Optional[aws_cdk.aws_s3.BucketAccessControl]:
        """Specifies a canned ACL that grants predefined permissions to the bucket.

        default
        :default: BucketAccessControl.PRIVATE
        """
        return self._values.get("access_control")

    @builtins.property
    def block_public_access(self) -> typing.Optional[aws_cdk.aws_s3.BlockPublicAccess]:
        """The block public access configuration of this bucket.

        default
        :default:

        false New buckets and objects don't allow public access, but users can modify bucket
        policies or object permissions to allow public access.

        see
        :see: https://docs.aws.amazon.com/AmazonS3/latest/dev/access-control-block-public-access.html
        """
        return self._values.get("block_public_access")

    @builtins.property
    def bucket_name(self) -> typing.Optional[str]:
        """Physical name of this bucket.

        default
        :default: - Assigned by CloudFormation (recommended).
        """
        return self._values.get("bucket_name")

    @builtins.property
    def cors(self) -> typing.Optional[typing.List[aws_cdk.aws_s3.CorsRule]]:
        """The CORS configuration of this bucket.

        default
        :default: - No CORS configuration.

        see
        :see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-cors.html
        """
        return self._values.get("cors")

    @builtins.property
    def encryption(self) -> typing.Optional[aws_cdk.aws_s3.BucketEncryption]:
        """The kind of server-side encryption to apply to this bucket.

        If you choose KMS, you can specify a KMS key via ``encryptionKey``. If
        encryption key is not specified, a key will automatically be created.

        default
        :default: - ``Kms`` if ``encryptionKey`` is specified, or ``Unencrypted`` otherwise.
        """
        return self._values.get("encryption")

    @builtins.property
    def encryption_key(self) -> typing.Optional[aws_cdk.aws_kms.IKey]:
        """External KMS key to use for bucket encryption.

        The 'encryption' property must be either not specified or set to "Kms".
        An error will be emitted if encryption is set to "Unencrypted" or
        "Managed".

        default
        :default:

        - If encryption is set to "Kms" and this property is undefined,
          a new KMS key will be created and associated with this bucket.
        """
        return self._values.get("encryption_key")

    @builtins.property
    def inventories(self) -> typing.Optional[typing.List[aws_cdk.aws_s3.Inventory]]:
        """The inventory configuration of the bucket.

        default
        :default: - No inventory configuration

        see
        :see: https://docs.aws.amazon.com/AmazonS3/latest/dev/storage-inventory.html
        """
        return self._values.get("inventories")

    @builtins.property
    def lifecycle_rules(
        self,
    ) -> typing.Optional[typing.List[aws_cdk.aws_s3.LifecycleRule]]:
        """Rules that define how Amazon S3 manages objects during their lifetime.

        default
        :default: - No lifecycle rules.
        """
        return self._values.get("lifecycle_rules")

    @builtins.property
    def metrics(self) -> typing.Optional[typing.List[aws_cdk.aws_s3.BucketMetrics]]:
        """The metrics configuration of this bucket.

        default
        :default: - No metrics configuration.

        see
        :see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-metricsconfiguration.html
        """
        return self._values.get("metrics")

    @builtins.property
    def public_read_access(self) -> typing.Optional[bool]:
        """Grants public read access to all objects in the bucket.

        Similar to calling ``bucket.grantPublicAccess()``

        default
        :default: false
        """
        return self._values.get("public_read_access")

    @builtins.property
    def removal_policy(self) -> typing.Optional[aws_cdk.core.RemovalPolicy]:
        """Policy to apply when the bucket is removed from this stack.

        default
        :default: - The bucket will be orphaned.
        """
        return self._values.get("removal_policy")

    @builtins.property
    def server_access_logs_bucket(self) -> typing.Optional[aws_cdk.aws_s3.IBucket]:
        """Destination bucket for the server access logs.

        default
        :default: - If "serverAccessLogsPrefix" undefined - access logs disabled, otherwise - log to current bucket.
        """
        return self._values.get("server_access_logs_bucket")

    @builtins.property
    def server_access_logs_prefix(self) -> typing.Optional[str]:
        """Optional log file prefix to use for the bucket's access logs.

        If defined without "serverAccessLogsBucket", enables access logs to current bucket with this prefix.

        default
        :default: - No log file prefix
        """
        return self._values.get("server_access_logs_prefix")

    @builtins.property
    def versioned(self) -> typing.Optional[bool]:
        """Whether this bucket should have versioning turned on or not.

        default
        :default: false
        """
        return self._values.get("versioned")

    @builtins.property
    def website_error_document(self) -> typing.Optional[str]:
        """The name of the error document (e.g. "404.html") for the website. ``websiteIndexDocument`` must also be set if this is set.

        default
        :default: - No error document.
        """
        return self._values.get("website_error_document")

    @builtins.property
    def website_index_document(self) -> typing.Optional[str]:
        """The name of the index document (e.g. "index.html") for the website. Enables static website hosting for this bucket.

        default
        :default: - No index document.
        """
        return self._values.get("website_index_document")

    @builtins.property
    def website_redirect(self) -> typing.Optional[aws_cdk.aws_s3.RedirectTarget]:
        """Specifies the redirect behavior of all requests to a website endpoint of a bucket.

        If you specify this property, you can't specify "websiteIndexDocument", "websiteErrorDocument" nor , "websiteRoutingRules".

        default
        :default: - No redirection.
        """
        return self._values.get("website_redirect")

    @builtins.property
    def website_routing_rules(
        self,
    ) -> typing.Optional[typing.List[aws_cdk.aws_s3.RoutingRule]]:
        """Rules that define when a redirect is applied and the redirect behavior.

        default
        :default: - No redirection rules.
        """
        return self._values.get("website_routing_rules")

    @builtins.property
    def force_delete(self) -> typing.Optional[bool]:
        """If the buckets contains objects, forces the deletion during stack deletion.

        default
        :default: false
        """
        return self._values.get("force_delete")

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DeletableBucketProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EmptyBucket(
    aws_cdk.core.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cloudcomponents/cdk-deletable-bucket.EmptyBucket",
):
    def __init__(
        self, scope: aws_cdk.core.Construct, id: str, *, bucket: aws_cdk.aws_s3.IBucket
    ) -> None:
        """
        :param scope: -
        :param id: -
        :param bucket: -
        """
        props = EmptyBucketProps(bucket=bucket)

        jsii.create(EmptyBucket, self, [scope, id, props])


@jsii.data_type(
    jsii_type="@cloudcomponents/cdk-deletable-bucket.EmptyBucketProps",
    jsii_struct_bases=[],
    name_mapping={"bucket": "bucket"},
)
class EmptyBucketProps:
    def __init__(self, *, bucket: aws_cdk.aws_s3.IBucket) -> None:
        """
        :param bucket: -
        """
        self._values = {
            "bucket": bucket,
        }

    @builtins.property
    def bucket(self) -> aws_cdk.aws_s3.IBucket:
        return self._values.get("bucket")

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EmptyBucketProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "DeletableBucket",
    "DeletableBucketProps",
    "EmptyBucket",
    "EmptyBucketProps",
]

publication.publish()
