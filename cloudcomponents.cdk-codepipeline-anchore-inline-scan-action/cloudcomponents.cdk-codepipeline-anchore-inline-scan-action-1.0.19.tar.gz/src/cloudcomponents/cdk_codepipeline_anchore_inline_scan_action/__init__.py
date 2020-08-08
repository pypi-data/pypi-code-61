"""
[![cloudcomponents Logo](https://raw.githubusercontent.com/cloudcomponents/cdk-constructs/master/logo.png)](https://github.com/cloudcomponents/cdk-constructs)

# @cloudcomponents/cdk-codepipeline-anchore-inline-scan-action

[![Build Status](https://travis-ci.org/cloudcomponents/cdk-constructs.svg?branch=master)](https://travis-ci.org/cloudcomponents/cdk-constructs)
[![cdkdx](https://img.shields.io/badge/buildtool-cdkdx-blue.svg)](https://github.com/hupe1980/cdkdx)
[![typescript](https://img.shields.io/badge/jsii-typescript-blueviolet.svg)](https://www.npmjs.com/package/@cloudcomponents/cdk-codepipeline-anchore-inline-scan-action)
[![python](https://img.shields.io/badge/jsii-python-blueviolet.svg)](https://pypi.org/project/cloudcomponents.cdk-codepipeline-anchore-inline-scan-action/)

> CodePipeline action to integrate [Anchore Engine](https://docs.anchore.com/current/) into your pipeline

## Install

TypeScript/JavaScript:

```bash
npm i @cloudcomponents/cdk-codepipeline-anchore-inline-scan-action
```

Python:

```bash
pip install cloudcomponents.cdk-codepipeline-anchore-inline-scan-action
```

## How to use

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
from aws_cdk.core import Construct, Stack, StackProps
from aws_cdk.aws_codecommit import Repository
from aws_cdk.aws_codepipeline import Pipeline, Artifact
from aws_cdk.aws_codepipeline_actions import CodeCommitSourceAction
from cloudcomponents.cdk_codepipeline_dockerfile_linter_action import CodePipelineDockerfileLinterAction
from cloudcomponents.cdk_codepipeline_anchore_inline_scan_action import CodePipelineAnchoreInlineScanAction
class ContainerAuditStack(Stack):
    def __init__(self, scope, id, *, description=None, env=None, stackName=None, tags=None, synthesizer=None, terminationProtection=None):
        super().__init__(scope, id, description=description, env=env, stackName=stackName, tags=tags, synthesizer=synthesizer, terminationProtection=terminationProtection)

        repository = Repository(self, "Repository",
            repository_name="container-audit-repository"
        )

        source_artifact = Artifact()

        source_action = CodeCommitSourceAction(
            action_name="CodeCommit",
            repository=repository,
            output=source_artifact,
            branch="master"
        )

        linter_action = CodePipelineDockerfileLinterAction(
            action_name="Linter",
            input=source_artifact
        )

        vuln_scan_action = CodePipelineAnchoreInlineScanAction(
            action_name="VulnScan",
            input=source_artifact
        )

        Pipeline(self, "Pipeline",
            pipeline_name="container-audit-pipeline",
            stages=[StageProps(
                stage_name="Source",
                actions=[source_action]
            ), StageProps(
                stage_name="Audit",
                actions=[linter_action, vuln_scan_action]
            )
            ]
        )
```

## API Reference

See [API.md](https://github.com/cloudcomponents/cdk-constructs/tree/master/packages/cdk-codepipeline-anchore-inline-scan-action/API.md).

## Example

See more complete [examples](https://github.com/cloudcomponents/cdk-constructs/tree/master/examples).

## License

[MIT](https://github.com/cloudcomponents/cdk-constructs/tree/master/packages/cdk-codepipeline-anchore-inline-scan-action/LICENSE)
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

import aws_cdk.aws_codebuild
import aws_cdk.aws_codepipeline
import aws_cdk.aws_codepipeline_actions
import aws_cdk.aws_iam
import aws_cdk.aws_s3
import aws_cdk.core


class CodePipelineAnchoreInlineScanAction(
    aws_cdk.aws_codepipeline_actions.Action,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cloudcomponents/cdk-codepipeline-anchore-inline-scan-action.CodePipelineAnchoreInlineScanAction",
):
    def __init__(
        self,
        *,
        input: aws_cdk.aws_codepipeline.Artifact,
        compute_type: typing.Optional[aws_cdk.aws_codebuild.ComputeType] = None,
        policy_bundle_path: typing.Optional[str] = None,
        timeout: typing.Optional[jsii.Number] = None,
        version: typing.Optional[str] = None,
        role: typing.Optional[aws_cdk.aws_iam.IRole] = None,
        action_name: str,
        run_order: typing.Optional[jsii.Number] = None,
        variables_namespace: typing.Optional[str] = None,
    ) -> None:
        """
        :param input: The source to use as input for this action.
        :param compute_type: The type of compute to use for backup the repositories. See the {@link ComputeType} enum for the possible values. Default: taken from {@link LinuxBuildImage.STANDARD_4_0#defaultComputeType}
        :param policy_bundle_path: Path to local Anchore policy bundle. Default: ./policy_bundle.json
        :param timeout: Specify timeout for image scanning in seconds. Default: 300
        :param version: Version of anchore ci-tools. Default: v0.7.2
        :param role: The Role in which context's this Action will be executing in. The Pipeline's Role will assume this Role (the required permissions for that will be granted automatically) right before executing this Action. This Action will be passed into your {@link IAction.bind} method in the {@link ActionBindOptions.role} property. Default: a new Role will be generated
        :param action_name: The physical, human-readable name of the Action. Note that Action names must be unique within a single Stage.
        :param run_order: The runOrder property for this Action. RunOrder determines the relative order in which multiple Actions in the same Stage execute. Default: 1
        :param variables_namespace: The name of the namespace to use for variables emitted by this action. Default: - a name will be generated, based on the stage and action names, if any of the action's variables were referenced - otherwise, no namespace will be set
        """
        props = CodePipelineAnchoreInlineScanActionProps(
            input=input,
            compute_type=compute_type,
            policy_bundle_path=policy_bundle_path,
            timeout=timeout,
            version=version,
            role=role,
            action_name=action_name,
            run_order=run_order,
            variables_namespace=variables_namespace,
        )

        jsii.create(CodePipelineAnchoreInlineScanAction, self, [props])

    @jsii.member(jsii_name="bound")
    def _bound(
        self,
        scope: aws_cdk.core.Construct,
        _stage: aws_cdk.aws_codepipeline.IStage,
        *,
        bucket: aws_cdk.aws_s3.IBucket,
        role: aws_cdk.aws_iam.IRole,
    ) -> aws_cdk.aws_codepipeline.ActionConfig:
        """The method called when an Action is attached to a Pipeline.

        This method is guaranteed to be called only once for each Action instance.

        :param scope: -
        :param _stage: -
        :param bucket: 
        :param role: 
        """
        options = aws_cdk.aws_codepipeline.ActionBindOptions(bucket=bucket, role=role)

        return jsii.invoke(self, "bound", [scope, _stage, options])


@jsii.data_type(
    jsii_type="@cloudcomponents/cdk-codepipeline-anchore-inline-scan-action.CodePipelineAnchoreInlineScanActionProps",
    jsii_struct_bases=[aws_cdk.aws_codepipeline.CommonAwsActionProps],
    name_mapping={
        "action_name": "actionName",
        "run_order": "runOrder",
        "variables_namespace": "variablesNamespace",
        "role": "role",
        "input": "input",
        "compute_type": "computeType",
        "policy_bundle_path": "policyBundlePath",
        "timeout": "timeout",
        "version": "version",
    },
)
class CodePipelineAnchoreInlineScanActionProps(
    aws_cdk.aws_codepipeline.CommonAwsActionProps
):
    def __init__(
        self,
        *,
        action_name: str,
        run_order: typing.Optional[jsii.Number] = None,
        variables_namespace: typing.Optional[str] = None,
        role: typing.Optional[aws_cdk.aws_iam.IRole] = None,
        input: aws_cdk.aws_codepipeline.Artifact,
        compute_type: typing.Optional[aws_cdk.aws_codebuild.ComputeType] = None,
        policy_bundle_path: typing.Optional[str] = None,
        timeout: typing.Optional[jsii.Number] = None,
        version: typing.Optional[str] = None,
    ) -> None:
        """
        :param action_name: The physical, human-readable name of the Action. Note that Action names must be unique within a single Stage.
        :param run_order: The runOrder property for this Action. RunOrder determines the relative order in which multiple Actions in the same Stage execute. Default: 1
        :param variables_namespace: The name of the namespace to use for variables emitted by this action. Default: - a name will be generated, based on the stage and action names, if any of the action's variables were referenced - otherwise, no namespace will be set
        :param role: The Role in which context's this Action will be executing in. The Pipeline's Role will assume this Role (the required permissions for that will be granted automatically) right before executing this Action. This Action will be passed into your {@link IAction.bind} method in the {@link ActionBindOptions.role} property. Default: a new Role will be generated
        :param input: The source to use as input for this action.
        :param compute_type: The type of compute to use for backup the repositories. See the {@link ComputeType} enum for the possible values. Default: taken from {@link LinuxBuildImage.STANDARD_4_0#defaultComputeType}
        :param policy_bundle_path: Path to local Anchore policy bundle. Default: ./policy_bundle.json
        :param timeout: Specify timeout for image scanning in seconds. Default: 300
        :param version: Version of anchore ci-tools. Default: v0.7.2
        """
        self._values = {
            "action_name": action_name,
            "input": input,
        }
        if run_order is not None:
            self._values["run_order"] = run_order
        if variables_namespace is not None:
            self._values["variables_namespace"] = variables_namespace
        if role is not None:
            self._values["role"] = role
        if compute_type is not None:
            self._values["compute_type"] = compute_type
        if policy_bundle_path is not None:
            self._values["policy_bundle_path"] = policy_bundle_path
        if timeout is not None:
            self._values["timeout"] = timeout
        if version is not None:
            self._values["version"] = version

    @builtins.property
    def action_name(self) -> str:
        """The physical, human-readable name of the Action.

        Note that Action names must be unique within a single Stage.
        """
        return self._values.get("action_name")

    @builtins.property
    def run_order(self) -> typing.Optional[jsii.Number]:
        """The runOrder property for this Action.

        RunOrder determines the relative order in which multiple Actions in the same Stage execute.

        default
        :default: 1

        see
        :see: https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html
        """
        return self._values.get("run_order")

    @builtins.property
    def variables_namespace(self) -> typing.Optional[str]:
        """The name of the namespace to use for variables emitted by this action.

        default
        :default:

        - a name will be generated, based on the stage and action names,
          if any of the action's variables were referenced - otherwise,
          no namespace will be set
        """
        return self._values.get("variables_namespace")

    @builtins.property
    def role(self) -> typing.Optional[aws_cdk.aws_iam.IRole]:
        """The Role in which context's this Action will be executing in.

        The Pipeline's Role will assume this Role
        (the required permissions for that will be granted automatically)
        right before executing this Action.
        This Action will be passed into your {@link IAction.bind}
        method in the {@link ActionBindOptions.role} property.

        default
        :default: a new Role will be generated
        """
        return self._values.get("role")

    @builtins.property
    def input(self) -> aws_cdk.aws_codepipeline.Artifact:
        """The source to use as input for this action."""
        return self._values.get("input")

    @builtins.property
    def compute_type(self) -> typing.Optional[aws_cdk.aws_codebuild.ComputeType]:
        """The type of compute to use for backup the repositories.

        See the {@link ComputeType} enum for the possible values.

        default
        :default: taken from {@link LinuxBuildImage.STANDARD_4_0#defaultComputeType}
        """
        return self._values.get("compute_type")

    @builtins.property
    def policy_bundle_path(self) -> typing.Optional[str]:
        """Path to local Anchore policy bundle.

        default
        :default: ./policy_bundle.json
        """
        return self._values.get("policy_bundle_path")

    @builtins.property
    def timeout(self) -> typing.Optional[jsii.Number]:
        """Specify timeout for image scanning in seconds.

        default
        :default: 300
        """
        return self._values.get("timeout")

    @builtins.property
    def version(self) -> typing.Optional[str]:
        """Version of anchore ci-tools.

        default
        :default: v0.7.2
        """
        return self._values.get("version")

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodePipelineAnchoreInlineScanActionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CodePipelineAnchoreInlineScanAction",
    "CodePipelineAnchoreInlineScanActionProps",
]

publication.publish()
