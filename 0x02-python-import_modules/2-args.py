#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    counter = len(sys.argv) - 1
    if counter == 0:
        print("0 argument")
    elif counter == 1:
        print("1 argument")
    else:
        print("{} argumaents".format(counter))
    for x in range(counter):
        print("{}:{}".format(x + 1, sys.argv[x + 1]))

