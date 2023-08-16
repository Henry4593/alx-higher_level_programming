#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    list_keys = list(a_dictionary.keys())
    for key in list_keys:
        if a_dictionary[key] == value:
            del a_dictionary[key]
    return a_dictionary
