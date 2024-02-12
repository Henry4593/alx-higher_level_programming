#!/usr/bin/python3
""" 12-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    rect_1 = Rectangle(10, 2, 1, 9)
    print(rect_1)
    rect_1_dictionary = rect_1.to_dictionary()
    print(rect_1_dictionary)
    print(type(rect_1_dictionary))

    rect_2 = Rectangle(1, 1)
    print(rect_2)
    rect_2.update(**rect_1_dictionary)
    print(rect_2)
    print(rect_1 == rect_2)
