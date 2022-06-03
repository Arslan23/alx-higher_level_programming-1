#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    import re
    i = 0
    arg_len = 0
    type_c = 0
    r = ""
    _sum = 0

    argv_count = len(sys.argv) - 1
    if argv_count > 0:
        for i in range(argv_count):
            arg_len = len(sys.argv[i + 1])
            for j in range(arg_len):
                r = sys.argv[i + 1]
                if r.find('[0-9]*') is None:
                    type_c = 1
            if type_c != 1:
                _sum = _sum + int(sys.argv[i + 1])
                type_c = 0
    print("{}".format(_sum))
