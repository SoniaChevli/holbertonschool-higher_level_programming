#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix != [[]]:
        for row in matrix:
            for i, d in enumerate(row):
                if i != len(row) - 1:
                    print('{:d}'.format(d), end=' ')
                else:
                    print('{:d}'.format(d))
    else:
        print('')
