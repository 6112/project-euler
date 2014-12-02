import helpers.prime as prime

def totient(n):
    """Returns the number of integers <= n that are relatively prime with n."""
    t = n
    for p in set(prime.prime_factors(n)):
        t *= 1 - 1 / p
    return round(t)
