from fefu_admission.university.university.university import University

from .department import FefuDepartment


class FefuUniversity(University):

    def __init__(self, settings):
        super().__init__(name="ДВФУ", departmentClass=FefuDepartment, settings=settings)
