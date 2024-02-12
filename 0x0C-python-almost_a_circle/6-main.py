#!/usr/bin/python3
""" 6-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    rect_1 = Rectangle(2, 3, 2, 2)
    rect_1.display()

    print("---")

    rect_2 = Rectangle(3, 2, 1, 0)
    rect_2.display()
