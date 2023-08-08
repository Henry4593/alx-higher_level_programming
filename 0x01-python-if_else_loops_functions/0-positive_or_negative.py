#!/usr/bin/python3
import random
number = random.randint(-10, 10)
gen_rdm_number = number
if number == 0:
    print(f"{0:d} is zero".format(gen_rdm_number))
elif number < 0:
    print(f"{0:d} is negative".format(gen_rdm_number))
else:
    print(f"{0:d} is positive".format(gen_rdm_number))
