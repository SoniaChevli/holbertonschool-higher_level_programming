#!/usr/bin/python3
j = 1
i = 0
while(i < 9):
    x = j
    while(x < 10):
        if(x == 9 and i == 8):
            print('{:d}{:d}'.format(i, x))
        else:
            print("{:d}{:d}, ".format(i, x), end='')
        x = x + 1
    j = j + 1
    i = i + 1
