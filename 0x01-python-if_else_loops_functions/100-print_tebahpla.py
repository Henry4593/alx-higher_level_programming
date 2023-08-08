#!/usr/bin/python3
final_str = ""
ascii_no = ord("z")
upper_on = False
while ascii_no >= ord("a") and ascii_no >= ord("A"):
	if upper_on:
		ascii_no -= 32
		final_str += chr(ascii_no)
		ascii_no += 31
		upper_on = False
	else:
		final_str += chr(ascii_no)
		ascii_no -= 1
		upper_on = True
print(final_str, end='')
