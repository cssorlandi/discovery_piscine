#!/usr/bin/python3

import sys

parameters = sys.argv
parameters.pop(0)

if len(parameters) < 2:
    print("none")
else:
    parameters.reverse()
    for param in parameters:
        print(param)
