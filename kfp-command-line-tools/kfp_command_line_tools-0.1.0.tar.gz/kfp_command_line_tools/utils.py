import json


def _parameters_from_file(obj):
    with open(obj) as f:
        parameters_file = json.load(f)
        return parameters_file


def _parameters_from_command_line(obj):
    params_list = [_ for _ in obj]
    parameters_dict = {str(params_list[i]): str(params_list[i + 1]) for i in range(0, len(params_list), 2)}
    return parameters_dict


def verify(params, file_params):
    if len(params) == 0:
        return _parameters_from_file(file_params)
    else:
        return _parameters_from_command_line(params)
