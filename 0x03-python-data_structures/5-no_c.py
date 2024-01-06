#!/usr/bin/python3

def no_c(my_string):
    new_str = [char_c for char_c in my_string if char_c not in "cC"]
    return "".join(new_str)
