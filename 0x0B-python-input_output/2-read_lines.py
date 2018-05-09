#!/usr/bin/python3


def read_lines(filename="", nb_lines=0):
    """ read n lines of a file """
    linecount = 0
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            linecount += 1
            print(line, end='')
            if linecount == nb_lines:
                break
