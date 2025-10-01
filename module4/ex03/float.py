#!/usr/bin/python3

user_input = float(input("Give me a number: "))

frac = user_input % 1

if (frac > 0):
    print("This number is a decimal.")
else:
    print("This number is an integer.")
