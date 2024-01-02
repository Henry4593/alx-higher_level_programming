#!/usr/bin/python3
import random
gen_num = random.randint(-10, 10)
number = gen_num
if number == 0:
	print("{0:d} is zero".format(number))
elif number > 0:
	print("{0:d} is positive".format(number))
else:
	print("{0:d} is negative".format(number))
