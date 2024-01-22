#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        result_div = a / b
    except ZeroDivisionError:
        result_div = None
    except TypeError:
        result_div = None
    finally:
        print("Inside result_div: {0}".format(result_div))
        return result_div
