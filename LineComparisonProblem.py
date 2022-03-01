import math


def compare_to():  # function to take input and compute the length of the line
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
    print()
    
    comp = int((res1 - res2))
    if res1 == res2:
        print(comp)
    elif res1 > res2:               # Comparison
        print(comp)
    else:
        print(comp)


# Driver Code
if __name__ == '__main__':
    compare_to()  # function calling
