#!/usr/bin/python3
def print_last_digit(number):
    last_digit = None
    if number == 0:
        last_digit = 0
    elif number < 0:
        abs_num = -(number)
        last_digit = abs_num % 10
    else:
        last_digit = number % 10
    print(last_digit, end='')
    return last_digit
