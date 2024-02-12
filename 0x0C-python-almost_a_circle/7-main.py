#!/usr/bin/python3
""" Doc """
from models.rectangle import Rectangle

if __name__ == "__main__":

    rect_1 = Rectangle(10, 10, 10, 10)
    print(rect_1)

    rect_1.update(89)
    print(rect_1)

    rect_1.update(89, 2)
    print(rect_1)

    rect_1.update(89, 2, 3)
    print(rect_1)

    rect_1.update(89, 2, 3, 4)
    print(rect_1)

    rect_1.update(89, 2, 3, 4, 5)
    print(rect_1)
