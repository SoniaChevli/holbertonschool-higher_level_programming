#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    if len(sys.argv) == 0:
        print("0 arguments.")
    else:
        print("{:d} arguments:".format(len(sys.argv) - 1))

        for x in range(1, len(sys.argv)):
            print("{:d}: {:s}".format(x, sys.argv[x]))
