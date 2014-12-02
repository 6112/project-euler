# encoding=utf-8
## SOLVED 18/11/14
## 127035954683

# The cube, 41063625 (3453), can be permuted to produce two other cubes:
# 56623104 (3843) and 66430125 (4053). In fact, 41063625 is the smallest cube
# which has exactly three permutations of its digits which are also cube.

# Find the smallest cube for which exactly five permutations of its digits are
# cube.

from helpers.sequence import is_permutation
from math import ceil

def euler():
    for n in range(346, 6000):
        # number of cubes that are permutations of n^3
        cube_permutations = 0
        digits = str(n * n * n)
        maximum = maximum_for(digits)
        # for each number from n to maximum (see maximum_for()), check if its
        # cube is a permutation of n
        for m in range(n, maximum):
            cube = m * m * m
            if is_permutation(str(cube), digits):
                cube_permutations += 1
        # return it if it has the right number of permutations
        if cube_permutations == 5:
            return n ** 3

# calculate the highest possible value for the cube root of a permutation of
# the given digits
def maximum_for(digits):
    xs = reversed(sorted(digits))
    return ceil(int("".join(xs)) ** (1 / 3))
