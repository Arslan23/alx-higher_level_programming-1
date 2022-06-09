#!/usr/bin/python3
def simple_delete(a_dictionary, cle=""):
    if cle in a_dictionary:
        del a_dictionary[cle]
    return a_dictionary
