"""
This script demonstrates hwo code can be imported from other Python files.
"""

# Code can be import from other Python files using the import statement.
#  There's a file called "math_funcs.py" in "toimport" directory.
# This file four functions that perform basic math operations: `add`,
# `subtract`, `multiply`, and `divide`.

# To use these functions in this script, we can import them using the import
# statement. The format we are using `from <moduel_name> import <function_name>`
# Note a module is a file containing Python code.

from .toimport.math_funcs import add, subtract, multiply, divide

# In the above import statement, we are importing the functions `add`, `subtract`,
# `multiply`, and `divide` from the module `math_funcs` in the package `toimport`.
# The `from` keyword is used to specify the module name and the `import` keyword
# is used to specify the function names. The functions are separated by commas.
# The module starts with a dot `.` which means that the module is in the same


# Now we can use the functions in this script.

print(add(1, 2))
print(subtract(1, 2))
print(multiply(1, 2))
print(divide(1, 2))

