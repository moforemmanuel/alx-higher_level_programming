#!/usr/bin/python
def print_last_digit(number):
    num = (abs(number))%10
    print("{}".format(num),end = "")
    return num
