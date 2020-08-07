"""
## AWS Cloud9 Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

![cdk-constructs: Experimental](https://img.shields.io/badge/cdk--constructs-experimental-important.svg?style=for-the-badge)

> The APIs of higher level constructs in this module are experimental and under active development. They are subject to non-backward compatible changes or removal in any future version. These are not subject to the [Semantic Versioning](https://semver.org/) model and breaking changes will be announced in the release notes. This means that while you may use them, you may need to update your source code when upgrading to a newer version of this package.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

AWS Cloud9 is a cloud-based integrated development environment (IDE) that lets you write, run, and debug your code with just a browser. It includes a code editor, debugger, and terminal. Cloud9 comes prepackaged with essential tools for popular programming languages, including JavaScript, Python, PHP, and more, so you don’t need to install files or configure your development machine to start new projects. Since your Cloud9 IDE is cloud-based, you can work on your projects from your office, home, or anywhere using an internet-connected machine. Cloud9 also provides a seamless experience for developing serverless applications enabling you to easily define resources, debug, and switch between local and remote execution of serverless applications. With Cloud9, you can quickly share your development environment with your team, enabling you to pair program and track each other's inputs in real time.

### Creating EC2 Environment

EC2 Environments are defined with `Ec2Environment`. To create an EC2 environment in the private subnet, specify `subnetSelection` with private `subnetType`.

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_cloud9 as cloud9

# create a cloud9 ec2 environment in a new VPC
vpc = ec2.Vpc(self, "VPC", max_azs=3)
cloud9.Ec2Environment(self, "Cloud9Env", vpc=vpc)

# or create the cloud9 environment in the default VPC with specific instanceType
default_vpc = ec2.Vpc.from_lookup(self, "DefaultVPC", is_default=True)
cloud9.Ec2Environment(self, "Cloud9Env2",
    vpc=default_vpc,
    instance_type=ec2.InstanceType("t3.large")
)

# or specify in a different subnetSelection
c9env = cloud9.Ec2Environment(self, "Cloud9Env3",
    vpc=vpc,
    subnet_selection=SubnetSelection(
        subnet_type=ec2.SubnetType.PRIVATE
    )
)

# print the Cloud9 IDE URL in the output
cdk.CfnOutput(self, "URL", value=c9env.ide_url)
```

### Cloning Repositories

Use `clonedRepositories` to clone one or multiple AWS Codecommit repositories into the environment:

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
# create a codecommit repository to clone into the cloud9 environment
repo_new = codecommit.Repository(self, "RepoNew",
    repository_name="new-repo"
)

# import an existing codecommit repository to clone into the cloud9 environment
repo_existing = codecommit.Repository.from_repository_name(stack, "RepoExisting", "existing-repo")

# create a new Cloud9 environment and clone the two repositories
cloud9.Ec2Environment(stack, "C9Env",
    vpc=vpc,
    cloned_repositories=[
        cloud9.CloneRepository.from_code_commit(repo_new, "/src/new-repo"),
        cloud9.CloneRepository.from_code_commit(repo_existing, "/src/existing-repo")
    ]
)
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

import aws_cdk.aws_codecommit
import aws_cdk.aws_ec2
import aws_cdk.core


@jsii.implements(aws_cdk.core.IInspectable)
class CfnEnvironmentEC2(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-cloud9.CfnEnvironmentEC2",
):
    """A CloudFormation ``AWS::Cloud9::EnvironmentEC2``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloud9-environmentec2.html
    cloudformationResource:
    :cloudformationResource:: AWS::Cloud9::EnvironmentEC2
    """

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: str,
        *,
        instance_type: str,
        automatic_stop_time_minutes: typing.Optional[jsii.Number] = None,
        connection_type: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        owner_arn: typing.Optional[str] = None,
        repositories: typing.Optional[
            typing.Union[
                aws_cdk.core.IResolvable,
                typing.List[
                    typing.Union["RepositoryProperty", aws_cdk.core.IResolvable]
                ],
            ]
        ] = None,
        subnet_id: typing.Optional[str] = None,
        tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        """Create a new ``AWS::Cloud9::EnvironmentEC2``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param instance_type: ``AWS::Cloud9::EnvironmentEC2.InstanceType``.
        :param automatic_stop_time_minutes: ``AWS::Cloud9::EnvironmentEC2.AutomaticStopTimeMinutes``.
        :param connection_type: ``AWS::Cloud9::EnvironmentEC2.ConnectionType``.
        :param description: ``AWS::Cloud9::EnvironmentEC2.Description``.
        :param name: ``AWS::Cloud9::EnvironmentEC2.Name``.
        :param owner_arn: ``AWS::Cloud9::EnvironmentEC2.OwnerArn``.
        :param repositories: ``AWS::Cloud9::EnvironmentEC2.Repositories``.
        :param subnet_id: ``AWS::Cloud9::EnvironmentEC2.SubnetId``.
        :param tags: ``AWS::Cloud9::EnvironmentEC2.Tags``.
        """
        props = CfnEnvironmentEC2Props(
            instance_type=instance_type,
            automatic_stop_time_minutes=automatic_stop_time_minutes,
            connection_type=connection_type,
            description=description,
            name=name,
            owner_arn=owner_arn,
            repositories=repositories,
            subnet_id=subnet_id,
            tags=tags,
        )

        jsii.create(CfnEnvironmentEC2, self, [scope, id, props])

    @jsii.member(jsii_name="fromCloudFormation")
    @builtins.classmethod
    def from_cloud_formation(
        cls,
        scope: aws_cdk.core.Construct,
        id: str,
        resource_attributes: typing.Any,
        *,
        finder: aws_cdk.core.ICfnFinder,
    ) -> "CfnEnvironmentEC2":
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
    def tags(self) -> aws_cdk.core.TagManager:
        """``AWS::Cloud9::EnvironmentEC2.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloud9-environmentec2.html#cfn-cloud9-environmentec2-tags
        """
        return jsii.get(self, "tags")

    @builtins.property
    @jsii.member(jsii_name="instanceType")
    def instance_type(self) -> str:
        """``AWS::Cloud9::EnvironmentEC2.InstanceType``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloud9-environmentec2.html#cfn-cloud9-environmentec2-instancetype
        """
        return jsii.get(self, "instanceType")

    @instance_type.setter
    def instance_type(self, value: str) -> None:
        jsii.set(self, "instanceType", value)

    @builtins.property
    @jsii.member(jsii_name="automaticStopTimeMinutes")
    def automatic_stop_time_minutes(self) -> typing.Optional[jsii.Number]:
        """``AWS::Cloud9::EnvironmentEC2.AutomaticStopTimeMinutes``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloud9-environmentec2.html#cfn-cloud9-environmentec2-automaticstoptimeminutes
        """
        return jsii.get(self, "automaticStopTimeMinutes")

    @automatic_stop_time_minutes.setter
    def automatic_stop_time_minutes(self, value: typing.Optional[jsii.Number]) -> None:
        jsii.set(self, "automaticStopTimeMinutes", value)

    @builtins.property
    @jsii.member(jsii_name="connectionType")
    def connection_type(self) -> typing.Optional[str]:
        """``AWS::Cloud9::EnvironmentEC2.ConnectionType``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloud9-environmentec2.html#cfn-cloud9-environmentec2-connectiontype
        """
        return jsii.get(self, "connectionType")

    @connection_type.setter
    def connection_type(self, value: typing.Optional[str]) -> None:
        jsii.set(self, "connectionType", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[str]:
        """``AWS::Cloud9::EnvironmentEC2.Description``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloud9-environmentec2.html#cfn-cloud9-environmentec2-description
        """
        return jsii.get(self, "description")

    @description.setter
    def description(self, value: typing.Optional[str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[str]:
        """``AWS::Cloud9::EnvironmentEC2.Name``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloud9-environmentec2.html#cfn-cloud9-environmentec2-name
        """
        return jsii.get(self, "name")

    @name.setter
    def name(self, value: typing.Optional[str]) -> None:
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="ownerArn")
    def owner_arn(self) -> typing.Optional[str]:
        """``AWS::Cloud9::EnvironmentEC2.OwnerArn``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloud9-environmentec2.html#cfn-cloud9-environmentec2-ownerarn
        """
        return jsii.get(self, "ownerArn")

    @owner_arn.setter
    def owner_arn(self, value: typing.Optional[str]) -> None:
        jsii.set(self, "ownerArn", value)

    @builtins.property
    @jsii.member(jsii_name="repositories")
    def repositories(
        self,
    ) -> typing.Optional[
        typing.Union[
            aws_cdk.core.IResolvable,
            typing.List[typing.Union["RepositoryProperty", aws_cdk.core.IResolvable]],
        ]
    ]:
        """``AWS::Cloud9::EnvironmentEC2.Repositories``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloud9-environmentec2.html#cfn-cloud9-environmentec2-repositories
        """
        return jsii.get(self, "repositories")

    @repositories.setter
    def repositories(
        self,
        value: typing.Optional[
            typing.Union[
                aws_cdk.core.IResolvable,
                typing.List[
                    typing.Union["RepositoryProperty", aws_cdk.core.IResolvable]
                ],
            ]
        ],
    ) -> None:
        jsii.set(self, "repositories", value)

    @builtins.property
    @jsii.member(jsii_name="subnetId")
    def subnet_id(self) -> typing.Optional[str]:
        """``AWS::Cloud9::EnvironmentEC2.SubnetId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloud9-environmentec2.html#cfn-cloud9-environmentec2-subnetid
        """
        return jsii.get(self, "subnetId")

    @subnet_id.setter
    def subnet_id(self, value: typing.Optional[str]) -> None:
        jsii.set(self, "subnetId", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-cloud9.CfnEnvironmentEC2.RepositoryProperty",
        jsii_struct_bases=[],
        name_mapping={
            "path_component": "pathComponent",
            "repository_url": "repositoryUrl",
        },
    )
    class RepositoryProperty:
        def __init__(self, *, path_component: str, repository_url: str) -> None:
            """
            :param path_component: ``CfnEnvironmentEC2.RepositoryProperty.PathComponent``.
            :param repository_url: ``CfnEnvironmentEC2.RepositoryProperty.RepositoryUrl``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloud9-environmentec2-repository.html
            """
            self._values = {
                "path_component": path_component,
                "repository_url": repository_url,
            }

        @builtins.property
        def path_component(self) -> str:
            """``CfnEnvironmentEC2.RepositoryProperty.PathComponent``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloud9-environmentec2-repository.html#cfn-cloud9-environmentec2-repository-pathcomponent
            """
            return self._values.get("path_component")

        @builtins.property
        def repository_url(self) -> str:
            """``CfnEnvironmentEC2.RepositoryProperty.RepositoryUrl``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloud9-environmentec2-repository.html#cfn-cloud9-environmentec2-repository-repositoryurl
            """
            return self._values.get("repository_url")

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RepositoryProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-cloud9.CfnEnvironmentEC2Props",
    jsii_struct_bases=[],
    name_mapping={
        "instance_type": "instanceType",
        "automatic_stop_time_minutes": "automaticStopTimeMinutes",
        "connection_type": "connectionType",
        "description": "description",
        "name": "name",
        "owner_arn": "ownerArn",
        "repositories": "repositories",
        "subnet_id": "subnetId",
        "tags": "tags",
    },
)
class CfnEnvironmentEC2Props:
    def __init__(
        self,
        *,
        instance_type: str,
        automatic_stop_time_minutes: typing.Optional[jsii.Number] = None,
        connection_type: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        owner_arn: typing.Optional[str] = None,
        repositories: typing.Optional[
            typing.Union[
                aws_cdk.core.IResolvable,
                typing.List[
                    typing.Union[
                        "CfnEnvironmentEC2.RepositoryProperty", aws_cdk.core.IResolvable
                    ]
                ],
            ]
        ] = None,
        subnet_id: typing.Optional[str] = None,
        tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        """Properties for defining a ``AWS::Cloud9::EnvironmentEC2``.

        :param instance_type: ``AWS::Cloud9::EnvironmentEC2.InstanceType``.
        :param automatic_stop_time_minutes: ``AWS::Cloud9::EnvironmentEC2.AutomaticStopTimeMinutes``.
        :param connection_type: ``AWS::Cloud9::EnvironmentEC2.ConnectionType``.
        :param description: ``AWS::Cloud9::EnvironmentEC2.Description``.
        :param name: ``AWS::Cloud9::EnvironmentEC2.Name``.
        :param owner_arn: ``AWS::Cloud9::EnvironmentEC2.OwnerArn``.
        :param repositories: ``AWS::Cloud9::EnvironmentEC2.Repositories``.
        :param subnet_id: ``AWS::Cloud9::EnvironmentEC2.SubnetId``.
        :param tags: ``AWS::Cloud9::EnvironmentEC2.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloud9-environmentec2.html
        """
        self._values = {
            "instance_type": instance_type,
        }
        if automatic_stop_time_minutes is not None:
            self._values["automatic_stop_time_minutes"] = automatic_stop_time_minutes
        if connection_type is not None:
            self._values["connection_type"] = connection_type
        if description is not None:
            self._values["description"] = description
        if name is not None:
            self._values["name"] = name
        if owner_arn is not None:
            self._values["owner_arn"] = owner_arn
        if repositories is not None:
            self._values["repositories"] = repositories
        if subnet_id is not None:
            self._values["subnet_id"] = subnet_id
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def instance_type(self) -> str:
        """``AWS::Cloud9::EnvironmentEC2.InstanceType``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloud9-environmentec2.html#cfn-cloud9-environmentec2-instancetype
        """
        return self._values.get("instance_type")

    @builtins.property
    def automatic_stop_time_minutes(self) -> typing.Optional[jsii.Number]:
        """``AWS::Cloud9::EnvironmentEC2.AutomaticStopTimeMinutes``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloud9-environmentec2.html#cfn-cloud9-environmentec2-automaticstoptimeminutes
        """
        return self._values.get("automatic_stop_time_minutes")

    @builtins.property
    def connection_type(self) -> typing.Optional[str]:
        """``AWS::Cloud9::EnvironmentEC2.ConnectionType``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloud9-environmentec2.html#cfn-cloud9-environmentec2-connectiontype
        """
        return self._values.get("connection_type")

    @builtins.property
    def description(self) -> typing.Optional[str]:
        """``AWS::Cloud9::EnvironmentEC2.Description``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloud9-environmentec2.html#cfn-cloud9-environmentec2-description
        """
        return self._values.get("description")

    @builtins.property
    def name(self) -> typing.Optional[str]:
        """``AWS::Cloud9::EnvironmentEC2.Name``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloud9-environmentec2.html#cfn-cloud9-environmentec2-name
        """
        return self._values.get("name")

    @builtins.property
    def owner_arn(self) -> typing.Optional[str]:
        """``AWS::Cloud9::EnvironmentEC2.OwnerArn``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloud9-environmentec2.html#cfn-cloud9-environmentec2-ownerarn
        """
        return self._values.get("owner_arn")

    @builtins.property
    def repositories(
        self,
    ) -> typing.Optional[
        typing.Union[
            aws_cdk.core.IResolvable,
            typing.List[
                typing.Union[
                    "CfnEnvironmentEC2.RepositoryProperty", aws_cdk.core.IResolvable
                ]
            ],
        ]
    ]:
        """``AWS::Cloud9::EnvironmentEC2.Repositories``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloud9-environmentec2.html#cfn-cloud9-environmentec2-repositories
        """
        return self._values.get("repositories")

    @builtins.property
    def subnet_id(self) -> typing.Optional[str]:
        """``AWS::Cloud9::EnvironmentEC2.SubnetId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloud9-environmentec2.html#cfn-cloud9-environmentec2-subnetid
        """
        return self._values.get("subnet_id")

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        """``AWS::Cloud9::EnvironmentEC2.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloud9-environmentec2.html#cfn-cloud9-environmentec2-tags
        """
        return self._values.get("tags")

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEnvironmentEC2Props(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloneRepository(
    metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-cloud9.CloneRepository"
):
    """The class for different repository providers.

    stability
    :stability: experimental
    """

    @jsii.member(jsii_name="fromCodeCommit")
    @builtins.classmethod
    def from_code_commit(
        cls, repository: aws_cdk.aws_codecommit.IRepository, path: str
    ) -> "CloneRepository":
        """import repository to cloud9 environment from AWS CodeCommit.

        :param repository: the codecommit repository to clone from.
        :param path: the target path in cloud9 environment.

        stability
        :stability: experimental
        """
        return jsii.sinvoke(cls, "fromCodeCommit", [repository, path])

    @builtins.property
    @jsii.member(jsii_name="pathComponent")
    def path_component(self) -> str:
        """
        stability
        :stability: experimental
        """
        return jsii.get(self, "pathComponent")

    @builtins.property
    @jsii.member(jsii_name="repositoryUrl")
    def repository_url(self) -> str:
        """
        stability
        :stability: experimental
        """
        return jsii.get(self, "repositoryUrl")


@jsii.data_type(
    jsii_type="@aws-cdk/aws-cloud9.Ec2EnvironmentProps",
    jsii_struct_bases=[],
    name_mapping={
        "vpc": "vpc",
        "cloned_repositories": "clonedRepositories",
        "description": "description",
        "ec2_environment_name": "ec2EnvironmentName",
        "instance_type": "instanceType",
        "subnet_selection": "subnetSelection",
    },
)
class Ec2EnvironmentProps:
    def __init__(
        self,
        *,
        vpc: aws_cdk.aws_ec2.IVpc,
        cloned_repositories: typing.Optional[typing.List["CloneRepository"]] = None,
        description: typing.Optional[str] = None,
        ec2_environment_name: typing.Optional[str] = None,
        instance_type: typing.Optional[aws_cdk.aws_ec2.InstanceType] = None,
        subnet_selection: typing.Optional[aws_cdk.aws_ec2.SubnetSelection] = None,
    ) -> None:
        """Properties for Ec2Environment.

        :param vpc: The VPC that AWS Cloud9 will use to communicate with the Amazon Elastic Compute Cloud (Amazon EC2) instance.
        :param cloned_repositories: The AWS CodeCommit repository to be cloned. Default: - do not clone any repository
        :param description: Description of the environment. Default: - no description
        :param ec2_environment_name: Name of the environment. Default: - automatically generated name
        :param instance_type: The type of instance to connect to the environment. Default: - t2.micro
        :param subnet_selection: The subnetSelection of the VPC that AWS Cloud9 will use to communicate with the Amazon EC2 instance. Default: - all public subnets of the VPC are selected.

        stability
        :stability: experimental
        """
        if isinstance(subnet_selection, dict):
            subnet_selection = aws_cdk.aws_ec2.SubnetSelection(**subnet_selection)
        self._values = {
            "vpc": vpc,
        }
        if cloned_repositories is not None:
            self._values["cloned_repositories"] = cloned_repositories
        if description is not None:
            self._values["description"] = description
        if ec2_environment_name is not None:
            self._values["ec2_environment_name"] = ec2_environment_name
        if instance_type is not None:
            self._values["instance_type"] = instance_type
        if subnet_selection is not None:
            self._values["subnet_selection"] = subnet_selection

    @builtins.property
    def vpc(self) -> aws_cdk.aws_ec2.IVpc:
        """The VPC that AWS Cloud9 will use to communicate with the Amazon Elastic Compute Cloud (Amazon EC2) instance.

        stability
        :stability: experimental
        """
        return self._values.get("vpc")

    @builtins.property
    def cloned_repositories(self) -> typing.Optional[typing.List["CloneRepository"]]:
        """The AWS CodeCommit repository to be cloned.

        default
        :default: - do not clone any repository

        stability
        :stability: experimental
        """
        return self._values.get("cloned_repositories")

    @builtins.property
    def description(self) -> typing.Optional[str]:
        """Description of the environment.

        default
        :default: - no description

        stability
        :stability: experimental
        """
        return self._values.get("description")

    @builtins.property
    def ec2_environment_name(self) -> typing.Optional[str]:
        """Name of the environment.

        default
        :default: - automatically generated name

        stability
        :stability: experimental
        """
        return self._values.get("ec2_environment_name")

    @builtins.property
    def instance_type(self) -> typing.Optional[aws_cdk.aws_ec2.InstanceType]:
        """The type of instance to connect to the environment.

        default
        :default: - t2.micro

        stability
        :stability: experimental
        """
        return self._values.get("instance_type")

    @builtins.property
    def subnet_selection(self) -> typing.Optional[aws_cdk.aws_ec2.SubnetSelection]:
        """The subnetSelection of the VPC that AWS Cloud9 will use to communicate with the Amazon EC2 instance.

        default
        :default: - all public subnets of the VPC are selected.

        stability
        :stability: experimental
        """
        return self._values.get("subnet_selection")

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Ec2EnvironmentProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="@aws-cdk/aws-cloud9.IEc2Environment")
class IEc2Environment(aws_cdk.core.IResource, jsii.compat.Protocol):
    """A Cloud9 Environment.

    stability
    :stability: experimental
    """

    @builtins.staticmethod
    def __jsii_proxy_class__():
        return _IEc2EnvironmentProxy

    @builtins.property
    @jsii.member(jsii_name="ec2EnvironmentArn")
    def ec2_environment_arn(self) -> str:
        """The arn of the EnvironmentEc2.

        stability
        :stability: experimental
        attribute:
        :attribute:: environmentE2Arn
        """
        ...

    @builtins.property
    @jsii.member(jsii_name="ec2EnvironmentName")
    def ec2_environment_name(self) -> str:
        """The name of the EnvironmentEc2.

        stability
        :stability: experimental
        attribute:
        :attribute:: environmentEc2Name
        """
        ...


class _IEc2EnvironmentProxy(jsii.proxy_for(aws_cdk.core.IResource)):
    """A Cloud9 Environment.

    stability
    :stability: experimental
    """

    __jsii_type__ = "@aws-cdk/aws-cloud9.IEc2Environment"

    @builtins.property
    @jsii.member(jsii_name="ec2EnvironmentArn")
    def ec2_environment_arn(self) -> str:
        """The arn of the EnvironmentEc2.

        stability
        :stability: experimental
        attribute:
        :attribute:: environmentE2Arn
        """
        return jsii.get(self, "ec2EnvironmentArn")

    @builtins.property
    @jsii.member(jsii_name="ec2EnvironmentName")
    def ec2_environment_name(self) -> str:
        """The name of the EnvironmentEc2.

        stability
        :stability: experimental
        attribute:
        :attribute:: environmentEc2Name
        """
        return jsii.get(self, "ec2EnvironmentName")


@jsii.implements(IEc2Environment)
class Ec2Environment(
    aws_cdk.core.Resource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-cloud9.Ec2Environment",
):
    """A Cloud9 Environment with Amazon EC2.

    stability
    :stability: experimental
    resource:
    :resource:: AWS::Cloud9::EnvironmentEC2
    """

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: str,
        *,
        vpc: aws_cdk.aws_ec2.IVpc,
        cloned_repositories: typing.Optional[typing.List["CloneRepository"]] = None,
        description: typing.Optional[str] = None,
        ec2_environment_name: typing.Optional[str] = None,
        instance_type: typing.Optional[aws_cdk.aws_ec2.InstanceType] = None,
        subnet_selection: typing.Optional[aws_cdk.aws_ec2.SubnetSelection] = None,
    ) -> None:
        """
        :param scope: -
        :param id: -
        :param vpc: The VPC that AWS Cloud9 will use to communicate with the Amazon Elastic Compute Cloud (Amazon EC2) instance.
        :param cloned_repositories: The AWS CodeCommit repository to be cloned. Default: - do not clone any repository
        :param description: Description of the environment. Default: - no description
        :param ec2_environment_name: Name of the environment. Default: - automatically generated name
        :param instance_type: The type of instance to connect to the environment. Default: - t2.micro
        :param subnet_selection: The subnetSelection of the VPC that AWS Cloud9 will use to communicate with the Amazon EC2 instance. Default: - all public subnets of the VPC are selected.

        stability
        :stability: experimental
        """
        props = Ec2EnvironmentProps(
            vpc=vpc,
            cloned_repositories=cloned_repositories,
            description=description,
            ec2_environment_name=ec2_environment_name,
            instance_type=instance_type,
            subnet_selection=subnet_selection,
        )

        jsii.create(Ec2Environment, self, [scope, id, props])

    @jsii.member(jsii_name="fromEc2EnvironmentName")
    @builtins.classmethod
    def from_ec2_environment_name(
        cls, scope: aws_cdk.core.Construct, id: str, ec2_environment_name: str
    ) -> "IEc2Environment":
        """import from EnvironmentEc2Name.

        :param scope: -
        :param id: -
        :param ec2_environment_name: -

        stability
        :stability: experimental
        """
        return jsii.sinvoke(
            cls, "fromEc2EnvironmentName", [scope, id, ec2_environment_name]
        )

    @builtins.property
    @jsii.member(jsii_name="ec2EnvironmentArn")
    def ec2_environment_arn(self) -> str:
        """The environment ARN of this Cloud9 environment.

        stability
        :stability: experimental
        attribute:
        :attribute:: true
        """
        return jsii.get(self, "ec2EnvironmentArn")

    @builtins.property
    @jsii.member(jsii_name="ec2EnvironmentName")
    def ec2_environment_name(self) -> str:
        """The environment name of this Cloud9 environment.

        stability
        :stability: experimental
        attribute:
        :attribute:: true
        """
        return jsii.get(self, "ec2EnvironmentName")

    @builtins.property
    @jsii.member(jsii_name="environmentId")
    def environment_id(self) -> str:
        """The environment ID of this Cloud9 environment.

        stability
        :stability: experimental
        """
        return jsii.get(self, "environmentId")

    @builtins.property
    @jsii.member(jsii_name="ideUrl")
    def ide_url(self) -> str:
        """The complete IDE URL of this Cloud9 environment.

        stability
        :stability: experimental
        """
        return jsii.get(self, "ideUrl")

    @builtins.property
    @jsii.member(jsii_name="vpc")
    def vpc(self) -> aws_cdk.aws_ec2.IVpc:
        """VPC ID.

        stability
        :stability: experimental
        """
        return jsii.get(self, "vpc")


__all__ = [
    "CfnEnvironmentEC2",
    "CfnEnvironmentEC2Props",
    "CloneRepository",
    "Ec2Environment",
    "Ec2EnvironmentProps",
    "IEc2Environment",
]

publication.publish()
