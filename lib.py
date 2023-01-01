import json
from csv import DictReader


def get_csv_data(csv_file):
    """Generator function that yields each csv record as dictionary"""
    with open(csv_file) as csv_file_handler:
        for row in DictReader(csv_file_handler):
            yield row


def pretty_print(_object, title='', indent=4):
    print(title + '\n', json.dumps(_object, indent=indent))


def enrich_data(_dict, **kwargs):
    result_dict = _dict.copy()

    for key, value in kwargs.items():
        try:
            result_dict[key] = value(_dict[key])
        except ValueError:
            result_dict[key] = value()  # initialize with default value

    return result_dict
