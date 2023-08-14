#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return None
    idx_reverse = -1
    for _ in range(len(my_list)):
        print("{}".format(my_list[idx_reverse]))
        idx_reverse -= 1
