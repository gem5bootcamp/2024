
# Importing the Union class from the typing module
# The `typing` module is a module in the Python standard library which is
# included with Python and can imported directly like this.
from typing import Union


def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    return a + b

def subtract(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    return a - b

def multiply(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    return a * b

def divide(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    return a / b
