#!/usr/bin/python3
final_str = ""
for idx_str in reversed(range(97, 123)):
    if (idx_str % 2 == 0):
        final_str += chr(idx_str)
    else:
        final_str += chr(idx_str - 32)
print(final_str, end='')
