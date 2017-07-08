# encoding=utf-8
## SOLVED 2017/07/08
## 8581146

# A number chain is created by continuously adding the square of the digits in a
# number to form a new number until it has been seen before.

# For example,

# 44 → 32 → 13 → 10 → 1 → 1
# 85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

# Therefore any chain that arrives at 1 or 89 will become stuck in an endless
# loop. What is most amazing is that EVERY starting number will eventually
# arrive at 1 or 89.

# How many starting numbers below ten million will arrive at 89?

from collections import defaultdict

MAX = 1 * 10 ** 6

def factorial(n):
    """Return the `n!`."""
    acc = 1
    for i in range(2, n + 1):
        acc *= i
    return acc

def digit_sequences(tokens, n):
    """Iterator for sequences of `n` digits in sorted order, taken from the list
    of `tokens`. Sequences may contain the same digit more than once."""
    if not tokens or n == 0:
        yield []
        return
    for index, first in enumerate(tokens):
        if n == 1:
            yield [first]
        else:
            for seq in digit_sequences(tokens[index:], n - 1):
                if seq:
                    yield [first] + seq

def permutation_count(xs):
    """Return the number of permutations of the sequence `xs`, taking into
    account duplicate elements."""
    lookup = defaultdict(lambda: 0)
    for x in xs:
        lookup[x] += 1
    base = factorial(len(xs))
    for i in lookup.values():
        base //= factorial(i)
    return base

def euler():
    acc = 0
    for i in range(1, 1000):
        arrives_at(i)
    for seq in digit_sequences(range(10), 7):
        m = sum(c * c for c in seq)
        if arrives_at(m) == 89:
            acc += permutation_count(seq)
    return acc

arrives_at_cache = { 0: 0, 1: 1, 89: 89 }
def arrives_at(n):
    """Determine which value the number `n` arrives at in the chain: 1 or 89."""
    if n in arrives_at_cache:
        return arrives_at_cache[n]
    m = sum(int(c) * int(c) for c in str(n))
    result = arrives_at(m)
    arrives_at_cache[n] = result
    return result
