import json
import yaml

from path import check_path


def read_text(file):
    file = check_path(file)
    with open(file, 'rt') as f:
        lines = f.readlines()
    return lines


def write_text(file, lines, mode='wt'):
    file = check_path(file, str)
    with open(file, mode) as f:
        f.writelines(lines)


def read_yaml(file):
    file = check_path(file, str)
    with open(file, 'rt') as f:
        yaml_dict = yaml.safe_load(f)
    return yaml_dict


def write_yaml(file, dictionary):
    file = check_path(file, str)
    with open(file, 'wt') as f:
        yaml.safe_dump(dictionary, f)


def read_json(file):
    file = check_path(file, str)
    with open(file, 'rt') as f:
        json_dict = json.load(f)
    return json_dict


def write_json(file, dictionary):
    file = check_path(file, str)
    with open(file, 'wt') as f:
        json.dump(dictionary, f)
