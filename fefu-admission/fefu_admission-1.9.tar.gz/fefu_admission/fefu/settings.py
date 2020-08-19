import os

from fefu_admission.university import Settings
from fefu_admission.utils import Utils

from lxml import html


class FefuSettings(Settings):
    URL_TABLE = "https://www.dvfu.ru/admission/program-bs/b/"

    def __init__(self, university):
        super().__init__(university,
                         data_path=os.path.join(os.path.expanduser('~'), ".fefu_admission"))

    def __get_html_with_departments_list(self):
        return Utils.get_response(
            method="get",
            url=self.URL_TABLE
        ).text

    def get_list_of_all_departments(self):

        def remove_spaces_on_the_sides(string):
            start = 0
            end = len(string)

            for i in range(0, len(string)):
                if string[i] != " " and string[i] != " " and string[i] != "\t":
                    break
                start += 1

            for i in range(end - 1, -1, -1):
                if string[i] != " " and string[i] != " " and string[i] != "\t":
                    break
                end -= 1
            return string[start:end]

        page = html.fromstring(self.__get_html_with_departments_list())
        table = page.get_element_by_id("program")
        tbody = table.find("tbody")
        print(tbody)

        departments_list = []
        for tr in tbody[:len(tbody) - 1]:
            department_str = "{} {}".format(
                *[remove_spaces_on_the_sides(item.text_content().replace("\t", "").replace("\n", "")) for item in tr[0:2]]
            )
            departments_list.append(department_str)

        return departments_list
