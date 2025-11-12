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



