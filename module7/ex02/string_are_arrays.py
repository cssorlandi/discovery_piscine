#!/usr/bin/python3

import sys

params = sys.argv
params.pop(0)

if len(params) != 1:
    print("none")
else:
    param = params[0]
    if param.count("z") == 0:
        print("none")
    else:
        z_counter = ""
        for char in param:
            if char == "z":
                z_counter = z_counter + "z"
        print(z_counter)
