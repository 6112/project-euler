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

HIGHEST_VALUE = 10000
CHAIN_LENGTH = 5


def euler():
    ps = list(primes(HIGHEST_VALUE))
    concats = dict()
    for p in ps:
        concats[p] = set()
        for q in ps:
            if q > p and is_concat_prime(p, q):
                concats[p].add(q)
    for p in ps:
        c = make_chain(CHAIN_LENGTH - 1, concats, p, concats[p])
        if c:
            return sum(c)
    return None

def make_chain(length, concats, p, remaining):
    if length == 0:
        return [p]
    for q in remaining:
        inter = remaining & concats[q]
        chain = make_chain(length - 1, concats, q, inter)
        if chain:
            return [p] + chain
    return None

def is_concat_prime(p, q):
    left = int(str(p) + str(q))
    right = int (str(q) + str(p))
    return is_prime(left) and is_prime(right)
