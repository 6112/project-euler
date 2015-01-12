# encoding=utf-8
## SOLVED 2014/12/01
## 303963552391

# Consider the fraction, n/d, where n and d are positive integers. If n<d and
# HCF(n,d)=1, it is called a reduced proper fraction.

# If we list the set of reduced proper fractions for d ≤ 8 in ascending order
# of size, we get:

# 1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3,
# 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

# It can be seen that there are 21 elements in this set.

# How many elements would be contained in the set of reduced proper fractions
# for d ≤ 1,000,000?

from math import sqrt

from helpers.prime import generate_primes, primes
from helpers.totient import *

def euler():
    MAX = 10 ** 6
    # at the end, this table will contain all the values for totients
    table = list(range(MAX + 1))
    match_count = 0
    # there are totient(p) reduced fracions for each denominator p
    for p in range(2, MAX + 1):
        if table[p] == p:
            # this number is prime: multiply each of is multiples by (1 - 1 / p)
            for q in range(p, MAX + 1, p):
                table[q] *= 1 - 1 /  p
        # add totient(p) to the number of matches
        match_count += table[p]
    # return the number of matches, as an integer
    return round(match_count)
