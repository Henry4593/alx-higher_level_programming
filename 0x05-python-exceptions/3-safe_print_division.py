#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        result = float(a) / b
    except (ZeroDivisionError, TypeError, OverflowError, ValueError):
        result = None
    finally:
        print("Inside result_div: {}".format(result))
