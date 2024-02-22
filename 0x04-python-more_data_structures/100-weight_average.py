#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0

    avg = 0
    weight_count = 0
    for lst in my_list:
        avg += lst[0] * lst[1]
        weight_count += lst[1]

    return avg / weight_count
