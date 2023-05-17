#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    t_weight = 0
    w_sum = 0

    for score, weight in my_list:
        t_weight += weight
        w_sum += score * weight

    return w_sum / t_weight
