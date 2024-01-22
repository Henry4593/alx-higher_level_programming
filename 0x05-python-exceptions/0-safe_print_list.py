#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    idx_x = 0

    try:
        for _ in my_list:
            if idx_x < x:
                print('{}'.format(my_list[idx_x]), end='')
                idx_x += 1

        print()
    except TypeError:
        pass
    finally:
        return idx_x
