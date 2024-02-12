#!/usr/bin/python3
""" 1-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    rect_1 = Rectangle(10, 2)
    print(rect_1.id)

    rect_2 = Rectangle(2, 10)
    print(rect_2.id)

    r3 = Rectangle(10, 2, 0, 0, 12)
    print(r3.id)
