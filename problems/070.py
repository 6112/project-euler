# encoding=utf-8
## SOLVED 2014/12/01
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

import helpers.sequence as sequence
import helpers.prime as prime
import helpers.discreet as discreet

import math

HIGHEST_N = 10 ** 7

def euler():
    middle = math.ceil(math.sqrt(HIGHEST_N))
    for p in range(middle, 0, -1):
        if prime.is_prime(p):
            for q in range(middle + 1, math.ceil((10 ** 7) / p)):
                if prime.is_prime(q):
                    n = p * q
                    t = discreet.totient(n)
                    if sequence.is_permutation(str(n), str(t)):
                        return n
