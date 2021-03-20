# encoding=utf-8
## SOLVED 2021/03/20
## 518408346

# It is easily proved that no equilateral triangle exists with integral length
# sides and integral area. However, the almost equilateral triangle 5-5-6 has an
# area of 12 square units.

# We shall define an almost equilateral triangle to be a triangle for which two
# sides are equal and the third differs by no more than one unit.

# Find the sum of the perimeters of all almost equilateral triangles with
# integral side lengths and area and whose perimeters do not exceed one billion
# (1,000,000,000).

import math

MAX = 1000000000

def euler():
    acc = 0
    for m in range(1, math.isqrt(MAX)):
        # Only these 2 values of n might satisfy -1 <= 2*min(a,b)-c <= 1.
        n1 = round(math.sqrt((m * m + 1) / 3))
        n2 = 2*m-round(math.sqrt(12*m*m))//2
        for n in set([n1, n2]):
            # Euclid's formula for generating pythagorean triples.
            a = m * m - n * n
            b = 2 * m * n
            c = m * m + n * n
            a, b = min(a, b), max(a, b)
            p = a * 2 + c * 2
            if p > MAX:
                continue
            if abs(2 * a - c) > 1:
                continue
            acc += p
    return acc
