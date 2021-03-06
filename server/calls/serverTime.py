"""
  This Source Code Form is subject to the terms of the Mozilla Public
  License, v. 2.0. If a copy of the MPL was not distributed with this
  file, You can obtain one at http://mozilla.org/MPL/2.0/.
"""

def main(in_list):
    import time

    # Values are passed in as a list of arguments i.e. arg1 = [arg1, arg2, etc. ]
    # In this case, we only care about the first value
    # We have to handle the case that there are too many arguments or not enough. Your choice as to 
    # what to do in each scenario
    try:
        when = in_list[0]
    except IndexError:
        when = ""

    if when.lower() == 'now':
        return "now: " + str(time.asctime( time.localtime(time.time()) ))
    else:
        return str(time.asctime( time.localtime(time.time()) ))
