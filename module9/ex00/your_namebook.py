#!/usr/bin/python3

def array_of_names(names):
    names_list = []
    for key, value in names.items():
        names_list.append(f"{key.capitalize()} {value.capitalize()}")
    return names_list

persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}

print(array_of_names(persons))
