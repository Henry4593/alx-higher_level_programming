#!/usr/bin/python3

def multiple_returns(sentence):
    length = 0
    first_char = sentence[0]
    if sentence == "":
        first_char = None
        return (length, first_char)
    else:
        if first_char is None:
            first_char = None
        length = len(sentence)
    return (length, first_char)
