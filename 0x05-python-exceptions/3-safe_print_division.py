#!/usr/bin/python3
def safe_print_division(a, b):
    result_div = 0

    try:
        result_div = a / b
    except ZeroDivisionError:
        result_div = None
    finally:
        print('Inside result_div: {}'.format(result_div))
        return result_div
