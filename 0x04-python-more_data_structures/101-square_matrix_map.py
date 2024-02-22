#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map((lambda i: map((lambda j: j * number)), i)), matrix[:])
