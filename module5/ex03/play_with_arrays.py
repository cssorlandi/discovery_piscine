#!/usr/bin/python3

original_array =  [2, 8, 9, 48, 8, 22, -12, 2]
modified_array = []

for item in original_array:
    if item > 5:
        modified_array.append(item + 2)

numbers_set = set(modified_array)

print(original_array)
print(numbers_set)
