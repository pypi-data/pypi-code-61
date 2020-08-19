import click
import os
import yaml


def read_or_build_config_file():
    default_path = os.path.expanduser("~/.kfpclient/config.yaml")
    config_path = os.environ.get("KFPCLIENT_CONFIG", default_path)

    try:
        with open(config_path) as file:
            return yaml.full_load(file)
    except:
        yaml_dict = {}
        build_or_not = input(f'There is no config file in {default_path}. Would you like a little help to build '
                             f'one?(y/n)')
        if build_or_not == 'y':
            host = input('Enter with the Kubeflow host name: ')
            namespace = input('Enter with your namespace: ')
            yaml_dict['host'] = host
            yaml_dict['namespace'] = namespace
            with open(config_path, 'w') as config:
                yaml.dump(yaml_dict, config)
            return read_or_build_config_file()
        else:
            click.echo(f'Ok, but for using kfpctl you will need a config file located n {default_path}.')
