#!/usr/bin/python3
"""Module for text indentation."""


def text_indentation(text):
    """Prints text with correct indentation, ensuring two new
       lines after each period".",question mark"?", or colon":".

    Args:
        text (str): The text to be printed with proper indentation.

    Raises:
        TypeError: If `text` is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    char = 0
    while char < len(text) and text[char] == ' ':
        c += 1

    while char < len(text):
        print(text[char], end="")
        if text[char] == "\n" or text[char] in ".?:":
            if text[char] in ".?:":
                print("\n")
            char += 1
            while char < len(text) and text[char] == ' ':
                char += 1
            continue
        char += 1
