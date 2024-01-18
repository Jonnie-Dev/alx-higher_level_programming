#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    operators = {"+": add, "-": sub, "*": mul, "/": div}

    if len(sys.argv) != 4 or sys.argv[2] not in operators:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a, operator, b = sys.argv[1], sys.argv[2], sys.argv[3]

    if (not a.isdigit() or (a[1:].isdigit() and a[0] == '-')) or \
       (not b.isdigit() or (b[1:].isdigit() and b[0] == '-')):
        print("Invalid input. <a> and <b> must be integers.")
        sys.exit(1)

    a, b = int(a), int(b)
    result = operators[operator](a, b)

    print("{} {} {} = {}".format(a, operator, b, result))
    sys.exit(0)
