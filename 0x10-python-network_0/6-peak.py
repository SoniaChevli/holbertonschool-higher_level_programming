#!/usr/bin/python3
'''
technical interview practice
find the peak in the unsorted array
'''


def find_peak(list_of_integers):
    ''' find peak function '''
    if list_of_integers == []:
        return None

    for i in range(0, len(list_of_integers) - 1):
        if list_of_integers[i] > list_of_integers[i + 1]:
            return list_of_integers[i]

    if list_of_integers[len(list_of_integers) - 1] > \
       list_of_integers[len(list_of_integers) - 2] or \
       list_of_integers[len(list_of_integers) - 1] == \
       list_of_integers[len(list_of_integers) - 2]:
        return list_of_integers[len(list_of_integers) - 1]
    return None
