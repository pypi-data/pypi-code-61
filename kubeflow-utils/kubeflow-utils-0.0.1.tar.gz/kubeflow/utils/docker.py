import base64
import json
from pathlib import Path


class Docker:
    def login(self, registry, username, password):
        config = Docker.__build_docker_config(registry, username, password)
        Docker.__save_docker_config(config)

    @staticmethod
    def __encode(string):
        encoded = base64.b64encode(string.encode('UTF-8'))
        return encoded.decode('UTF-8')

    @staticmethod
    def __generate_auth_string(username, password):
        return Docker.__encode(username + ':' + password)

    @staticmethod
    def __build_docker_config(registry, username, password):
        data = {
            "auths": {
                registry: {
                    "auth": Docker.__generate_auth_string(username, password)
                }
            },
            "HttpHeaders": {
                "User-Agent": "Docker-Client/19.03.12 (linux)"
            }
        }

        return json.dumps(data)

    @staticmethod
    def __save_docker_config(config_string):
        docker_path = Path.home().joinpath('.docker')
        if not docker_path.exists(): docker_path.mkdir(parents=True)

        with open(str(Path.home().joinpath('.docker').joinpath('config.json')), 'w+') as config_file:
            print(config_string, file=config_file)
