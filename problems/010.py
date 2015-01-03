# encoding=utf-8
## SOLVED 2013/12/19
## 142913828922

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

import helpers.prime as prime

HIGHEST_VALUE = 2000000

def euler ():
    # calculate and return the sum of the primes
    return sum (prime.primes (HIGHEST_VALUE))
