from .serialization import SettingsSerialization


class Settings:

    def __init__(self, university=None, data_path=""):
        self.serialization = SettingsSerialization(self, data_path)
        self.university = university
        self.me = None
        self.list_of_departments = []

    def get_data_path(self):
        return self.serialization.data_path

    def get_list_of_all_departments(self):
        return []
