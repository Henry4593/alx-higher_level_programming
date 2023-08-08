#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
gen_number = number
str = "Last digit of"

if gen_number < 0:
    abs_num = -(gen_number)
    last_digit = -(abs_num % 10)
    if (abs_num % 10) == 0:
        last_digit == 0
        print(f"{str} {gen_number} is {last_digit} and is 0")
    else:
        print(f"{str} {gen_number} is {last_digit} and is less than 6"
              " and not 0")
else:
    last_digit = gen_number % 10
    if last_digit > 5:
        print(f"{str} {gen_number} is {last_digit} and is greater than 5")
    elif last_digit == 0:
        print(f"{str} {gen_number} is {last_digit} and is 0")
    else:
        print(f"{str} {gen_number} is {last_digit} and is less"
              " than 6 and not 0")
