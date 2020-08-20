# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['aurora_term']

package_data = \
{'': ['*']}

install_requires = \
['boto3>=1.10,<2.0', 'docopt>=0.6.2,<0.7.0']

entry_points = \
{'console_scripts': ['aurora-term = aurora_term.__main__:main']}

setup_kwargs = {
    'name': 'aurora-term',
    'version': '0.1.0',
    'description': 'AWS Aurora Serverless interactive terminal',
    'long_description': 'aurora-term\n===========\n\nAWS Aurora Serverless interactive terminal.\n\nIntroduction\n------------\n\nThe **aurora-term** app allows you to run SQL statements against `Aurora Serverless`_ databases without establishing a persistent connection, this is easily achieved thanks to the `Data-API`_.\n\nBesides the non-persistent connection it works just as any other interactive terminal like `mysql-cli`_ and `psql`_.\n\nRequirements\n------------\n\n- Python 3 and Pip.\n- An AWS IAM user `authorized`_ to access the Data API (with the *AmazonRDSDataFullAccess* policy for example).\n- Access key and secret access key properly configured for the same user (it can be done using the `aws-cli`_).\n\nInstallation\n------------\n\nThe easiest and recommended way to install it is using Pip. ::\n\n  pip install aurora-term\n\nUsage\n-----\n\nJust specify the database cluster ARN, the secret manager ARN and the database name. ::\n\n  aurora-term --cluster="arn:aws:rds:..." --secret="arn:aws:secretsmanager:..." mydb\n\n**TIP:**\n\nThere are a few environment variables that might come in handy, you can set them to avoid the need to pass all the credentials when starting **aurora-term**.\n\n- **AWS_PROFILE** Profile to be used.\n- **RDS_CLUSTER_ARN** Aurora cluster ARN.\n- **RDS_SECRET_ARN** Secret manager ARN.\n- **RDS_DB_NAME** Database name.\n\ne.g. ::\n\n  export RDS_CLUSTER_ARN="arn:aws:rds:..."\n  export RDS_SECRET_ARN="arn:aws:secretsmanager:..."\n\n  aurora-term mydb\n\nThe interactive terminal looks like as follow. ::\n\n  aurora-term (0.1.0)\n  Type "help" or "?" for help.\n\n  mydb=#\n\nFor more usage details. ::\n\n  aurora-term -h\n\n\n.. _Aurora Serverless: https://aws.amazon.com/rds/aurora/\n.. _Data-API: https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/data-api.html\n.. _mysql-cli: https://dev.mysql.com/doc/refman/5.5/en/mysql.html\n.. _psql: https://www.postgresql.org/docs/current/app-psql.html\n.. _authorized: https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html\n.. _aws-cli: https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html\n',
    'author': 'Juliano Fernandes',
    'author_email': 'julianofernandes@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/julianolf/aurora-term',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
