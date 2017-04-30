import json
from collections import namedtuple


def parser(json_file):
    with open(json_file) as f:
        config = json.loads(f.read())

    def convert_namedtuple(item):
        if isinstance(item, dict):
            for key, value in item.items():
                if isinstance(value, dict) or isinstance(value, list):
                    item[key] = convert_namedtuple(value)
            return namedtuple('config', item.keys())(**item)
        if isinstance(item, list):
            for key, value in enumerate(item):
                if isinstance(value, dict) or isinstance(value, list):
                    item[key] = convert_namedtuple(value)
        return item
    return convert_namedtuple(config)
