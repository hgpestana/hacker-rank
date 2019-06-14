#!/bin/python3

import math
import os
import random
import re
import sys


def staircase(size, length):
    if size > 1:
        staircase(size-1, length)
    print('{:>{len}}'.format(size*"#", len=length))


if __name__ == '__main__':
    staircase(5, 5)
