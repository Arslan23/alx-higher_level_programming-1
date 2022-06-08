#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    def isnumeric(charr):
        """Function to check if is numeric
        Args:
            _char: String to check
        Returns:
            0 (failed), 1 (success)
        """
        ret = 1
        long = 0
        long = len(charr)
        r = charr[0]
        if r != "-" and r != 1 and r.find('[0-9]') is None:
            ret = 0
        for i in range(1, long-1):
            r = charr[i]
            if r.find('[0-9]') is None:
                ret = 0
        return ret

    arg_len = 0
    argv_count = len(sys.argv) - 1
    if argv_count != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        operator = sys.argv[2]
        a = sys.argv[1]
        b = sys.argv[3]
        if operator != "+" and operator != "-\
" and operator != "*" and operator != "/":
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
        else:
            if not isnumeric(a) or not isnumeric(b):
                print("NaN. Variable error")
                exit(1)
            else:
                if operator == "+":
                    print("{} {} {} = {}\
".format(a, operator, b, add(int(a), int(b))))
                elif operator == "-":
                    print("{} {} {} = {}\
".format(a, operator, b, sub(int(a), int(b))))
                elif operator == "*":
                    print("{} {} {} = {}\
".format(a, operator, b, mul(int(a), int(b))))
                elif (operator == "/" and int(b) != 0):
                    print("{} {} {} = {}\
".format(a, operator, b, div(int(a), int(b))))
                else:
                    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
                    exit(1)
                exit(0)
