#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i = 0
    l = len(sys.argv) - 1
    if l == 0:
        print("0 argument.")
    elif l == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(l))
    for i in range(l):
        print("{}: ".format(i + 1) + "{}".format(sys.argv[i + 1]))
