#!/usr/bin/python3
""" 17-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    rect_1 = Rectangle(3, 5, 1)
    rect_1_dictionary = rect_1.to_dictionary()
    rect_2 = Rectangle.create(**rect_1_dictionary)
    print(rect_1)
    print(rect_2)
    print(rect_1 is rect_2)
    print(rect_1 == rect_2)
