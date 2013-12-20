## Module for prime number mathematics.

from math import ceil, sqrt, floor

prime_list = [2, 3]

def generate_primes (highest_value):
    """Generates the list of primes prime_list which contains all prime numbers
    lower than a given number."""
    number = prime_list [-1]
    highest_test_prime = ceil (sqrt (highest_value))
    test_primes = []
    i = 0
    while i < len (prime_list) and prime_list [i] <= highest_test_prime:
        test_primes.append (prime_list [i])
        i += 1
    def divides_by (prime):
        return number % prime == 0
    while number <= highest_value:
        if all (number % prime != 0 for prime in test_primes):
            prime_list.append (number)
            if number <= highest_test_prime:
                test_primes.append (number)
        number += 2
    return prime_list

def primes (highest_value):
    """Returns an iterator for all primes up to a maximum value."""
    generate_primes (highest_value)
    i = 0
    while i < len (prime_list) and prime_list [i] <= highest_value:
        yield prime_list [i]
        i += 1

def is_prime (number):
    """Returns True if a given integer is a prime number."""
    highest_divisor = floor (sqrt (number))
    return all (number % prime != 0 for prime in primes (highest_divisor))

def prime_factors (number):
    """Returns a list of all primes that are divisors of a given integer
    number.
    
    The list contains only prime numbers, whose product is equal to the original
    number""" 
    if is_prime (number):
        return [number]
    factors = []
    highest_divisor = floor (sqrt (number))
    for prime in primes (highest_divisor):
        if number % prime == 0:
            return prime_factors (prime) + prime_factors (number // prime)
