import math

def myfunc(x):
    return math.cos(math.pi/x)

def funcx2(x):
    return x*x

def counting_withinrange(row, minimum, maximum):
    """Returns how many numbers lie within `maximum` and `minimum` in a given `row`"""
    count = 0
    for n in row:
        if minimum <= n <= maximum:
            count = count + 1
    return count

# We change the function, such we have only ONE parameter.
def counting_withinrange1(row, minimum=4, maximum=8):
    count = 0
    for n in row:
        if minimum <= n <= maximum:
            count = count + 1
    return count
