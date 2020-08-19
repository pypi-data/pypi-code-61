from fefu_admission.university.applicants_holder import ApplicantsHolderBase

from .serialization import DepartmentSerialization


class Department(ApplicantsHolderBase):

    def __init__(self, n: str, university):
        super().__init__()
        self.name = n
        self.serialization = DepartmentSerialization(self)
        self.university = university
        self.settings = university.settings

    def get_html_table(self):
        """
        Get html page with a table with information of applicants
        :return: html_text: str
        """
        pass

    def load_from_web(self):
        """
        Calls a method serialization.get_html_table() and parses the table data, adding applicants to the lists
        :return: None
        """
        pass

    def __str__(self):
        return self.name
