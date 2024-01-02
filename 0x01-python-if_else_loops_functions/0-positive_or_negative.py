#!/usr/bin/python3
import random
number = random.randint(-10, 10)
gen_num = number
if gen_num == 0:
    print("{0:d} is zero".format(gen_num))
elif gen_num > 0:
    print("{0:d} is positive".format(gen_num))
else:
    print("{0:d} is negative".format(gen_num))
