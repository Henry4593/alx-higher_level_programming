#!/usr/bin/python3
""" 8-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    rect_1 = Rectangle(10, 10, 10, 10)
    print(rect_1)

    rect_1.update(height=1)
    print(rect_1)

    rect_1.update(width=1, x=2)
    print(rect_1)

    rect_1.update(y=1, width=2, x=3, id=89)
    print(rect_1)

    rect_1.update(x=1, height=2, y=3, width=4)
    print(rect_1)
