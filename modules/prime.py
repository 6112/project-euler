## Module for prime number mathematics.

from math import ceil, sqrt, floor

prime_list = [2, 3]

def generate_primes (highest_value):
    """Generates the list of primes prime_list which contains all prime numbers
    lower than a given number."""
    number = prime_list [-1] + 2
    highest_test_prime = ceil (sqrt (highest_value))
    test_primes = []
    i = 0
    while i < len (prime_list) and prime_list [i] <= highest_test_prime:
        test_primes.append (prime_list [i])
        i += 1
    while number <= highest_value:
        if all (number % prime != 0 for prime in test_primes):
            prime_list.append (number)
            if number <= highest_test_prime:
                test_primes.append (number)
        number += 2
    return prime_list

def generate_n_primes (number_of_primes):
    """Generates the list of primes prime_list which contains all the first n
    prime numbers."""
    number = prime_list [-1] + 2
    prime_count = len (prime_list)
    while prime_count < number_of_primes:
        is_a_prime = True
        highest_test_prime = ceil (sqrt (number))
        i = 0
        while i < len (prime_list) and prime_list [i] <= highest_test_prime:
            is_a_prime = is_a_prime and number % prime_list [i] != 0
            i += 1
        if is_a_prime:
            prime_list.append (number)
            prime_count += 1
        number += 2
    return prime_list

def all_primes (leap = 100000):
    """Used as an iteartor for all prime numbers."""
    highest_prime = prime_list [-1]
    while True:
        highest_prime += leap
        generate_primes (highest_prime)
        iterator = 0
        while iterator < len (prime_list):
            yield prime_list [iterator]
            iterator += 1

def primes (highest_value):
    """Used as an iterator for all primes up to a maximum value."""
    generate_primes (highest_value)
    i = 0
    while i < len (prime_list) and prime_list [i] <= highest_value:
        yield prime_list [i]
        i += 1

def n_primes (number_of_primes):
    """Used as an iterator for the first n primes."""
    generate_n_primes (number_of_primes)
    for i in range (number_of_primes):
        yield prime_list [i]

def is_prime (number):
    """Returns True if a given integer is a prime number."""
    if number == 1:
        return False
    highest_divisor = floor (sqrt (number))
    return all (number % prime != 0 for prime in primes (highest_divisor))

prime_factors_cache = {}
def prime_factors (number):
    """Returns a list of all primes that are divisors of a given integer
    number.
    
    The list contains only prime numbers, whose product is equal to the original
    number""" 
    if is_prime (number):
        return [number]
    if number in prime_factors_cache:
        return prime_factors_cache [number]
    factors = []
    highest_divisor = floor (sqrt (number))
    for prime in primes (highest_divisor):
        if number % prime == 0:
            factors = prime_factors (prime) + prime_factors (number // prime)
            prime_factors_cache [number] = factors
            return factors

def dictionary_prime_factors (number):
    """Returns the same list of prime factors as the prime_factors() function,
    but reduces as a dictionary mapping each factor to its number of occurences.

    For instance, [2,2,2, 3, 5,5] becomes {2:3, 3:1, 5:2}."""
    factors = prime_factors (number)
    unique_factors = list (set (factors))
    dictionary = {}
    for factor in unique_factors:
        dictionary [factor] = factors.count (factor)
    return dictionary

def divisor_count (number):
    """Returns the number of integers that can evenly divide a given number."""
    dictionary = dictionary_prime_factors (number)
    divisors = 1
    for power in dictionary.values ():
        divisors *= (power + 1)
    return divisors

divisors_cache = {}
def divisors (number):
    """Returns a list of the divisors of a given number."""
    if number in divisors_cache: 
        return divisors_cache [number]
    prime_divisors = prime_factors (number)
    divisors_dictionary = {}
    for prime in prime_divisors:
        divisors_dictionary [prime] = True
        factor = number // prime
        divisors_dictionary [factor] = True
        if not factor in prime_divisors:
            xs = list (divisors_dictionary.items ())
            xs += [(divisor, True) for divisor in divisors (factor)]
            divisors_dictionary = dict (xs)
    result = list (divisors_dictionary.keys ())
    if not 1 in result:
        result.append (1)
    if not number in result:
        result.append (number)
    divisors_cache [number] = result
    return result
