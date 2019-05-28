#!/usr/bin/python3

def main(when):
    import time

    if when.lower == 'now':
        return "now: " + str(time.asctime( time.localtime(time.time()) ))
    else:
        return str(time.asctime( time.localtime(time.time()) ))