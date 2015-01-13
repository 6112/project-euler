## Module for various functions related to discreet mathematics.

import helpers.prime as prime

def totient(n):
    """Return the number of integers <= n that are relatively prime with n."""
    t = n
    for p in set(prime.prime_factors(n)):
        t *= 1 - 1 / p
    return round(t)

# list of partitions, used by partition(), and indirectly by next_p
ps = [0, 1]
def partition(n):
    """Return the partition of n.

    See Euler's pentagonal number theorem."""
    n += 1
    i = len(ps)
    while i <= n:
        ps.append(_next_p(i, ps))
        i += 1
    return ps[n]

# helper function for partition(): calculate the next partition
def _next_p(n, ps):
    acc = 0
    for dk in (-1, 1):
        k = dk
        q = pentagonal(k)
        while q < n:
            acc += int(((-1) ** (k - 1)) * ps[n - q])
            k += dk
            q = pentagonal(k)
    return acc

# helper function for partition(): calculate the k-th pentagonal number
def pentagonal(k):
    return int(k * (3 * k - 1) / 2)

def gcd(a, b):
    """Return the greatest common divisor for the two integers."""
    if a == b:
        return a
    if a == 0:
        return b
    if b == 0:
        return a
    if a % 2 == 0:
        if b % 2 == 1:
            return gcd(a / 2, b)
        else:
            return gcd(a / 2, b / 2) * 2
    if b % 2 == 0:
        return gcd(a, b / 2)
    if a > b:
        return gcd((a - b) / 2, b)
    return gcd((b - a) / 2, a)
