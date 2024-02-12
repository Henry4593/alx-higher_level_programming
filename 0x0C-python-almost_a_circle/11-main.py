#!/usr/bin/python3
""" 11-main """
from models.square import Square

if __name__ == "__main__":

    sqr_1 = Square(5)
    print(sqr_1)

    sqr_1.update(10)
    print(sqr_1)

    sqr_1.update(1, 2)
    print(sqr_1)

    sqr_1.update(1, 2, 3)
    print(sqr_1)

    sqr_1.update(1, 2, 3, 4)
    print(sqr_1)

    sqr_1.update(x=12)
    print(sqr_1)

    sqr_1.update(size=7, y=1)
    print(sqr_1)

    sqr_1.update(size=7, id=89, y=1)
    print(sqr_1)
