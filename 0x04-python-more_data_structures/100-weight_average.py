#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0
    else:
        productlist = list((map(lambda x: x[0] * x[1], my_list)))
        weight = list(map(lambda x: x[1], my_list))
        sum_product = 0
        sum_weight = 0
        for prod_elem, weight_elem in zip(productlist, weight):
            sum_product += prod_elem
            sum_weight += weight_elem
        average = sum_product / sum_weight
        return average
