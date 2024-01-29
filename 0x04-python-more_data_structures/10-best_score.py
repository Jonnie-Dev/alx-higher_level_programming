#!/usr/bin/python3

def best_score(a_dict):
    if a_dict is None:
        return None
    highest = ["", 0]
    for key in a_dict.keys():
        if a_dict[key] > highest[1]:
            highest = [key, a_dict[key]]
    return highest[0]
