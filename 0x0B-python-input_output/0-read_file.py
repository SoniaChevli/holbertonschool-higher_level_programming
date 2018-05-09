#!/usr/bin/python3


def read_file(filename=""):
    """ opens and reads the file"""
    with open(filename, 'r') as f:
        for line in f:
            print(line, end='')
