#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        arr_i = matrix[i]
        for j in range(len(arr_i)):
            end_char = " " if j < len(arr_i) - 1 else "\n"
            print("{:d}".format(arr_i[j]), end=end_char)
    if matrix == [[]]:
        print()
