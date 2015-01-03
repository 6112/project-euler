# encoding=utf-8
## SOLVED 2013/12/19
## 31875000

# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a^2 + b^2 = c^2

# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

import math

TARGET_VALUE = 1000

def euler ():
    # for each (a, b) pair
    for a in range (1, TARGET_VALUE):
        for b in range (1, TARGET_VALUE):
            # calculate c
            c = math.sqrt (a * a + b * b)
            # return if the pair satisfies a+b+c=1000 and c is natural
            if c == int (c) and a + b + c == TARGET_VALUE:
                return a * b * int (c)
