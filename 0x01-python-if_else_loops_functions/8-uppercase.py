#!/usr/bin/python3
def uppercase(str):
    final_str = ""
    for char in str:
        if ord(char) >= 97 and ord(char) <= 122:
            char = chr(ord(char) - 32)
            final_str += char
    print("{}".format(final_str))
