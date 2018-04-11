#!/usr/bin/python3
for x in range(90, 64, -1):
    if (x % 2 == 0):
        x = x + 32
    print('{:c}'.format(x), end='')
    if (x > 96):
        x = x - 32
