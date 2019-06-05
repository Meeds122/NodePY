#!/usr/bin/python3

def main(in_list):
    import time

    # Values are passed in as a list of arguments i.e. arg1 = [arg1, arg2, etc. ]
    # In this case, we only care about the first value

    when = in_list[0]

    # Testing
    print(in_list)
    print(when)

    if when.lower() == 'now':
        return "now: " + str(time.asctime( time.localtime(time.time()) ))
    else:
        return str(time.asctime( time.localtime(time.time()) ))
