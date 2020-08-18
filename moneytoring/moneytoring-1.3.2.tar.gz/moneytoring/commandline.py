import sys
from .query import *
from .parser import get_parsed_data


def help_cmd():
    print("help command")
    return True


def filter_dest():
    print("filter by dest command")
    return True


def report_budget(salary_input=None, month_count=None, money_left=None, parsed_dataset=get_parsed_data()):
    salary_input = sys.argv[1] if salary_input is None else salary_input
    month_count = sys.argv[2] if month_count is None else month_count
    money_left = sys.argv[3] if money_left is None else money_left
    salary_input = float(salary_input)
    money_left = float(money_left)
    month_count = int(month_count)
    for i in range(month_count):
        print(f"----------- Month n°{i+1} ------------")
        money_left += salary_input
        print(
            f"\033[92m++ Salary : {salary_input} €\033[0m ==> Money left : \033[93m{round(money_left, 2)} €\033[0m")
        food_expenses = round((salary_input * 26)/100, 2)
        money_left -= food_expenses
        print(
            f"\033[91m-- Food : {food_expenses} €\033[0m ==> Money left : \033[93m{round(money_left, 2)} €\033[0m")
        money_left -= 150
        print(
            f"\033[91m-- Home : 150 €\033[0m ==> Money left : \033[93m{round(money_left, 2)} €\033[0m")
        money_left -= 275
        print(
            f"\033[91m-- Cofidis : 275 €\033[0m ==> Money left : \033[93m{round(money_left, 2)} €\033[0m")
    return True


def yearly_summary(year_input=None, parsed_dataset=get_parsed_data()):
    year_input = sys.argv[1] if year_input is None else year_input
    if year_input == "all":
        for year in get_years(parsed_dataset):
            print("--------------------")
            print(
                f"Dépensé en {str(year)} : \033[91m{round(get_total_expenses(get_data_by_year(year, parsed_dataset)),2)} €\033[0m")
            print(
                f"Obtenu en {str(year)} : \033[92m{round(get_total_incomes(get_data_by_year(year, parsed_dataset)), 2)} €\033[0m")
    else:
        try:
            print(
                f"Dépensé en {str(year_input)} : \033[91m{round(get_total_expenses(get_data_by_year(int(year_input), parsed_dataset)),2)} €\033[0m")
            print(
                f"Obtenu en {str(year_input)} : \033[92m{round(get_total_incomes(get_data_by_year(int(year_input), parsed_dataset)), 2)} €\033[0m")
        except ValueError:
            print("Can't parse this value into an integer")
    return True


def summary(parsed_dataset=get_parsed_data()):
    print(
        f"Total dépensé : \033[91m{round(get_total_expenses(parsed_dataset), 2)} €\033[0m")
    print(
        f"Total obtenu : \033[92m{round(get_total_incomes(parsed_dataset), 2)} €\033[0m")
    return True
