#!/usr/bin/python3

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


print(find_peak([1, 2, 4, 6, 3]))
print(find_peak([4, 2, 1, 2, 3, 1]))
print(find_peak([2, 2, 2]))
print(find_peak([]))
print(find_peak([-2, -4, 2, 1]))
print(find_peak([4, 2, 1, 2, 2, 2, 3, 1]))