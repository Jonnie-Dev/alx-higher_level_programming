#!/usr/bin/python3

import sys
args = sys.argv[1:]
args_len = len(args)
print("{} {}".format(args_len, "argument" if args_len == 1 else "arguments"))
for i in  range(args_len):
    print("{}: {}".format(i+1, args[i]))
