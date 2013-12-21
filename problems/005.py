## SOLVED 19/12/13
## 232792560

# 2520 is the smallest number that can be divided by each of the numbers from 1
# to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the
# numbers from 1 to 20?

from modules.prime import *

HIGHEST_DIVISOR = 20

def euler ():
    zipped_factors = {}
    for number in range (1, HIGHEST_DIVISOR + 1):
        factors = dictionary_prime_factors (number)
        for factor, occurences in factors.items ():
            if (not factor in zipped_factors
              or zipped_factors [factor] < occurences):
                zipped_factors [factor] = occurences
    product = 1
    for factor, power in zipped_factors.items ():
        product *= factor ** power
    return product
