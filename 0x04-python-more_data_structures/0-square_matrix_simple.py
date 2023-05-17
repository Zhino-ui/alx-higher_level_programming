#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    n_matrix = []
    for row in matrix:
        n_row = []
        for x in row:
            n_row.append(x ** 2)
        n_matrix.append(n_row)
    return n_matrix
