"""
This script demonstrates the use of if statements in Python.
"""

x = 5

# Check if x is greater than 5
# If so then the code block will be executed. The code block is indented code
# directly below the if statement.
# Python uses indentation to define code blocks, so be careful with your
# indentation.
if x > 5:
    print("x is greater than 5")

# If-else statements can be be used to do something if the condition is not
# met.
if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")

# If-elif-else statements can be used to check multiple conditions.
if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than 5")

# You can also nest if statements.
# Not the nested indentation.
if x > 5:
    if x == 6:
        print("x is equal to 6")
    else:
        print("x is greater than 5 but not equal to 6")


