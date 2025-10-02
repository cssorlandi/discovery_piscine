#!/usr/bin/python3

import sys

params = sys.argv
params.pop(0)

if len(params) == 0:
    print("none")
else:
    print("parameters:", len(params))
    for param in params:
        print(f"{param}: {len(param)}")
