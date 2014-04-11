#encoding=utf-8
## SOLVED 10/04/14
## 134043

# The first two consecutive numbers to have two distinct prime factors are:

# 14 = 2 × 7
# 15 = 3 × 5

# The first three consecutive numbers to have three distinct prime factors are:

# 644 = 2² × 7 × 23
# 645 = 3 × 5 × 43
# 646 = 2 × 17 × 19.

# Find the first four consecutive integers to have four distinct prime factors.
# What is the first of these numbers?

import modules.prime as prime

FACTOR_COUNT = 4

def euler():
    # for each integer n
    n = 2
    while True:
        # 'is_answer' will be True iff all FACTOR_COUNT consecutive numbers
        # have exactly FACTOR_COUNT distinct prime factors
        is_answer = True
        # for each of those numbers
        for offset in range(0, FACTOR_COUNT):
            # it's not the right answer if it doesn't have the right amount of
            # factors
            if prime_factor_count(n + offset) != FACTOR_COUNT:
                is_answer = False
                n += offset
                break
        # return the answer if found
        if is_answer:
            return n
        # increment n
        n += 1

def prime_factor_count(n):
    """Returns the number of distinct prime factors of a number."""
    return len(prime.dictionary_prime_factors(n))
