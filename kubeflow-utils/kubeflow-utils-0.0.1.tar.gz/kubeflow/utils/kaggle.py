import json
from pathlib import Path


class Kaggle:
    def login(self, username, apikey):
        kaggle_json = Kaggle.__generate_kaggle_json_string(username, apikey)
        Kaggle.__save_kaggle_json(kaggle_json)

    @staticmethod
    def __generate_kaggle_json_string(username, apikey):
        data = {
            "username": username,
            "key": apikey
        }

        return json.dumps(data)

    @staticmethod
    def __save_kaggle_json(json_str):
        kaggle_path = Path.home().joinpath('.kaggle')
        if not kaggle_path.exists(): kaggle_path.mkdir(parents=True)

        with open(str(kaggle_path.joinpath('kaggle.json')), 'w+') as kaggle_json:
            print(json_str, file=kaggle_json)
