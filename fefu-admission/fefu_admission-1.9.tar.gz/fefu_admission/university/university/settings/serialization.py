import os
import json

from fefu_admission.prompt import Prompt
from fefu_admission.university.enrollee import Enrollee


class SettingsSerialization:

    def __init__(self, settings, data_path):
        self.settings = settings
        self.data_path = data_path

    def load(self):
        if not os.path.isfile(self.get_path_to_settings_file()):
            if Prompt.get_confirm("Settings file not founded. Do you want generate settings file?"):
                self.generate_and_save_settings()
            else:
                return {
                    "me": None,
                    "list_of_departments": []
                }
        read_file = open(self.get_path_to_settings_file(), "r")
        data = json.load(read_file)
        read_file.close()

        self.settings.me = Enrollee.get_from_json(data.get("me", None))
        self.settings.list_of_departments = data.get("list_of_departments", [])

    def __create_settings_file(self, settings_content):
        if not os.path.exists(self.data_path):
            os.makedirs(self.data_path)
        with open(self.get_path_to_settings_file(), 'w') as settings_file:
            json.dump(settings_content, settings_file)

    def get_generated_settings(self):
        selected_departments_str = []
        list_of_all_departments = self.settings.get_list_of_all_departments()
        print("Do you want to add this direction?")
        for department_str in list_of_all_departments:
            answer = Prompt.get_confirm(department_str)
            if answer == Prompt.YES:
                selected_departments_str.append(department_str)
            else:
                pass
        settings_data = {
            "list_of_departments": selected_departments_str
        }
        if Prompt.get_confirm("do you want to know your place on the list?") == Prompt.YES:
            name = Prompt.get_str("Enter name")
            points = [int(x) for x in Prompt.get_str("Enter your points").split(" ")]
            settings_data["me"] = {
                "name": name,
                "points": points,
                "agreement": True
            }
        else:
            settings_data["me"] = None
        return settings_data

    def generate_and_save_settings(self):
        self.__create_settings_file(self.get_generated_settings())

    def get_path_to_settings_file(self):
        return os.path.join(self.data_path, "settings.json")
