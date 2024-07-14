"""
This script demonstrates the use of bools as a primative data type in
Python.
"""

# Bools are a primative data type in Python. They are "True" or "False" and are
# declared like so. Here we declare a variable `x` and assign it the literal
# value `True`.
x = True
print(f"Value of x: {x}")

# Bools can be set using logical operations of literals or other bool
# variables. These logical operations are `is` `and`, `or`, and `not` and are used
# to comapre values

# Set `y`` to True if  `x and True`.
y = x and True
print(f"Value of y: {y}")

# Set `z`` to True if `x or False`.
z = x or False
print(f"Value of z: {z}")

# Set `a`` to True if `not x`.
a = not x
print(f"Value of a: {a}")

# The ==, !=, <, >, <=, and >= operators can be used to compare values of other
# primative data types. The result of these operations is a bool.

# Set `b` to True if `1 + 1` is equal to `2`.
b = (1 + 1) == 2
print(f"Value of b: {b}")

# Set `c` to True if `1 + 1` is not equal to `2`.
c = (1 + 1) != 2
print(f"Value of c: {c}")

# Set `d` to True if `1 + 1` is less than `3`.
d = (1 + 1) < 3
print(f"Value of d: {d}")

# Set `e` to True if `1 + 1` is greater than `3`.
e = (1 + 1) > 3
print(f"Value of e: {e}")

# Set `f` to True if `1 + 1` is less than or equal to `2`.
f = (1 + 1) <= 2

# Set `g` to True if `1 + 1` is greater than or equal to `2`.
g = (1 + 1) >= 2
