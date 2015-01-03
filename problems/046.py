#encoding=utf-8
## SOLVED 2014/04/10
## 5777

# It was proposed by Christian Goldbach that every odd composite number can be
# written as the sum of a prime and twice a square.

# 9 = 7 + 2×12
# 15 = 7 + 2×22
# 21 = 3 + 2×32
# 25 = 7 + 2×32
# 27 = 19 + 2×22
# 33 = 31 + 2×12

# It turns out that the conjecture was false.

# What is the smallest odd composite that cannot be written as the sum of a prime
# and twice a square?

import math

import helpers.prime as primeutils

def euler():
    # for each odd number starting at 3
    composite = 3
    while True:
        # 'found' will be True iff the composite can be expressed as the sum
        # of a prime and two times a square
        found = False
        # try all prime numbers that are less than the composite number
        for prime in primeutils.primes(composite):
            # calculate the square
            square = (composite - prime) // 2
            # it must have an integer square root for it to be valid
            root = math.sqrt(square)
            if root == int(root):
               found = True 
               break
        # if it cannot be expressed as the sum of blah blah...
        if not found:
            # we found the answer
            return composite
        # next odd number
        composite += 2
