#!/usr/bin/python3

def is_red_head(family_member):
    name, head = family_member
    if head == "red":
        return True
    else:
        return False

def find_the_redheads(family_list):
    filtered_dictionary = dict(filter(is_red_head, family_list.items()))
    return list(filtered_dictionary.keys())

dupoint_family = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck": "red"
}

print(find_the_redheads(dupoint_family))
