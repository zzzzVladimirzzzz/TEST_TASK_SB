import json


def convert_func(json_file: str):
    with open(json_file, 'r') as f:
        test_dict = json.load(f)
        for key, val in test_dict.items():
            test_dict[key] = val
    return test_dict
