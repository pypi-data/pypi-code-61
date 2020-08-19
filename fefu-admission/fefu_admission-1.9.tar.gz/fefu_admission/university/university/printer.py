from colorama import Back, Fore, Style
from tabulate import tabulate

from fefu_admission.university.applicants_holder import \
    ApplicantsHolderInformationPrinter
from fefu_admission.university.type_of_completion import TypeOfCompletion


class UniversityInformationPrinter(ApplicantsHolderInformationPrinter):

    def __init__(self, applicants_holder):
        super().__init__(applicants_holder)

    def get_list_of_department(self, department, with_agreement=False):
        rows_list = []
        index = self.applicants_holder.departments.index(department)
        for type_of_completion in [TypeOfCompletion.SpecialQuota,
                                   TypeOfCompletion.TargetQuota,
                                   TypeOfCompletion.Budget]:
            rows_list.append([type_of_completion.value])
            if with_agreement:
                list_applicants = department.applicants_with_agreement[type_of_completion]
            else:
                list_applicants = department.applicants[type_of_completion]

            for index_of_enrollee, enrollee in enumerate(list_applicants):
                me = self.applicants_holder.settings.me
                if type_of_completion == TypeOfCompletion.Budget:
                    if me is not None:
                        if me < enrollee:
                            break
                applied_for_another_dep = None
                another_dep = None
                for index_of_department, item in enumerate(self.applicants_holder.departments):
                    if index == index_of_department:
                        continue
                    applied_for_another_dep = item.search_enrollee_in_list_with_agreement(
                        type_of_completion, enrollee.name) is not None
                    if applied_for_another_dep:
                        another_dep = item
                        break
                style_start = ""
                note = ""
                if applied_for_another_dep:
                    style_start = Back.RED + Fore.BLACK
                    note = "Подал на {}".format(another_dep.name)
                elif enrollee.agreement:
                    style_start = Back.GREEN + Fore.BLACK
                    note = "Подал на это направление"

                rows_list.append([index_of_enrollee + 1, "{}{}{}".format(style_start, enrollee.name, Style.RESET_ALL),
                                  *enrollee.points, enrollee.get_points_sum(), note])

        return rows_list

    def print_list_of_department(self, department, with_agreement=False):
        ApplicantsHolderInformationPrinter(department).print_info()
        print(tabulate(self.get_list_of_department(department, with_agreement), tablefmt='fancy_grid'))

    def search_for_matches(self):
        total = 0
        for dep in self.applicants_holder.departments:
            for type_of_completion in TypeOfCompletion:
                count = 1
                points = []
                departments_list = dep.applicants[type_of_completion]
                for enrollee_index, enrollee in enumerate(departments_list):
                    if points == enrollee.points:
                        count += 1
                    else:
                        if count >= 3:
                            print("{}, {}".format(dep.name, type_of_completion.value))
                            for i in range(enrollee_index - count, enrollee_index):
                                enr = departments_list[i]
                                print(i + 1 - (enrollee_index - count), enr.name, enr.points)
                            print("\n")
                            total += 1
                        count = 1
                        points = enrollee.points
        print("Number of matches in a row: {}".format(total))
