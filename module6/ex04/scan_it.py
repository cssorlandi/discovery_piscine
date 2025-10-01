#!/usr/bin/python3

import sys

params = sys.argv
params.pop(0)

if len(params) != 2:
    print("none")
else:
    first_param = params[0]
    second_param = params[1]
    result = second_param.count(first_param)
    if result == 0:
        print("none")
    else:
        print(result)
