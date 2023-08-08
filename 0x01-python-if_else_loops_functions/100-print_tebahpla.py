#!/usr/bin/python3
for idx_str in reversed(range(97, 123)):
    if (idx_str % 2 == 0):
        print(chr(idx_str), end='')
    else:
        print(chr(idx_str - 32), end='')
