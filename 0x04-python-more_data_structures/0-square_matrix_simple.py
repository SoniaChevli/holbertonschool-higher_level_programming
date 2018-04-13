#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    a = []
    for row in matrix:
        a.append([i ** 2 for i in row])
    return a
