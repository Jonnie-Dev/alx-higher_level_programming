#!/usr/bin/python3
def complex_delete(a_dict, value):
    new_dict = dict(a_dict)
    for i in new_dict.keys():
        if a_dict[i] == value:
            del a_dict[i]

    return a_dict
