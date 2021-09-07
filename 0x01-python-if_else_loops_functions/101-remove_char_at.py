#!/usr/bin/python3
def remove_char_at(str, n):
    new_list = list(str)
    new_list.remove(new_list[n])
    new_str = "".join(new_list)
    return new_str
