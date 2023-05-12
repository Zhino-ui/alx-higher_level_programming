#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv
    import sys
    if len(sys.argv) != 4:
        print("Usage:", argv[0], "<a> <operator> <b>")
        exit(1)
    ops = argv[2]
    fun = {"+": add, "-": sub, "*": mul, "/": div}
    if ops not in fun:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    print("{:d} {:s} {:d} = {:d}".format(a, ops, b, fun[ops](a, b)))
