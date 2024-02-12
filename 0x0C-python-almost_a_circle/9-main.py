#!/usr/bin/python3
""" 9-main """
from models.square import Square

if __name__ == "__main__":

    sqr_1 = Square(5)
    print(sqr_1)
    print(sqr_1.area())
    sqr_1.display()

    print("---")

    sqr_2 = Square(2, 2)
    print(sqr_2)
    print(sqr_2.area())
    sqr_2.display()

    print("---")

    s3 = Square(3, 1, 3)
    print(s3)
    print(s3.area())
    s3.display()
