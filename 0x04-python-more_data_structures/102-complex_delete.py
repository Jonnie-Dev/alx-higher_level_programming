#!/usr/bin/python3
def complex_delete(a_dict, value):
    for i in a_dict.keys():
        if a_dict[i] == value:
            del a_dict[i]

    return a_dict
