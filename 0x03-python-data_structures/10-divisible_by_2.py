#!/bin/usr/python3
def divisible_by_2(my_list=[]):
    list_dup = []
    for d in my_list:
        if d % 2 == 0:
            list_dup.append(True)
        else:
            list_dup.append(False)
    return list_dup
