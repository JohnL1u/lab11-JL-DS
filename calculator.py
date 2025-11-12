"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

import math

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("division by zero: 'a' is 0 in b / a")
    return b / a

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