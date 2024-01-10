#!/usr/bin/python3
def search_replace(my_list, search, replace):
    final_list = my_list.copy()
    for idx, item in enumerate(final_list):
        if item == search:
            final_list[idx] = replace
    return final_list
