#!/usr/bin/python3

def common_elements(set_1, set_2):
    common_el = []
    for i in set_2:
        if i in set_1:
            common_el.append(i)
    return common_el
