#!/usr/bin/python3

def sdef safe_print_integer(value):
    try:
        print("{:d}".format(int(value)), end="")
    except ValueError:
        return false
    else:
        return true
