import json
import setuptools

kwargs = json.loads(
    """
{
    "name": "aws-cdk.aws-config",
    "version": "1.57.0",
    "description": "The CDK Construct Library for AWS::Config",
    "license": "Apache-2.0",
    "url": "https://github.com/aws/aws-cdk",
    "long_description_content_type": "text/markdown",
    "author": "Amazon Web Services",
    "project_urls": {
        "Source": "https://github.com/aws/aws-cdk.git"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "aws_cdk.aws_config",
        "aws_cdk.aws_config._jsii"
    ],
    "package_data": {
        "aws_cdk.aws_config._jsii": [
            "aws-config@1.57.0.jsii.tgz"
        ],
        "aws_cdk.aws_config": [
            "py.typed"
        ]
    },
    "python_requires": ">=3.6",
    "install_requires": [
        "jsii>=1.9.0, <2.0.0",
        "publication>=0.0.3",
        "aws-cdk.aws-events==1.57.0",
        "aws-cdk.aws-iam==1.57.0",
        "aws-cdk.aws-lambda==1.57.0",
        "aws-cdk.aws-sns==1.57.0",
        "aws-cdk.core==1.57.0",
        "constructs>=3.0.2, <4.0.0"
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
        "Development Status :: 4 - Beta",
        "License :: OSI Approved"
    ]
}
"""
)

with open("README.md") as fp:
    kwargs["long_description"] = fp.read()


setuptools.setup(**kwargs)
