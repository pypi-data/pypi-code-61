"""
[![cloudcomponents Logo](https://raw.githubusercontent.com/cloudcomponents/cdk-constructs/master/logo.png)](https://github.com/cloudcomponents/cdk-constructs)

# @cloudcomponents/cdk-dynamodb-seeder

[![Build Status](https://travis-ci.org/cloudcomponents/cdk-constructs.svg?branch=master)](https://travis-ci.org/cloudcomponents/cdk-constructs)
[![cdkdx](https://img.shields.io/badge/buildtool-cdkdx-blue.svg)](https://github.com/hupe1980/cdkdx)
[![typescript](https://img.shields.io/badge/jsii-typescript-blueviolet.svg)](https://www.npmjs.com/package/@cloudcomponents/cdk-dynamodb-seeder)
[![python](https://img.shields.io/badge/jsii-python-blueviolet.svg)](https://pypi.org/project/cloudcomponents.cdk-dynamodb-seeder/)

> A seeder for dynamodb tables

## Install

TypeScript/JavaScript:

```bash
npm i @cloudcomponents/cdk-dynamodb-seeder
```

Python:

```bash
pip install cloudcomponents.cdk-dynamodb-seeder
```

## How to use

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
import path as path
from aws_cdk.core import Construct, Stack, StackProps, RemovalPolicy
from aws_cdk.aws_dynamodb import Table, AttributeType
from aws_cdk.aws_s3 import Bucket
from cloudcomponents.cdk_dynamodb_seeder import DynamoDBSeeder, Seeds

class DynamoDBSeederStack(Stack):
    def __init__(self, scope, id, *, description=None, env=None, stackName=None, tags=None, synthesizer=None, terminationProtection=None):
        super().__init__(scope, id, description=description, env=env, stackName=stackName, tags=tags, synthesizer=synthesizer, terminationProtection=terminationProtection)

        table = Table(self, "Table",
            partition_key=Attribute(
                name="id",
                type=AttributeType.NUMBER
            ),
            removal_policy=RemovalPolicy.DESTROY
        )

        DynamoDBSeeder(self, "JsonFileSeeder",
            table=table,
            seeds=Seeds.from_json_file(path.join(__dirname, "..", "seeds.json"))
        )

        DynamoDBSeeder(self, "InlineSeeder",
            table=table,
            seeds=Seeds.from_inline([{
                "id": 3,
                "column": "foo"
            }, {
                "id": 4,
                "column": "bar"
            }
            ])
        )

        seeds_bucket = Bucket.from_bucket_name(self, "SeedsBucket", "my-seeds-bucket")

        DynamoDBSeeder(self, "BucketSeeder",
            table=table,
            seeds=Seeds.from_bucket(seeds_bucket, "seeds.json")
        )
```

## API Reference

See [API.md](https://github.com/cloudcomponents/cdk-constructs/tree/master/packages/cdk-dynamodb-seeder/API.md).

## Example

See more complete [examples](https://github.com/cloudcomponents/cdk-constructs/tree/master/examples).

## License

[MIT](https://github.com/cloudcomponents/cdk-constructs/tree/master/packages/cdk-dynamodb-seeder/LICENSE)
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

import aws_cdk.assets
import aws_cdk.aws_dynamodb
import aws_cdk.aws_iam
import aws_cdk.aws_s3
import aws_cdk.aws_s3_assets
import aws_cdk.core


class DynamoDBSeeder(
    aws_cdk.core.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cloudcomponents/cdk-dynamodb-seeder.DynamoDBSeeder",
):
    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: str,
        *,
        seeds: "Seeds",
        table: aws_cdk.aws_dynamodb.ITable,
        timeout: typing.Optional[aws_cdk.core.Duration] = None,
    ) -> None:
        """
        :param scope: -
        :param id: -
        :param seeds: -
        :param table: -
        :param timeout: The function execution time (in seconds) after which Lambda terminates the function. Because the execution time affects cost, set this value based on the function's expected execution time. Default: Duration.minutes(15)
        """
        props = DynamoDBSeederProps(seeds=seeds, table=table, timeout=timeout)

        jsii.create(DynamoDBSeeder, self, [scope, id, props])


@jsii.data_type(
    jsii_type="@cloudcomponents/cdk-dynamodb-seeder.DynamoDBSeederProps",
    jsii_struct_bases=[],
    name_mapping={"seeds": "seeds", "table": "table", "timeout": "timeout"},
)
class DynamoDBSeederProps:
    def __init__(
        self,
        *,
        seeds: "Seeds",
        table: aws_cdk.aws_dynamodb.ITable,
        timeout: typing.Optional[aws_cdk.core.Duration] = None,
    ) -> None:
        """
        :param seeds: -
        :param table: -
        :param timeout: The function execution time (in seconds) after which Lambda terminates the function. Because the execution time affects cost, set this value based on the function's expected execution time. Default: Duration.minutes(15)
        """
        self._values = {
            "seeds": seeds,
            "table": table,
        }
        if timeout is not None:
            self._values["timeout"] = timeout

    @builtins.property
    def seeds(self) -> "Seeds":
        return self._values.get("seeds")

    @builtins.property
    def table(self) -> aws_cdk.aws_dynamodb.ITable:
        return self._values.get("table")

    @builtins.property
    def timeout(self) -> typing.Optional[aws_cdk.core.Duration]:
        """The function execution time (in seconds) after which Lambda terminates the function.

        Because the execution time affects cost, set this value
        based on the function's expected execution time.

        default
        :default: Duration.minutes(15)
        """
        return self._values.get("timeout")

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DynamoDBSeederProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Seeds(
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="@cloudcomponents/cdk-dynamodb-seeder.Seeds",
):
    @builtins.staticmethod
    def __jsii_proxy_class__():
        return _SeedsProxy

    def __init__(self) -> None:
        jsii.create(Seeds, self, [])

    @jsii.member(jsii_name="fromBucket")
    @builtins.classmethod
    def from_bucket(
        cls,
        bucket: aws_cdk.aws_s3.IBucket,
        key: str,
        object_version: typing.Optional[str] = None,
    ) -> "S3Seeds":
        """
        :param bucket: The S3 bucket.
        :param key: The object key.
        :param object_version: Optional S3 object version.

        return
        :return: ``S3Seeds`` associated with the specified S3 object.
        """
        return jsii.sinvoke(cls, "fromBucket", [bucket, key, object_version])

    @jsii.member(jsii_name="fromInline")
    @builtins.classmethod
    def from_inline(
        cls, seeds: typing.List[typing.Mapping[str, typing.Any]]
    ) -> "InlineSeeds":
        """
        :param seeds: The actual json code (limited to 4KiB).

        return
        :return: ``InlineSeeds`` with inline seeds.
        """
        return jsii.sinvoke(cls, "fromInline", [seeds])

    @jsii.member(jsii_name="fromJsonFile")
    @builtins.classmethod
    def from_json_file(
        cls,
        path: str,
        *,
        readers: typing.Optional[typing.List[aws_cdk.aws_iam.IGrantable]] = None,
        source_hash: typing.Optional[str] = None,
        exclude: typing.Optional[typing.List[str]] = None,
        follow: typing.Optional[aws_cdk.assets.FollowMode] = None,
        asset_hash: typing.Optional[str] = None,
        asset_hash_type: typing.Optional[aws_cdk.core.AssetHashType] = None,
        bundling: typing.Optional[aws_cdk.core.BundlingOptions] = None,
    ) -> "JsonFileSeeds":
        """Loads the seeds from a local disk path and uploads it to s3.

        :param path: Path to json seeds file.
        :param readers: A list of principals that should be able to read this asset from S3. You can use ``asset.grantRead(principal)`` to grant read permissions later. Default: - No principals that can read file asset.
        :param source_hash: Custom hash to use when identifying the specific version of the asset. For consistency, this custom hash will be SHA256 hashed and encoded as hex. The resulting hash will be the asset hash. NOTE: the source hash is used in order to identify a specific revision of the asset, and used for optimizing and caching deployment activities related to this asset such as packaging, uploading to Amazon S3, etc. If you chose to customize the source hash, you will need to make sure it is updated every time the source changes, or otherwise it is possible that some deployments will not be invalidated. Default: - automatically calculate source hash based on the contents of the source file or directory.
        :param exclude: Glob patterns to exclude from the copy. Default: nothing is excluded
        :param follow: A strategy for how to handle symlinks. Default: Never
        :param asset_hash: Specify a custom hash for this asset. If ``assetHashType`` is set it must be set to ``AssetHashType.CUSTOM``. For consistency, this custom hash will be SHA256 hashed and encoded as hex. The resulting hash will be the asset hash. NOTE: the hash is used in order to identify a specific revision of the asset, and used for optimizing and caching deployment activities related to this asset such as packaging, uploading to Amazon S3, etc. If you chose to customize the hash, you will need to make sure it is updated every time the asset changes, or otherwise it is possible that some deployments will not be invalidated. Default: - based on ``assetHashType``
        :param asset_hash_type: Specifies the type of hash to calculate for this asset. If ``assetHash`` is configured, this option must be ``undefined`` or ``AssetHashType.CUSTOM``. Default: - the default is ``AssetHashType.SOURCE``, but if ``assetHash`` is explicitly specified this value defaults to ``AssetHashType.CUSTOM``.
        :param bundling: Bundle the asset by executing a command in a Docker container. The asset path will be mounted at ``/asset-input``. The Docker container is responsible for putting content at ``/asset-output``. The content at ``/asset-output`` will be zipped and used as the final asset. Default: - uploaded as-is to S3 if the asset is a regular file or a .zip file, archived into a .zip file and uploaded to S3 otherwise

        return
        :return: ``JsonFileSeeds`` associated with the specified S3 object.
        """
        options = aws_cdk.aws_s3_assets.AssetOptions(
            readers=readers,
            source_hash=source_hash,
            exclude=exclude,
            follow=follow,
            asset_hash=asset_hash,
            asset_hash_type=asset_hash_type,
            bundling=bundling,
        )

        return jsii.sinvoke(cls, "fromJsonFile", [path, options])

    @jsii.member(jsii_name="bind")
    @abc.abstractmethod
    def bind(self, scope: aws_cdk.core.Construct) -> "SeedsConfig":
        """Called when the seeder is initialized to allow this object to bind to the stack.

        :param scope: The binding scope.
        """
        ...


class _SeedsProxy(Seeds):
    @jsii.member(jsii_name="bind")
    def bind(self, scope: aws_cdk.core.Construct) -> "SeedsConfig":
        """Called when the seeder is initialized to allow this object to bind to the stack.

        :param scope: The binding scope.
        """
        return jsii.invoke(self, "bind", [scope])


@jsii.data_type(
    jsii_type="@cloudcomponents/cdk-dynamodb-seeder.SeedsConfig",
    jsii_struct_bases=[],
    name_mapping={"inline_seeds": "inlineSeeds", "s3_location": "s3Location"},
)
class SeedsConfig:
    def __init__(
        self,
        *,
        inline_seeds: typing.Optional[str] = None,
        s3_location: typing.Optional[aws_cdk.aws_s3.Location] = None,
    ) -> None:
        """
        :param inline_seeds: Inline seeds.
        :param s3_location: The location of the seeds in S3.
        """
        if isinstance(s3_location, dict):
            s3_location = aws_cdk.aws_s3.Location(**s3_location)
        self._values = {}
        if inline_seeds is not None:
            self._values["inline_seeds"] = inline_seeds
        if s3_location is not None:
            self._values["s3_location"] = s3_location

    @builtins.property
    def inline_seeds(self) -> typing.Optional[str]:
        """Inline seeds."""
        return self._values.get("inline_seeds")

    @builtins.property
    def s3_location(self) -> typing.Optional[aws_cdk.aws_s3.Location]:
        """The location of the seeds in S3."""
        return self._values.get("s3_location")

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SeedsConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class InlineSeeds(
    Seeds,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cloudcomponents/cdk-dynamodb-seeder.InlineSeeds",
):
    """Seeds from an inline json object (limited to 4KiB)."""

    def __init__(self, seeds: str) -> None:
        """
        :param seeds: -
        """
        jsii.create(InlineSeeds, self, [seeds])

    @jsii.member(jsii_name="bind")
    def bind(self, _scope: aws_cdk.core.Construct) -> "SeedsConfig":
        """Called when the seeder is initialized to allow this object to bind to the stack.

        :param _scope: -
        """
        return jsii.invoke(self, "bind", [_scope])


class JsonFileSeeds(
    Seeds,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cloudcomponents/cdk-dynamodb-seeder.JsonFileSeeds",
):
    """Seeds from a local json file."""

    def __init__(
        self,
        path: str,
        *,
        readers: typing.Optional[typing.List[aws_cdk.aws_iam.IGrantable]] = None,
        source_hash: typing.Optional[str] = None,
        exclude: typing.Optional[typing.List[str]] = None,
        follow: typing.Optional[aws_cdk.assets.FollowMode] = None,
        asset_hash: typing.Optional[str] = None,
        asset_hash_type: typing.Optional[aws_cdk.core.AssetHashType] = None,
        bundling: typing.Optional[aws_cdk.core.BundlingOptions] = None,
    ) -> None:
        """
        :param path: -
        :param readers: A list of principals that should be able to read this asset from S3. You can use ``asset.grantRead(principal)`` to grant read permissions later. Default: - No principals that can read file asset.
        :param source_hash: Custom hash to use when identifying the specific version of the asset. For consistency, this custom hash will be SHA256 hashed and encoded as hex. The resulting hash will be the asset hash. NOTE: the source hash is used in order to identify a specific revision of the asset, and used for optimizing and caching deployment activities related to this asset such as packaging, uploading to Amazon S3, etc. If you chose to customize the source hash, you will need to make sure it is updated every time the source changes, or otherwise it is possible that some deployments will not be invalidated. Default: - automatically calculate source hash based on the contents of the source file or directory.
        :param exclude: Glob patterns to exclude from the copy. Default: nothing is excluded
        :param follow: A strategy for how to handle symlinks. Default: Never
        :param asset_hash: Specify a custom hash for this asset. If ``assetHashType`` is set it must be set to ``AssetHashType.CUSTOM``. For consistency, this custom hash will be SHA256 hashed and encoded as hex. The resulting hash will be the asset hash. NOTE: the hash is used in order to identify a specific revision of the asset, and used for optimizing and caching deployment activities related to this asset such as packaging, uploading to Amazon S3, etc. If you chose to customize the hash, you will need to make sure it is updated every time the asset changes, or otherwise it is possible that some deployments will not be invalidated. Default: - based on ``assetHashType``
        :param asset_hash_type: Specifies the type of hash to calculate for this asset. If ``assetHash`` is configured, this option must be ``undefined`` or ``AssetHashType.CUSTOM``. Default: - the default is ``AssetHashType.SOURCE``, but if ``assetHash`` is explicitly specified this value defaults to ``AssetHashType.CUSTOM``.
        :param bundling: Bundle the asset by executing a command in a Docker container. The asset path will be mounted at ``/asset-input``. The Docker container is responsible for putting content at ``/asset-output``. The content at ``/asset-output`` will be zipped and used as the final asset. Default: - uploaded as-is to S3 if the asset is a regular file or a .zip file, archived into a .zip file and uploaded to S3 otherwise
        """
        options = aws_cdk.aws_s3_assets.AssetOptions(
            readers=readers,
            source_hash=source_hash,
            exclude=exclude,
            follow=follow,
            asset_hash=asset_hash,
            asset_hash_type=asset_hash_type,
            bundling=bundling,
        )

        jsii.create(JsonFileSeeds, self, [path, options])

    @jsii.member(jsii_name="bind")
    def bind(self, scope: aws_cdk.core.Construct) -> "SeedsConfig":
        """Called when the seeder is initialized to allow this object to bind to the stack.

        :param scope: -
        """
        return jsii.invoke(self, "bind", [scope])

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> str:
        return jsii.get(self, "path")


class S3Seeds(
    Seeds,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cloudcomponents/cdk-dynamodb-seeder.S3Seeds",
):
    """Seeds from an S3 archive."""

    def __init__(
        self,
        bucket: aws_cdk.aws_s3.IBucket,
        key: str,
        object_version: typing.Optional[str] = None,
    ) -> None:
        """
        :param bucket: -
        :param key: -
        :param object_version: -
        """
        jsii.create(S3Seeds, self, [bucket, key, object_version])

    @jsii.member(jsii_name="bind")
    def bind(self, _scope: aws_cdk.core.Construct) -> "SeedsConfig":
        """Called when the seeder is initialized to allow this object to bind to the stack.

        :param _scope: -
        """
        return jsii.invoke(self, "bind", [_scope])


__all__ = [
    "DynamoDBSeeder",
    "DynamoDBSeederProps",
    "InlineSeeds",
    "JsonFileSeeds",
    "S3Seeds",
    "Seeds",
    "SeedsConfig",
]

publication.publish()
