# -----------------------------------------------------------------------
# 1. import the entire module
# -----------------------------------------------------------------------
# import my_module

# print(my_module.app_name)
# print(my_module.greet("Yash"))
# print("Addition:", my_module.add(10, 5))

# calc = my_module.Calculator()
# print("Multiplication:", calc.multiply(4, 3))


# -----------------------------------------------------------------------
# 2. import the entire module and use alias
# -----------------------------------------------------------------------
# import my_module as m

# print(m.app_name)
# print(m.greet("Yash"))
# print("Addition:", m.add(10, 5))

# calc = m.Calculator()
# print("Multiplication:", calc.multiply(4, 3))


# -----------------------------------------------------------------------
# 3. import required variable, functions and classes
# -----------------------------------------------------------------------
# from my_module import Calculator, add, app_name, greet

# print(app_name)
# print(greet("Yash"))
# print("Result:", add(3, 7))

# calc = Calculator()
# print("Product:", calc.multiply(5, 6))


# -----------------------------------------------------------------------
# 4. import everything (not recommended)
# -----------------------------------------------------------------------
from my_module import *

print(app_name)
print(greet("Yash"))
print("Result:", add(3, 7))

calc = Calculator()
print("Product:", calc.multiply(5, 6))
