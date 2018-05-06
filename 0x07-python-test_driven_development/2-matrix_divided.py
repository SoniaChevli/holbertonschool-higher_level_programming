#!/usr/bin/python3


def matrix_divided(matrix, div):
    new_matrix = []
    if matrix == []:
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    matrixlength = len(matrix[0])
    if not isinstance(matrix, list):
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    for i in matrix:
        if not isinstance(i, list):
            raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
        if len(i) !=  matrixlength:
            raise TypeError('Each row of the matrix must have the same size')
        for j in i:
            if not isinstance(j, (int, float)):
                raise TypeError('matrix must be a matrix (list of lists) of integers/floats')

    for row in matrix:
        new_matrix.append([round( i / div, 2) for i in row])
    return new_matrix


if __name__ == '__main__':
    import doctest
    doctest.testfile("./tests/2-matrix_divided.txt")
