# encoding=utf-8
## SOLVED 2013/12/23
## 2783915460

# A permutation is an ordered arrangement of objects. For example, 3124 is one
# possible permutation of the digits 1, 2, 3 and 4. If all of the permutations
# are listed numerically or alphabetically, we call it lexicographic order. The
# lexicographic permutations of 0, 1 and 2 are:

# 012   021   102   120   201   210

# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4,
# 5, 6, 7, 8 and 9?

import helpers.sequence as sequence

ANSWER_INDEX = 1000000

def euler():
    # list of digits
    tokens = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    # current permutation counter
    index = 0
    # for each permutation of the digits
    for permutation in sequence.permutations(tokens):
        index += 1
        # if the permutation is the one we want
        if index == ANSWER_INDEX:
            # return it, as a string
            return ''.join(map(str, permutation))
