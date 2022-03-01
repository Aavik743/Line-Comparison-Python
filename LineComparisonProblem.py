import math


def line_length():
    x1 = 2
    y1 = 3
    x2 = 4
    y2 = 5

    res = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
    print("\nThe required length is", res)


# Driver Code
if __name__ == '__main__':
    line_length()
