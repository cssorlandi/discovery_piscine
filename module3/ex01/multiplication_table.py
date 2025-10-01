#!/usr/bin/python3

print("Enter a number")
user_input = int(input())

count = 0

while count <= 10:
    result = count * user_input
    print(count, "x", user_input, "=", result)
    count += 1
