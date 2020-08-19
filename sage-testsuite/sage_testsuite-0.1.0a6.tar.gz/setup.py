# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fate_testsuite']

package_data = \
{'': ['*']}

install_requires = \
['click>=7.1.2,<8.0.0',
 'loguru>=0.5.1,<0.6.0',
 'prettytable>=0.7.2,<0.8.0',
 'requests>=2.24.0,<3.0.0',
 'requests_toolbelt>=0.9.1,<0.10.0',
 'ruamel.yaml>=0.16.10,<0.17.0',
 'sshtunnel>=0.1.5,<0.2.0']

entry_points = \
{'console_scripts': ['fate_testsuite = fate_testsuite.cli:cli']}

setup_kwargs = {
    'name': 'sage-testsuite',
    'version': '0.1.0a6',
    'description': 'testsuite for FATE',
    'long_description': 'testsuite\n==============\n\nA useful script to running FATE\'s testsuites.\n\nquick start\n-----------\n\n1. (optional) create virtual env\n\n   .. code-block:: bash\n\n      python -m venv venv\n      source venv/bin/activate\n\n\n2. install fate_testsuite\n\n   .. code-block:: bash\n\n      pip install fate_testsuite\n      fate_testsuite --help\n\n\n3. new and edit the testsuite_config.yaml\n\n   .. code-block:: bash\n\n      # create a testsuite_config.yaml in current dir\n      testsuite config new\n      # edit priority config file with system default editor\n      # filling some field according to comments\n      fate_testsuite config edit\n\n\n4. run some testsuites\n\n   .. code-block:: bash\n\n      fate_testsuite suite -i <path contains *testsuite.json>\n\n5. useful logs or exception will be saved to logs dir with namespace showed in last step\n\n\ntestsuite_config.yaml examples\n------------------------------\n\n\n1. no need ssh tunnel:\n\n   - 9999, service: service_a\n   - 10000, service: service_b\n\n   and both service_a, service_b can be requested directly:\n\n   .. code-block:: yaml\n\n      work_mode: 1 # 0 for standalone, 1 for cluster\n      data_base_dir: <path_to_data>\n      parties:\n        guest: [10000]\n        host: [9999, 10000]\n        arbiter: [9999]\n      services:\n        - flow_services:\n          - {address: service_a, parties: [9999]}\n            {address: service_b, parties: [10000]}\n\n2. need ssh tunnel:\n\n   - 9999, service: service_a\n   - 10000, service: service_b\n\n   service_a, can be requested directly while service_b don\'t,\n   but you can request service_b in other node, say B:\n\n   .. code-block:: yaml\n\n      work_mode: 0 # 0 for standalone, 1 for cluster\n      data_base_dir: <path_to_data>\n      parties:\n        guest: [10000]\n        host: [9999, 10000]\n        arbiter: [9999]\n      services:\n        - flow_services:\n          - {address: service_a, parties: [9999]}\n        - flow_services:\n          - {address: service_b, parties: [10000]}\n          ssh_tunnel: # optional\n          enable: true\n          ssh_address: <ssh_ip_to_B>:<ssh_port_to_B>\n          ssh_username: <ssh_username_to B>\n          ssh_password: # optional\n          ssh_priv_key: "~/.ssh/id_rsa"\n\n\ncommand options\n---------------\n\n1. exclude:\n\n   .. code-block:: bash\n\n      testsuite suite -i <path1 contains *testsuite.json> -e <path2 to exclude> -e <path3 to exclude> ...\n\n   will run testsuites in `path1` but not in `path2` and `path3`\n\n2. replace:\n\n   .. code-block:: bash\n\n      testsuite suite -i <path1 contains *testsuite.json> -r \'{"maxIter": 5}\'\n\n   will find all key-value pair with key "maxIter" in `data conf` or `conf` or `dsl` and replace the value with 5\n\n3. glob:\n\n   .. code-block:: bash\n\n      testsuite suite -i <path1 contains *testsuite.json> -g "hetero*"\n\n   will run testsuites in sub directory start with `hetero` of `path1`',
    'author': 'FederatedAI',
    'author_email': 'contact@FedAI.org',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://fate.fedai.org/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
