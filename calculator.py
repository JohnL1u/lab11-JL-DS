"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

# First example
import math
def add(a, b): a + b

def sub(a, b): a - b

def mul(a, b): a * b

def div(a, b):  b / a
    if a == 0:
        raise ZeroDivisionError

def log(a, b): math.log(b, a)
    if b <= 1 or a <= 0:
        raise ValueError

def exp(a, b): a ** b


import math

def square_root(a):
    if a < 0:
        raise ValueError("sqrt must be positive")
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b) # can have negative nums

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def log(a, b):
    if a <= 0:
        raise ValueError("log base must be positive")
    if a == 1:
        raise ValueError("log base cannot be 1")
    if b <= 0:
        raise ValueError("log argument must be positive")
    return math.log(b, a)

def exp(a, b):
    return a ** b