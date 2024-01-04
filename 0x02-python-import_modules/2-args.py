#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    length = 0
    for arg in argv[1:]:
        length += 1
    if length == 0:
        print("0 arguments.")
    elif length == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(length))
    for idx_arg, arg in enumerate(argv[1:]):
        print("{0}: {1}".format(idx_arg + 1, arg))
