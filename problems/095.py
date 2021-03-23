# encoding=utf-8
## SOLVED 2021/03/23
## 14316

# The proper divisors of a number are all the divisors excluding the number
# itself. For example, the proper divisors of 28 are 1, 2, 4, 7, and 14. As the
# sum of these divisors is equal to 28, we call it a perfect number.

# Interestingly the sum of the proper divisors of 220 is 284 and the sum of the
# proper divisors of 284 is 220, forming a chain of two numbers. For this
# reason, 220 and 284 are called an amicable pair.

# Perhaps less well known are longer chains. For example, starting with 12496,
# we form a chain of five numbers:

# 12496 → 14288 → 15472 → 14536 → 14264 (→ 12496 → ...)

# Since this chain returns to its starting point, it is called an amicable
# chain.

# Find the smallest member of the longest amicable chain with no element
# exceeding one million.

import math

MAX = 1000000

# Maps each number to the sum of their divisors.
sieve = [1] * (MAX + 1)

def euler():
    # This sieve is faster than computing the divisors of each number.
    for d in range(2, math.ceil(math.sqrt(MAX)) + 1):
        for i in range(d * d, MAX + 1, d):
            if i // d == d:
                sieve[i] += d
            else:
                sieve[i] += d + i // d
    longest = 0
    smallest = MAX
    for n in range(10, MAX):
        chain = generate_chain(n)
        if chain and len(chain) > longest:
            longest = len(chain)
            smallest = min(chain)
    return smallest

# Avoid re-visiting the same number twice.
seen = set()

def generate_chain(n):
    chain = []
    while n not in chain:
        if n > MAX or n <= 0:
            return None
        if n in seen:
            return None
        seen.add(n)
        chain.append(n)
        n = sieve[n]
    return chain[chain.index(n):]
