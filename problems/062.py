# encoding=utf-8
## SOLVED 18/11/14
## 127035954683

from modules.sequence import is_permutation
from math import ceil

def euler():
    for n in range(346, 6000):
        cube_permutations = 0
        digits = str(n * n * n)
        maximum = maximum_for(digits)
        for m in range(n, maximum):
            cube = m * m * m
            if is_permutation(str(cube), digits):
                cube_permutations += 1
        if cube_permutations == 5:
            return n ** 3

# calculate the highest possible value for the cube root of a permutation of
# the given digits
def maximum_for(digits):
    xs = reversed(sorted(digits))
    return ceil(int("".join(xs)) ** (1 / 3))
