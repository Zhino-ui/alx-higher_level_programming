#!/usr/bin/python3
def search_replace(my_list, search, replace):
    n_list = []
    for x in my_list:
        if x == search:
            n_list.append(replace)
        else:
            n_list.append(x)
    return n_list
