from csv import reader
from os import path
from datetime import datetime


def get_csv_file_path():
    return path.join(path.dirname(__file__), "transactions.csv")


def get_reader():
    csv_reader = None
    if path.exists(get_csv_file_path()):
        csv_reader = reader(open(get_csv_file_path()))
    return csv_reader


def get_parsed_data():
    parsed_data = []
    try:
        lines = [line for line in open(get_csv_file_path())]
        for line in lines:
            if line != lines[0]:
                listed = line.strip().replace(',', '.').split(';')
                date = datetime.strptime(listed[0], '%d/%m/%Y')
                type_transaction = listed[2]
                montant = float(listed[5])
                dest = listed[7]
                parsed_data.append([date, type_transaction, montant, dest])
    except FileNotFoundError:
        print("You need to populate the program with a CSV file first !!")
        print("Usage : setup-csv <path_of_your_csv>")
    return parsed_data
