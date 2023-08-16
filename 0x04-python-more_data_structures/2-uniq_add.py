#!/usr/bin/python3
def uniq_add(my_list=[]):
    final_list = list(set(my_list))
    sum_total = 0
    for item in final_list:
        sum_total += item
    return sum_total
