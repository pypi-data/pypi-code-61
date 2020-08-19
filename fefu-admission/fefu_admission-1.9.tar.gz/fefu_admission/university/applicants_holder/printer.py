from tabulate import tabulate

from fefu_admission.university.type_of_completion import TypeOfCompletion


class ApplicantsHolderInformationPrinter:

    def __init__(self, applicants_holder):
        self.applicants_holder = applicants_holder

    def print_info(self):
        me_enrollee = self.applicants_holder.settings.me

        len_applicants = self.applicants_holder.get_len_applicants()
        budget_places = self.applicants_holder.places[TypeOfCompletion.Budget]
        budget_places_for_now = self.applicants_holder.get_budget_places_for_now()

        number_of_applicants = self.applicants_holder.get_len_applicants(type_of_completion=TypeOfCompletion.Budget)
        number_of_applicants_with_agreement = self.applicants_holder.get_len_applicants(agreement=True)
        rows_list = [
            ["Название", self.applicants_holder.name],
            ["Всего подало", len_applicants],
            ["Бюджетных мест", budget_places],
            ["Бюджетные места на данный момент", budget_places_for_now]
        ]
        if me_enrollee is not None:
            me_position_among_all = self.applicants_holder.get_position_of_me(TypeOfCompletion.Budget)
            me_position_among_all_with_agreement = \
                self.applicants_holder.get_position_of_me(type_of_completion=TypeOfCompletion.Budget, agreement=True)
            rows_list += [
                ["Мое место среди бюджетников", "{} из {} ({k:.3f})".format(me_position_among_all, number_of_applicants,
                                                                            k=me_position_among_all / len_applicants)],
                ["Мое место среди бюджетников подавших согласие", "{} из {} ({k:.3f})".format(
                    me_position_among_all_with_agreement, number_of_applicants_with_agreement,
                    k=me_position_among_all_with_agreement / budget_places_for_now)]
            ]
        else:
            rows_list += [["Бюджетников подало", number_of_applicants]]
        rows_list += [["Подало согласие", number_of_applicants_with_agreement]]
        print(tabulate(rows_list, tablefmt='fancy_grid'))
