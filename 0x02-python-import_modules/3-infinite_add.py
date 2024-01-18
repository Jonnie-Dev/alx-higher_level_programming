#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    args = sys.argv[1:]
    count = 0
    for i in range(len(args)):
        count += int(args[i])
    print("{}".format(count))
