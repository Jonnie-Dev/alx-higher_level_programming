#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    args = sys.argv[1:]
    args_len = len(args)
    print("{}".format(args_len), end="")
    print("{}".format("argument" if args_len == 1 else "arguments"), end="")
    print("{}".format("." if args_len == 0 else ":"))
    for i in range(args_len):
        print("{}: {}".format(i+1, args[i]))
