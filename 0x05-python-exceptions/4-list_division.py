#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    final_list = []

    for idx in range(list_length):
        try:
            final_list.append(my_list_1[idx] / my_list_2[idx])
        except ZeroDivisionError:
            final_list.append(0)
            print('division by 0')
            continue
        except IndexError:
            final_list.append(0)
            print('out of range')
            continue
        except TypeError:
            final_list.append(0)
            print('wrong type')
            continue
        finally:
            pass

    return final_list
