#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        x = ord(str[i])
        if (x >= 97 and x <= 122):
            x = x - 32
        if (i == len(str) - 1):
            print('{:c}'.format(x))
        else:
            print('{:c}'.format(x), end='')
