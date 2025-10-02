#!/usr/bin/python3

import sys

params = sys.argv
params.pop(0)

if len(params) != 2:
    print("none")
else:
    first_number = int(params[0])
    second_number = int(params[1])
    if first_number > second_number:
        print("none")
    else:
        numbers_list = list(range(first_number, second_number + 1))
        print(numbers_list)
