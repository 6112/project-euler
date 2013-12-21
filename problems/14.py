## SOLVED 20/12/13
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

from modules.prime import *

MAX_VALUE = 1000000

def euler ():
    return max ((collatz (n), n) for n in range (1, MAX_VALUE)) [1]

collatz_dictionary = {1: 1}
def collatz (number):
    if number in collatz_dictionary:
        return collatz_dictionary [number]
    elif number % 2 == 0:
        result = 1 + collatz (number // 2)
    else:
        result = 1 + collatz (number * 3 + 1)
    collatz_dictionary [number] = result
    return result
