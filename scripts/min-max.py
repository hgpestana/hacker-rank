#!/bin/python3

import math
import os
import random
import re
import sys


def min_max(array):

    results = []

    for i in range(len(array)):
        results.append(sum(array) - array[i])

    print("{} {}".format(min(results), max(results)))


if __name__ == '__main__':

    arr = [1, 2, 3, 4, 5]
    min_max(arr)
