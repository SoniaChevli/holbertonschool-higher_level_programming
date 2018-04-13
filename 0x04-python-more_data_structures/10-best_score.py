#!/usr/bin/python3
def best_score(a_dictionary):
    if type(a_dictionary) is not dict:
        return None
    if a_dictionary == {}:
        return None
    if a_dictionary is not None:
        return max(a_dictionary)
