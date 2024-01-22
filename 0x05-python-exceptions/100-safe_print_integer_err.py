#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print('{:d}'.format(value))
        return True
    except ValueError as val_err:
        sys.stderr.write("Exception: " + str(val_err) + "\n")
        return False
    except TypeError as type_err:
        sys.stderr.write("Exception: " + str(type_err) + "\n")
        return False
