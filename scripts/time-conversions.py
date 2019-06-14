#!/bin/python3

from datetime import datetime


def time_conversion(time: str) -> str:

    dt = datetime.strptime(time, '%I:%M:%S%p')
    return dt.strftime('%H:%M:%S')


if __name__ == '__main__':

    print(time_conversion('12:40:22AM'))
    print(time_conversion('12:40:22PM'))
