import json
import setuptools

kwargs = json.loads(
    """
{
    "name": "cloudcomponents.cdk-developer-tools-notifications",
    "version": "1.0.29",
    "description": "#slack / msteams / email notifications for developer tools: CodeCommit, CodeBuild, CodeDeploy, CodePipeline",
    "license": "MIT",
    "url": "https://github.com/cloudcomponents/cdk-constructs",
    "long_description_content_type": "text/markdown",
    "author": "hupe1980",
    "project_urls": {
        "Source": "https://github.com/cloudcomponents/cdk-constructs.git"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "cloudcomponents.cdk_developer_tools_notifications",
        "cloudcomponents.cdk_developer_tools_notifications._jsii"
    ],
    "package_data": {
        "cloudcomponents.cdk_developer_tools_notifications._jsii": [
            "cdk-developer-tools-notifications@1.0.29.jsii.tgz"
        ],
        "cloudcomponents.cdk_developer_tools_notifications": [
            "py.typed"
        ]
    },
    "python_requires": ">=3.6",
    "install_requires": [
        "jsii>=1.10.0, <2.0.0",
        "publication>=0.0.3",
        "aws-cdk.aws-codebuild>=1.57.0, <2.0.0",
        "aws-cdk.aws-codecommit>=1.57.0, <2.0.0",
        "aws-cdk.aws-codedeploy>=1.57.0, <2.0.0",
        "aws-cdk.aws-codepipeline>=1.57.0, <2.0.0",
        "aws-cdk.aws-codestarnotifications>=1.57.0, <2.0.0",
        "aws-cdk.aws-iam>=1.57.0, <2.0.0",
        "aws-cdk.aws-lambda>=1.57.0, <2.0.0",
        "aws-cdk.aws-lambda-event-sources>=1.57.0, <2.0.0",
        "aws-cdk.aws-sns>=1.57.0, <2.0.0",
        "aws-cdk.core>=1.57.0, <2.0.0",
        "cloudcomponents.cdk-chatops>=1.0.27, <2.0.0"
    ],
    "classifiers": [
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Typing :: Typed",
        "License :: OSI Approved"
    ]
}
"""
)

with open("README.md") as fp:
    kwargs["long_description"] = fp.read()


setuptools.setup(**kwargs)
