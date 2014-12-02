# encoding=utf-8
## SOLVED 25/12/13
## 55

# The number, 197, is called a circular prime because all rotations of the
# digits: 197, 971, and 719, are themselves prime.

# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71,
# 73, 79, and 97.

# How many circular primes are there below one million?

from helpers.prime import *
from helpers.sequence import *

import bisect

HIGHEST_VALUE = 1000000

def euler ():
    accumulator = 0
    for prime in primes (HIGHEST_VALUE):
        if is_circular (prime):
            accumulator += 1
    return accumulator

circular_cache = {}
def is_circular (prime):
    if prime in circular_cache:
        return circular_cache [prime]
    for rotation in rotations (str (prime)):
        if not is_prime (int (''.join (rotation))):
            return False
    for rotation in rotations (str (prime)):
        circular_cache [int (''.join (rotation))] = True
    return True
