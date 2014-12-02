# encoding=utf-8
## SOLVED 01/12/14
## 8319823

# Euler's Totient function, φ(n) [sometimes called the phi function], is used
# to determine the number of positive numbers less than or equal to n which are
# relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less
# than nine and relatively prime to nine, φ(9)=6.

# The number 1 is considered to be relatively prime to every positive number,
# so φ(1)=1.

# Interestingly, φ(87109)=79180, and it can be seen that 87109 is a permutation
# of 79180.

# Find the value of n, 1 < n < 10**7, for which φ(n) is a permutation of n and
# the ratio n/φ(n) produces a minimum.

from helpers.prime import *
from helpers.sequence import *

from math import sqrt, ceil

HIGHEST_N = 10 ** 7

def euler():
    middle = ceil(sqrt(HIGHEST_N))
    for p in range(middle, 0, -1):
        if is_prime(p):
            for q in range(middle + 1, ceil((10 ** 7) / p)):
                if is_prime(q):
                    n = p * q
                    t = totient(n)
                    if is_permutation(str(n), str(t)):
                        return n

def totient(n):
    t = n
    for p in set(prime_factors(t)):
        t *= 1 - 1 / p
    return round(t)
