#!/usr/bin/python3

import sys

params = sys.argv
params.pop(0)


def downcase_it(text):
    return text.lower()


if len(params) <= 0:
    print("none")
else:
    for param in params:
        print(downcase_it(param))
