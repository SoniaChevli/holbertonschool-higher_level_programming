#!/usr/bin/python3
def remove_char_at(str, n):
    copy = ''
    for x in range(len(str)):
        if (x != n):
            copy += str[x]
    return copy
