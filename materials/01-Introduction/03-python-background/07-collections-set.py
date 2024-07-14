"""
This script demonstrates the use of Sets in Python.
"""

# A set is an unordered collection of unique elements.
# A set can be created by using curly braces.
x = {1, 2, 3, 4, 5}


# Sets are also mutable so you can add and remove elements.
x.add(6)
print(x) # {1, 2, 3, 4, 5, 6}
x.remove(6) # {1, 2, 3, 4, 5}

# Adding a duplicate element will not change the set.
x.add(5)
print(x) # {1, 2, 3, 4, 5}

# Sets can be compared against others using set operations.
y = {4, 5, 6, 7, 8}
print(x & y) # {4, 5}
print(x | y) # {1, 2, 3, 4, 5, 6, 7, 8}
print(x - y) # {1, 2, 3}
print(x ^ y) # {1, 2, 3, 6, 7, 8}

# Elements in a set can only be accesesd via iteration as they are indexed and
# ordered like lists are.
for i in x:
    print(i)

# You can also quickly check if an element exists in a set.
print(1 in x) # True

