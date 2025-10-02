#!/usr/bin/python3

import sys

params = sys.argv
params.pop(0)

if len(params) == 0:
    print("none")
else:
    for param in params:
        if not (param.find("ism") == len(param) - 3):
            print(f"{param}ism")
