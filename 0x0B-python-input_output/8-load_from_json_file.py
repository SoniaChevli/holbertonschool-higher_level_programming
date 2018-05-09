#!/usr/bin/python3


def load_from_json_file(filename):
    """ creates object from json file"""
    import json
    with open(filename, 'r', encoding='utf-8') as f:
        return json.loads(f)
