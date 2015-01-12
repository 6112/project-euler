# encoding=utf-8
## SOLVED 2015/01/12
## 1097343

# The smallest number expressible as the sum of a prime square, prime cube, and
# prime fourth power is 28. In fact, there are exactly four numbers below fifty
# that can be expressed in such a way:

# 28 = 22 + 23 + 24
# 33 = 32 + 23 + 24
# 49 = 52 + 23 + 24
# 47 = 22 + 33 + 24

# How many numbers below fifty million can be expressed as the sum of a prime
# square, prime cube, and prime fourth power?

import helpers.prime as prime
import math

MAX = 50000000

def euler():
    # set of matches found
    matches = set()
    # the primes can never exceed this value
    limit = math.ceil(math.sqrt(MAX))
    # for each (a,b,c) triplet such that a^2+b^3+c^4 < MAX
    for a in prime.primes(limit):
        if a * a >= MAX:
            break
        for b in prime.primes(limit):
            if a * a + b * b * b >= MAX:
                break
            for c in prime.primes(limit):
                k = a * a + b * b * b + c * c * c * c
                if k >= MAX:
                    break
                matches.add(k)
    # return the number of matches
    return len(matches)
