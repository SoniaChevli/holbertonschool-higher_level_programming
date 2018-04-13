#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list =[]
    for d in my_list:
        if d == search:
            new_list.append(replace)
        else:
            new_list.append(d)
    return new_list
