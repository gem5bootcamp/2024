"""
This script demonstrates the use of Lists in Python.
"""

# A list is a collection of items that a particular order. Items in a list can
# be of any type and duplicates are permitted.
# Here we create a lost of integers
numbers = [1, 2, 3, 4, 5]

# Lists are _mutable_, meaning that you can change the contents of a list after
# it has been created. Here we can appenda value to the of the list
numbers.append(6)
print(numbers) # [1, 2, 3, 4, 5, 6]

# Lists can be accessed by index. The first element of a list is at index 0.
print(numbers[0]) # 1

# You can overwrite the value of a list element by assigning a new value to the
# index.
numbers[0] = 100

# You can iterate through the list, in order, through a `for` loop.
for number in numbers:
    print(number) # 100\n 2\n 3\n 4\n 5\n 6
