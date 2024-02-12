#!/usr/bin/python3
""" 13-main """
from models.square import Square

if __name__ == "__main__":

    sqr_1 = Square(10, 2, 1)
    print(sqr_1)
    sqr_1_dictionary = sqr_1.to_dictionary()
    print(sqr_1_dictionary)
    print(type(sqr_1_dictionary))

    sqr_2 = Square(1, 1)
    print(sqr_2)
    sqr_2.update(**sqr_1_dictionary)
    print(sqr_2)
    print(sqr_1 == sqr_2)
