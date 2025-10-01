#!/usr/bin/python3

table_count = 0

while table_count <= 10:
    table_list = []
    list_count = 0
    while list_count <= 10:
        table_list.append(table_count * list_count)
        list_count += 1
    print("Table of " + str(table_count) + ":", " ".join(map(str, table_list)))
    table_count += 1
