#!/usr/bin/python3
""" 10-main """
from models.square import Square

if __name__ == "__main__":

    sqr_1 = Square(5)
    print(sqr_1)
    print(sqr_1.size)
    sqr_1.size = 10
    print(sqr_1)

    try:
        sqr_1.size = "9"
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
