#!/usr/bin/python3

if __name__ == '__main__':
    from sys import argv
    from sys import exit
    from calculator_1 import add
    from calculator_1 import div
    from calculator_1 import mul
    from calculator_1 import sub

    result = 0
    length = 0
    operator_list = ["+", "-", "*", "/"]

    for idx_argv in argv[1:]:
        length += 1
    if length != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        if argv[2] not in operator_list:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
        else:
            if argv[2] == "+":
                print("{} + {} = {}".format(argv[1], argv[3],
                      add(int(argv[1]), int(argv[3]))))
            elif argv[2] == "*":
                print("{} * {} = {}".format(argv[1], argv[3],
                      mul(int(argv[1]), int(argv[3]))))
            elif argv[2] == "/":
                if (int(argv[3]) != 0):
                    print("{} / {} = {}".format(argv[1], argv[3],
                          div(int(argv[1]), int(argv[3]))))
                else:
                    exit(1)
            else:
                print("{} - {} = {}".format(argv[1], argv[3],
                      sub(int(argv[1]), int(argv[3]))))
