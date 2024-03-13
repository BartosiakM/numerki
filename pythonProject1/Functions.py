import math


def polynomial(x, coefficients, degree):
    power = 0
    result = 0
    while power <= degree:
        result = coefficients[power] + x * result
        power += 1
    return result


def exponential(x, base):
    result = 1
    for i in range(base):
        result *= x
    return result


def sin(x):
    return math.sin(x)

def cos(x):
    return math.cos(x)

def tan(x):
    return math.tan(x)

def ctan(x):
    return math.atan(x)

def complex(f1, f2, x):
    return f1(f2(x))