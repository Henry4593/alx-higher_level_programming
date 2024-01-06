#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    my_list_copy = [i for i in my_list]
    final_list = []
    for i in my_list_copy:
        if i % 2 == 0:
            final_list.append(True)
        else:
            final_list.append(False)
    return final_list
