from setuptools import setup, find_namespace_packages


setup(
    name='aws-cdk.zip-asset-code',
    version='1.0.1',

    description='AWS CDK extension for aws-cdk.aws-lambda',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',

    packages=find_namespace_packages(include='aws-cdk/*'),

    python_requires='>=3.8',
    install_requires=[
        'aws-cdk.aws-lambda'
    ]
)
