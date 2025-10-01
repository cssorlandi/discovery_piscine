#!/usr/bin/python3

import sys

params = sys.argv
params.pop(0)

if len(params) != 1:
    print("none")
else:
    first_param = params[0]
    user_entry = input("What was the parameter? ")
    if first_param != user_entry:
        print("Nope, sorry...")
    else:
        print("Good job!")
