#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Determine the length of the longer list
    max_length = max(len(tuple_a), len(tuple_b))

    # Pad the shorter list with zeros
    list_a = list(tuple_a)
    list_b = list(tuple_b)

    list_a += [0] * (max_length - len(list_a))
    list_b += [0] * (max_length - len(list_b))

    # Now, both lists have the same length
    tuple_res = [a + b for a, b in zip(list_a, list_b)]
    return tuple(tuple_res[0:2])
