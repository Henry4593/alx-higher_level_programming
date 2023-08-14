#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return None
    for idx_reverse in my_list[::-1]:
        print("{}".format(idx_reverse))
