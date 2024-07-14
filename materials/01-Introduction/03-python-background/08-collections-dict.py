"""
This script demonstrates the use of Dictionaries in Python.
"""

# A dictionary is a collection of key-value pairs. Each key is associated with a value.
# Dictionaries are unordered and mutable.
# A Dictionary can be conceptualized a set which each element in the set
# (the keys) mapped to some other variable (the value).
# Keys are unique within a dictionary, but values are not.

# For exmaple, A dictionary may be used to map people address.
# Many people can have the same address, but each person can only have one address.
# Dictionary can be created like so:
address_map = {
    "Alice": "1234 Main St",
    "Bob": "5678 Elm St",
    "Charlie": "91011 Oak St",
    "Mollu" : "1234 Main St",
}

# Dictionaries can be accessed using the key.
print(address_map["Alice"]) # 1234 Main

# Dictionaries can be modified by assigning a value to a key.
address_map["Alice"] = "1234 Elm St" # Change Alice's address.

# Dictionaries can be added to by assigning a value to a new key.
address_map["David"] = "91011 Oak St" # Add David's address.

# Keys in a dictionary be iterated over using a for loop.
for key in address_map:
    print(key, address_map[key]) # Print each key-value pair.
