#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list

    n_list = []

    for x in range(len(my_list)):
        if x != idx:
            n_list.append(my_list[x])
    return n_list
