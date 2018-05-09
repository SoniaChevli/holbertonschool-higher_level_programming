#!/usr/bin/python3


def save_to_json_file(my_obj, filename):
    """ writes an object to a textfile"""
    import json
    with open(filename, 'w') as f:
        my_obj = json.dumps(my_obj)
        f.write(my_obj)
