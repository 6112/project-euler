#!/usr/bin/python3
## SOLVED 19/12/13
## 104743

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
# that the 6th prime is 13.

# What is the 10 001st prime number?

from modules.prime import *

INDEX = 10000

def euler ():
    generate_n_primes (INDEX + 1)
    return prime_list [INDEX]

print (euler ())
