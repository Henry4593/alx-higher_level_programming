#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary is not None:
        new_dict = sorted(a_dictionary.items())
        for key, value in new_dict:
            print("{}: {}".format(key, value))
    else:
        return
