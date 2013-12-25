# encoding=utf-8
## SOLVED 23/12/13
## 2783915460

# A permutation is an ordered arrangement of objects. For example, 3124 is one
# possible permutation of the digits 1, 2, 3 and 4. If all of the permutations
# are listed numerically or alphabetically, we call it lexicographic order. The
# lexicographic permutations of 0, 1 and 2 are:

# 012   021   102   120   201   210

# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4,
# 5, 6, 7, 8 and 9?

from modules.sequence import *

ANSWER_INDEX = 1000000

def euler ():
    tokens = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    index = 0
    for permutation in permutations (tokens):
        index += 1
        if index == ANSWER_INDEX:
            return ''.join (map (str, permutation))
