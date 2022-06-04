#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv_count = len(sys.argv)
    if argv_count == 1:
        print("{} arguments.".format(argv_count - 1))
    elif argv_count == 2:
        print("{} argument:".format(argv_count - 1))
    else:
        print("{} arguments:".format(argv_count - 1))
    for i in range(1, argv_count):
        print("{}: {}".format(i + 1, sys.argv[i]))
