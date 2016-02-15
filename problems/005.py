# encoding=utf-8
## SOLVED 2013/12/19
## 232792560

# 2520 is the smallest number that can be divided by each of the numbers from 1
# to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the
# numbers from 1 to 20?

import helpers.prime as prime

HIGHEST_DIVISOR = 20

def euler():
    # dictionary containing the highest power of each prime factor
    zipped_factors = {}
    # for each number in the desired range
    for number in range(2, HIGHEST_DIVISOR + 1):
        # calculate its prime factors
        factors = prime.multiset_prime_factors(number)
        # for each of those factors, and its power
        for factor, power in factors.items():
            # if that factor's power is higher than the one we had before
            if (not factor in zipped_factors
                or zipped_factors [factor] < power):
                # set the factor's power to this power
                zipped_factors [factor] = power
    # calculate the product of the prime factors elevated to the given powers
    accumulator = 1
    for factor, power in zipped_factors.items():
        accumulator *= factor ** power
    # return that product
    return accumulator
