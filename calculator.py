"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

# First example
import math
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b / a

def log(a, b):
    if b <= 1 or a <= 0:
        raise ValueError
    return  math.log(b, a)

def exp(a, b):
    return a**b

def square_root(a):
    if a < 0:
        raise ValueError("sqrt must be positive")
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b) # can have negative nums