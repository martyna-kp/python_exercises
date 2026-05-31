# Given a year, return the century it is in.

# Solution 1: Using math.ceil
import math
def century(year):
    return math.ceil(year / 100)

# Solution 2: Using integer division without math.ceil
def century(year):
    return (year + 99) // 100