#!/usr/bin/python3
def uppercase(str):
    for char in str:
        print("{}".format(ord(char) - 32), end="")
    print("{}", end="\n")
