#!/usr/bin/python3
def uppercase(str):
    final_str = ""
    for idx_str in range(len(str)):
        if (ord(str[idx_str]) >= 97 and ord(str[idx_str]) <= 122):
            final_str += chr(ord(str[idx_str]) - 32)
            continue
        final_str += str[idx_str]

    print('{0}'.format(final_str))
