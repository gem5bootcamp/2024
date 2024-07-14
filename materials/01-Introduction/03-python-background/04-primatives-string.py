"""
This script demonstrates the use of strings as a primative data type in
Python.
"""

# Strings are a primative data type in Python. They are sequences of characters
# and are declared like so. Here we declare a variable `x` and assign it the
# literal value `"Hello World!"`.

x = "Hello World!"
print(x)

# There are numerous operations that can be performed on strings. A more
# complete list can be found here:
# https://www.pythonforbeginners.com/basics/string-manipulation-in-python.
# Below are a few common examples.

# Concatenation of two strings
# Note the use of the a literal string ("GoodBye!") and the variable `x`.
y = x + " GoodBye!"
print(y)

# We use the "f-string" syntax to insert the value strings inside other
# strings. The contents between the curly braces are evaluated as Python.
# In the follwoing we concatinate x with " GoodBye " and the value of x + y
# ("Hello World! GoodBye!"). This z will be set to
# "Hello World! GoodBye Hello World! Goodbye!"
z = f"{x} GoodBye {x + y}"
print(z)

