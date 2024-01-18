#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    args = sys.argv[1:]

    if len(args) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    if args[1] == "+":
        print("{} + {} = {}".format(args[0], args[2], int(args[0]) + int(args[2])))
    elif args[1] == "-":
        print("{} - {} = {}".format(args[0], args[2], int(args[0]) - int(args[2])))
    elif args[1] == "*":
        print("{} * {} = {}".format(args[0], args[2], int(args[0]) * int(args[2])))
    elif args[1] == "/":
        print("{} / {} = {}".format(args[0], args[2], int(args[0]) / int(args[2])))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    sys.exit(0)
