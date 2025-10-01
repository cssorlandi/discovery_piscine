#!/usr/bin/python3

user_input = int(input("Please tell me your age: "))

print(f"You are currently {user_input} years old")

years_count = 10

while years_count <= 30:
    print(f"In {years_count} years, you'll be {user_input + years_count} years old.")
    years_count += 10
