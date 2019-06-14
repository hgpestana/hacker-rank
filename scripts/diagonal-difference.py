#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the diagonalDifference function below.
def diagonal_difference(matrix):

    size = len(matrix)
    max_value = len(matrix) - 1

    diagonal_left = 0
    diagonal_right = 0

    for i in range(size):
        diagonal_left += matrix[i][i]
        diagonal_right += matrix[i][max_value - i]

    return abs(diagonal_left - diagonal_right)


if __name__ == '__main__':

    arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
    print(diagonal_difference(arr))
