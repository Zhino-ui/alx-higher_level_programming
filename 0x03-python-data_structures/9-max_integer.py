#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None

    max_value = float('-inf')

    for x in my_list:
        if x > max_value:
            max_value = x
    return max_value