#!/usr/bin/python3

def roman_to_int(roman_string):
    map_roman_num = {'M': 1000, 'D': 500, 'C': 100, 'L': 50,
                     'X': 10, 'V': 5, 'I': 1}
    idx_roman = 0
    roman_to_num = 0
    if isinstance(roman_string, str):
        for idx_roman in range(len(roman_string) - 1):
            if map_roman_num[roman_string[idx_roman]] >=\
                             map_roman_num[roman_string[idx_roman + 1]]:
                roman_to_num += map_roman_num[roman_string[idx_roman]]
            else:
                roman_to_num -= map_roman_num[roman_string[idx_roman]]
            idx_roman += 1
        roman_to_num += map_roman_num[roman_string[idx_roman]]
        return roman_to_num
    return 0
