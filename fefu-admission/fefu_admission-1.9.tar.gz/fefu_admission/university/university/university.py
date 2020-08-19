import logging

from fefu_admission.university.applicants_holder import ApplicantsHolderBase
from fefu_admission.university.department import DepartmentWebLoaderThread
from fefu_admission.university.type_of_completion import TypeOfCompletion
from fefu_admission.university.department.department import Department

from .serialization import UniversitySerialization


class University(ApplicantsHolderBase):

    def __init__(self, name="", departmentClass=Department, settings=None):
        super().__init__()
        self.name = name
        self.departments = []
        self.serialization = UniversitySerialization(self)
        self.departmentClass = departmentClass
        if settings is not None:
            self.set_settings(settings)
        else:
            self.settings = None

    def load_from_web_all(self):
        thread_list = []

        for department in self.departments:
            thread_list.append(DepartmentWebLoaderThread(department))

        for thread in thread_list:
            thread.start()
        for thread in thread_list:
            thread.join()
        logging.info("Done")

    def set_settings(self, settingsClass=None):
        self.settings = settingsClass(self)
        self.settings.serialization.load()
        for department in self.settings.list_of_departments:
            self.departments.append(self.departmentClass(department, self))

    def processing_all_departments(self):
        for type_of_completion in TypeOfCompletion:
            applicants_set = set()
            applicants_set_with_agreement = set()
            places = 0
            for department in self.departments:
                for enrolle in department.applicants[type_of_completion]:
                    applicants_set.add(enrolle)
                    if enrolle.agreement:
                        applicants_set_with_agreement.add(enrolle)
                places += department.places[type_of_completion]

            self.applicants[type_of_completion] = sorted(list(applicants_set))
            self.applicants_with_agreement[type_of_completion] = sorted(list(applicants_set_with_agreement))
            self.places[type_of_completion] = places
