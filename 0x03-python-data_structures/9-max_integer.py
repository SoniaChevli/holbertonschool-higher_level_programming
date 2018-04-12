#!/usr/bin/python3
def max_integer(my_list=[]):
    biggest_int = 0
    if len(my_list) == 0 or my_list == []:
        return None
    for i, d in enumerate(my_list):
        if d > biggest_int:
            biggest_int = d
    return biggest_int
