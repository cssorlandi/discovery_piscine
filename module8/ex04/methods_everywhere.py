#!/usr/bin/python3

import sys

params = sys.argv
params.pop(0)

def shrink(param):
    print(param[:8])

def enlarge(param):
    formatted_param = param
    count = len(param)
    while count < 8:
        formatted_param = formatted_param + "Z"
        count += 1
    print(formatted_param)

if len(params) == 0:
    print("none")
else:
    for param in params:
        if len(param) > 8:
            shrink(param)
        elif len(param) < 8:
            enlarge(param)
        else:
            print(param)
