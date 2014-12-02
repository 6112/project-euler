# encoding=utf-8
## SOLVED 19/12/13
## 6857

# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

import helpers.prime as prime

BIG_NUMBER = 600851475143

def euler ():
    # compute the prime factors of the big number
    factors = prime.prime_factors (BIG_NUMBER)
    # return the highest of the prime factors
    return max (factors)
