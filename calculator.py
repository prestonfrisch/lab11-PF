# https://github.com/prestonfrisch/lab11-PF.git
# Partner 1: Preston Frisch

import math

def square_root(a):
    if a < 0:
        raise ValueError("Cannot take square root of negative number")
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b     # sample expects a/b, not b/a

def logarithm(a, b):
    if a <= 0 or b <= 0:
        raise ValueError("Logarithm arguments must be positive")
    return math.log(b, a)

def exponent(a, b):
    return a ** b
