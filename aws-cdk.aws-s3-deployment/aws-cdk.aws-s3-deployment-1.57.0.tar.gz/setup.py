import json
import setuptools

kwargs = json.loads(
    """
{
    "name": "aws-cdk.aws-s3-deployment",
    "version": "1.57.0",
    "description": "Constructs for deploying contents to S3 buckets",
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
        "aws_cdk.aws_s3_deployment",
        "aws_cdk.aws_s3_deployment._jsii"
    ],
    "package_data": {
        "aws_cdk.aws_s3_deployment._jsii": [
            "aws-s3-deployment@1.57.0.jsii.tgz"
        ],
        "aws_cdk.aws_s3_deployment": [
            "py.typed"
        ]
    },
    "python_requires": ">=3.6",
    "install_requires": [
        "jsii>=1.9.0, <2.0.0",
        "publication>=0.0.3",
        "aws-cdk.aws-cloudfront==1.57.0",
        "aws-cdk.aws-iam==1.57.0",
        "aws-cdk.aws-lambda==1.57.0",
        "aws-cdk.aws-s3==1.57.0",
        "aws-cdk.aws-s3-assets==1.57.0",
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
