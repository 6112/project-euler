#encoding=utf-8
## SOLVED 10/04/14
## 1533776805

# Triangle, pentagonal, and hexagonal numbers are generated by the following
# formulae:

# Triangle        Tn=n(n+1)/2         1, 3, 6, 10, 15, ...
# Pentagonal      Pn=n(3n−1)/2        1, 5, 12, 22, 35, ...
# Hexagonal       Hn=n(2n−1)      1, 6, 15, 28, 45, ...

# It can be verified that T285 = P165 = H143 = 40755.

# Find the next triangle number that is also pentagonal and hexagonal.

import math

def euler():
    n = 144
    while True:
        hexagon = n * (2 * n - 1)
        if is_triangle(hexagon) and is_pentagon(hexagon):
            return hexagon
        n += 1

def is_triangle(n):
    """Return True iff n is a triangle number."""
    x = (-1 + math.sqrt(1 + 8 * n)) / 2
    return x == int(x)

def is_pentagon(n):
    """Return True iff n is a pentagon number."""
    x = (1 + math.sqrt(1 + 24 * n)) / 6
    return x == int(x)

def is_hexagon(n):
    """Return True iff n is a hexagon number."""
    x = (1 + math.sqrt(8 * n)) / 4
    return x == int(x)
