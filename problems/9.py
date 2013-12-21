#!/usr/bin/python3
## SOLVED 19/12/13
## 31875000


# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a2 + b2 = c2

# For example, 32 + 42 = 9 + 16 = 25 = 52.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

from math import sqrt

TARGET_VALUE = 1000

def euler ():
    for a in range (1, 1000):
        for b in range (1, 1000):
            c = sqrt (a * a + b * b)
            if c == int (c) and a + b + c == TARGET_VALUE:
                return a * b * int (c)
