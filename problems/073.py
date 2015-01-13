# encoding=utf-8
## SOLVED 2014/12/07
## 7295372

# Consider the fraction, n/d, where n and d are positive integers. If n<d and
# HCF(n,d)=1, it is called a reduced proper fraction.

# If we list the set of reduced proper fractions for d ≤ 8 in ascending order
# of size, we get:

# 1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3,
# 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

# It can be seen that there are 3 fractions between 1/3 and 1/2.

# How many fractions lie between 1/3 and 1/2 in the sorted set of reduced
# proper fractions for d ≤ 12,000?

import helpers.prime as prime
import math

DELTA = 0.0001
MAX = 12000

def euler():
    # number of fractions found
    match_count = 0
    # for each possible numerator n
    for n in range(2, math.ceil(MAX / 2) + 1):
        # lowest possible denominator for a fraction in the wanted range
        start = math.ceil(2 * n + DELTA)
        # highest possible denominator for a fraction in the wanted range
        end = min(MAX, int(3 * n - DELTA))
        # construct a dictionary whose keys are all the denominators that
        # do *not* make a reduced fraction with the numerator n
        table = dict()
        for p in prime.prime_factors(n):
            for q in range(p, end + 1, p):
                table[q] = True
        # for each denominator d
        for d in range(start, end + 1):
            # if n / d is a reduced fraction
            if not d in table:
                match_count += 1
    # return the number of fractions found
    return match_count
