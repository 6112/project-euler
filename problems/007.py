# encoding=utf-8
## SOLVED 2013/12/19
## 104743

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
# that the 6th prime is 13.

# What is the 10 001st prime number?

import helpers.prime as prime

INDEX = 10000

def euler():
    # generate 10001 prime numbers
    prime._generate_n_primes(INDEX + 1)
    # return the 10001st prime number
    return prime.prime_list [INDEX]
