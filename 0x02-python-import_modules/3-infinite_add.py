#!/usr/bin/python3

if __name__ == '__main__':
    from sys import argv
    length = len(argv) - 1
    sum_result = 0
    if length == 0:
        print("{}".format(sum_result))
    else:
        for arg in argv[1:]:
            sum_result += int(arg)
        print("{}".format(sum_result))
