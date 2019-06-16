#!/bin/python3

import math
import os
import random
import re
import sys


def grading_students(array: list) -> list:
    list_size: int = len(array)

    for i in range(list_size):
        if array[i] >= 38:
            next_multiple = ((array[i] + 4) // 5) * 5
            if next_multiple - array[i] < 3:
                array[i] = next_multiple

    return array


if __name__ == '__main__':
    arr = [73, 67, 38, 33]
    print(grading_students(arr))

