#!/usr/bin/python3

"""
Function to find peak in an array of integers
"""


def find_peak(array: list) -> int:
    """
    Find peak of an array
    :param array:
    :return: peak
    """
    peak = None
    if array:
        peak = max(array)
        # print(array.index(peak))
        # if array.index(peak) == 0:
        #     peak = max(array[1:])
    return peak
