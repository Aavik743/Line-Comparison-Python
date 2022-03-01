import math


def check_equality():  # function to take input and compute the length of the line
    x1 = 2  # input
    y1 = 3  # input
    x2 = 4  # input
    y2 = 9  # input

    res1 = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))  # computation
    print("\nThe required length is:", res1)

    p1 = 2  # input
    q1 = 5  # input
    p2 = 4  # input
    q2 = 7  # input

    res2 = math.sqrt(((p2 - p1) ** 2) + ((q2 - q1) ** 2))  # computation
    print("\nThe required length is:", res2)

    if res1 == res2:
        print("Lines are equal")
    elif res1 > res2:
        print("First line is longer")
    else:
        print("Second line is longer")


# Driver Code
if __name__ == '__main__':
    check_equality()  # function calling
