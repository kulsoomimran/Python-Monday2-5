# --- MODULE USAGE ---

import math
print("Square root of 16 is", math.sqrt(16))

from math import pi
print("Value of pi:", pi)

# FUNCTION DEFINITION AND CALLING
def greet(name):
    print(f"Hello, {name}!")
greet("Sara")

# FUNCTION WITH RETURN STATEMENT
def add(a, b):
    return a + b
result = add(5, 3)
print("Result: ",result)

# FUNCTION WITH DEFAULT ARGUMENTS
def greet(name, title="Mr."):
    print(f"Hello, {title} {name}!")
greet("Ali")
greet("Sara", "Ms.")

# FUNCTION WITH KEYWORD ARGUMENTS
def calculate_area(length, width):
    return length * width

area = calculate_area (width=5, length=10)
print("Area of the rectangle is", area)

# ANONYMOUS FUNCTIONS (LAMBDAS)
square = lambda x: x * x
print("Square of 5 is", square(5))



