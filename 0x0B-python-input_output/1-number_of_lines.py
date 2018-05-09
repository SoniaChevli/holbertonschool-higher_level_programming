#!/usr/bin/python3


def number_of_lines(filename=""):
    """ reads file and gives number of lines"""
    linecount = 0
    with open(filename, 'r') as f:
        for line in f:
            linecount = linecount + 1
    return linecount
