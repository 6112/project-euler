# encoding=utf-8
## SOLVED 17/11/14
## 26033

# The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes
# and concatenating them in any order the result will always be prime. For
# example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these
# four primes, 792, represents the lowest sum for a set of four primes with
# this property.

# Find the lowest sum for a set of five primes for which any two primes
# concatenate to produce another prime.

from modules.prime import *

# max prime to use for testing things
HIGHEST_VALUE = 10000

# target length of the chain to look for
CHAIN_LENGTH = 5

def euler():
    # calculate the list of all prime numbers up to HIGHEST_VALUE
    ps = list(primes(HIGHEST_VALUE))
    # make a dictionary that associates each prime number to other primes with
    # which it is_concat_prime()
    concats = dict()
    for p in ps:
        concats[p] = set()
        for q in ps:
            if q > p and is_concat_prime(p, q):
                concats[p].add(q)
    # for each possible starting number, try to make a chain
    for p in ps:
        c = make_chain(CHAIN_LENGTH - 1, concats, p, concats[p])
        # if the chain actually worked, return its sum
        if c:
            return sum(c)
    return None

def make_chain(length, concats, p, remaining):
    if length == 0:
        # return if the chain is completed
        return [p]
    # for each prime that works for is_concat_prime() with p
    for q in remaining:
        # intersection of primes that work for is_concat_prime() with p, and
        # those that work with q
        inter = remaining & concats[q]
        # try to continue the chain
        chain = make_chain(length - 1, concats, q, inter)
        # return if it worked
        if chain:
            return [p] + chain
    return None

# returns True iff "${p}${q}" and "${q}${p}" are both prime numbers
def is_concat_prime(p, q):
    left = int(str(p) + str(q))
    right = int (str(q) + str(p))
    return is_prime(left) and is_prime(right)
