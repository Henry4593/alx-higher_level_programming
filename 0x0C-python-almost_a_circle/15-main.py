#!/usr/bin/python3
""" 15-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    rect_1 = Rectangle(10, 7, 2, 8)
    rect_2 = Rectangle(2, 4)
    Rectangle.save_to_file([rect_1, rect_2])

    with open("Rectangle.json", "rect") as file:
        print(file.read())
