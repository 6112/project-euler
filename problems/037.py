# encoding=utf-8
## SOLVED 2013/12/25
## 748317

# The number 3797 has an interesting property. Being prime itself, it is
# possible to continuously remove digits from left to right, and remain prime at
# each stage: 3797, 797, 97, and 7. Similarly we can work from right to left:
# 3797, 379, 37, and 3.

# Find the sum of the only eleven primes that are both truncatable from left to
# right and right to left.

# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

import helpers.prime as primeutils
import helpers.sequence as sequence

def euler():
    accumulator = 0
    primes_found = 0
    cache = {}
    for prime in primeutils.all_primes():
        if prime not in cache and is_truncatable(prime):
            primes_found += 1
            accumulator += prime
            cache [prime] = True
        if primes_found == 11:
            break
    return accumulator

def is_truncatable(number):
    if number < 10:
        return False
    for truncation in sequence.left_truncations(str(number)):
        if not primeutils.is_prime(int(truncation)):
            return False
    for truncation in sequence.right_truncations(str(number)):
        if not primeutils.is_prime(int(truncation)):
            return False
    return True 
