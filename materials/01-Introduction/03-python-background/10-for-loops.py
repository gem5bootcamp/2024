"""
This script demonstrates the use of for loops in Python.
"""

# For loops are used to iterate over a sequence of elements.
# This are useful for iterating through collections such as lists, sets and
# dictionaries.

# For example, we can iterate over a list of numbers and print each number.
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number)

# `break` can be used to exit the loop early.
for number in numbers:
    if number == 3:
        break # Exit the loop and cease iteration early.
    print(number)

# `continue` can be used to skip the rest of the current iteration and move to
# the next one.
for number in numbers:
    if number == 3:
        continue # Skip the rest of the iteration and move to the next one.
    print(number)
