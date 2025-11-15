# -----------------------------------------------------------------------
# 1. math module
# -----------------------------------------------------------------------
# import math
from math import factorial, pi, sqrt

print("Square root of 16 is:", sqrt(16))
print("Pi value:", pi)
print("5! =", factorial(5))
print("-" * 50)


# -----------------------------------------------------------------------
# 2. random module
# -----------------------------------------------------------------------
# import random
from random import choice, randint

print("Random number between 1-10:", randint(1, 10))
print("Random choice from list:", choice(["apple", "banana", "cherry"]))
print("-" * 50)


# -----------------------------------------------------------------------
# 3. datetime module
# -----------------------------------------------------------------------
# import datetime
from datetime import date

today = date.today()
print("Today's date:", today)
print("Current month:", today.month)
print("Current year:", today.year)
print("-" * 50)
