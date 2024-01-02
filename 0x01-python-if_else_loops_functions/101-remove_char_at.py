#!/usr/bin/python3
def remove_char_at(str, n):

    final_str = ""

    for idx in range(len(str)):
        if idx != n:
            final_str += str[idx]

    return final_str
