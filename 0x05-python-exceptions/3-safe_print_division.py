#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        result = a / b
    except (ZeroDivisionError, TypeError, OverflowError, ValueError):
        result = None
    finally:
        print("Inside result_div: {:f}".format(result))
