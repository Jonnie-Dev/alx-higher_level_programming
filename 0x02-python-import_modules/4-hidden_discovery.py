#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4

    names = dir(hidden_4)
    names = sorted(name for name in names if not name.startswith("__"))

    for name in names:
        print("{}".format(name))
