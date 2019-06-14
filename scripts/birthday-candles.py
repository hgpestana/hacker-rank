#!/bin/python3

import math
import os
import random
import re
import sys


def birthday_candles(array: list) -> None:

    max_height: int = max(array)
    count: int = array.count(max_height)

    print(count)


if __name__ == '__main__':

    arr = [1, 2, 3, 5, 5]
    birthday_candles(arr)
