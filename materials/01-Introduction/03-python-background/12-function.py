"""
This script demonstrates how declare and use function Python.
In edition the user Python typing is demonstrated and encouraged when
developing gem5.
"""

# Functions in Python are declared using the def keyword.
# The have name and can take aruguments to perform operations on and return
# a value using the `return` keyword.
# The following function takes two arguments and returns their sum.
def add(a, b):
    return a + b

# To call a function in Python, you simply use the function name followed by
# the arguments in parentheses.
result = add(5, 3)

# Note: In files like this the function must be declared _before_ it is called.
# This is because Python is an interpreted language and the code is executed
# from top to bottom.

# The Python typing module can be used to specify the types of arguments and
# return values for functions. This can help with code readability and
# maintainability.
# The following function is the same as the previous one, but with type hints.
# The `Union` type is used to specify that the argument can be either an int
# or a float. `a: Union[int, float]` means that `a` can be either an int or a
# float. The return type is also specified as a `Union` of int and float.
# This means that the function can return either an int or a float.
from typing import Union

def add_typed(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    return a + b

# Typing is not enforced in Python, but it can be used to help catch errors
# early and make code more readable. We strongly encourage their in functions.

# Functions can call other functions, and even themselves. This is called
# recursion. The following function demonstrates recursion by calculating the
# factorial of a number.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# The following code will print the factorial of 5, which is 120.
result = factorial(5)
print(f"Factorial of 5: {result}")

