# encoding=utf-8
## SOLVED 23/12/13
## -59231

# Euler discovered the remarkable quadratic formula:

# n² + n + 41

# It turns out that the formula will produce 40 primes for the consecutive
# values n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is
# divisible by 41, and certainly when n = 41, 41² + 41 + 41 is clearly divisible
# by 41.

# The incredible formula  n² − 79n + 1601 was discovered, which produces 80
# primes for the consecutive values n = 0 to 79. The product of the
# coefficients, −79 and 1601, is −126479.

# Considering quadratics of the form:

# n² + an + b, where |a| < 1000 and |b| < 1000

# where |n| is the modulus/absolute value of n
# e.g. |11| = 11 and |−4| = 4

# Find the product of the coefficients, a and b, for the quadratic expression
# that produces the maximum number of primes for consecutive values of n,
# starting with n = 0.

from modules.prime import *

def euler ():
    longest_sequence = 0
    product = 0
    for a in range (-1000, 1000):
        for b in range (-1000, 1000):
            length = sequence_length (a, b)
            if length > longest_sequence:
                longest_sequence = length
                product = a * b
    return product

def sequence_length (a, b):
    def f ():
        return n ** 2 + a * n + b
    n = 0
    while f () > 1 and is_prime (f ()):
        n += 1
    return n
