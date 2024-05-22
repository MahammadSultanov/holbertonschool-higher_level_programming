#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    n = len(matrix)
    a = matrix[0]
    m = len(a)
    for i in matrix:
        for j in range(m):
            print("{:d}".format(i[j]), end=' ')
        print()
