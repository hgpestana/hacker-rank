#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the diagonalDifference function below.
def plus_minus(list):
    size = len(list)

    positive_values = 0
    negative_values = 0
    zero_values = 0

    for i in range(size):
        if list[i] > 0:
            positive_values += 1
        elif list[i] == 0:
            zero_values += 1
        else:
            negative_values += 1

    print("{0:.6f}".format(positive_values/size))
    print("{0:.6f}".format(negative_values/size))
    print("{0:.6f}".format(zero_values/size))


if __name__ == '__main__':
    arr = [-4, 3, -9, 0, 4, 1]
    plus_minus(arr)
