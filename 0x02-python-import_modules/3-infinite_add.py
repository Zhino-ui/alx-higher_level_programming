#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    final = 0
    for x in range(len(sys.argv) - 1):
        final += int(sys.argv[x + 1])
    print("{}".format(final))
