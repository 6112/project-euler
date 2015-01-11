# encoding=utf-8
## SOLVED 2013/12/20
## 837799

# The following iterative sequence is defined for the set of positive integers:

# n -> n/2 (n is even)
# n -> 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:

# 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

# It can be seen that this sequence (starting at 13 and finishing at 1) contains
# 10 terms. Although it has not been proved yet (Collatz Problem), it is thought
# that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?

# NOTE: Once the chain starts the terms are allowed to go above one million.

import helpers.prime as prime

MAX = 1000000

def euler ():
    # return the number that generates the longest collatz sequence
    return max ((collatz (n), n) for n in range (1, MAX)) [1]

# use a dictionary to optimize the collatz sequence
collatz_cache = {1: 1}
def collatz (number):
    """Return the length of the collatz sequence starting at a given number."""
    # use cache if possible
    if number in collatz_cache:
        return collatz_cache [number]
    # compute the result using recursion
    if number % 2 == 0:
        result = 1 + collatz (number // 2)
    else:
        result = 1 + collatz (number * 3 + 1)
    # set it in the cache
    collatz_cache [number] = result
    # return the result
    return result
