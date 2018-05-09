#!/usr/bin/python3
from sys import argv


save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

try:
    text = load_from_json_file('add_item.json')
except:
    text = []

for i, d in enumerate(argv):
    if i > 0:
        text.append(d)
save_to_json_file(text, 'add_item.json')
