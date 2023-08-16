#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()
    final_matrix = []
    for row in new_matrix:
        row = list(map(lambda num: num ** 2, row))
        final_matrix.append(row)
    return final_matrix
