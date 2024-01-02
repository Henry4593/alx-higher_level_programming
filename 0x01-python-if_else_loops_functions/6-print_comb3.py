#!/usr/bin/python3
for tens_digit in range(10):
    for ones_digit in range(10):
        if (tens_digit != ones_digit and tens_digit < ones_digit)\
           and tens_digit < 9:
            if (tens_digit == 8 and ones_digit == 9):
                print('{0}{1}'.format(tens_digit, ones_digit))
            else:
                print('{0}{1}, '.format(tens_digit, ones_digit), end='')
