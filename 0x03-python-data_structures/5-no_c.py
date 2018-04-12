#!/usr/bin/python3
def no_c(my_string):
    if my_string is not None:
        for i, d in enumerate(my_string):
            if d == 'c' or d == 'C':
                my_string = my_string[:i] + my_string[i + 1:]
        return my_string
