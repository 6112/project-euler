#encoding=utf-8
## SOLVED 12/04/14
## 296962999629

# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms
# increases by 3330, is unusual in two ways: (i) each of the three terms are
# prime, and, (ii) each of the 4-digit numbers are permutations of one another.

# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
# exhibiting this property, but there is one other 4-digit increasing sequence.

# What 12-digit number do you form by concatenating the three terms in this
# sequence?

import helpers.prime as prime
import helpers.sequence as sequence

# number of digits for each prime number
DIGITS = 4

# leap between two prime numbers that should also be permutations of eachother
LEAP = 3330

def euler():
    # for each of the two possible sets of answers
    for first_prime, second_prime, third_prime in prime_sets():
        # reject the first set of answers
        if first_prime != 1487:
            # return the 12 digits
            xs = (first_prime, second_prime, third_prime)
            return int(''.join(map(str, xs)))

def prime_sets():
    """Yield all sets of possible answers for problem #49.

    Will 'yield' three arguments: the first, second and third prime.

    These three prime numbers are separated by exactly LEAP, and are
    permutations of each other. The three primes have exactly 4 digits."""
    # for each prime number
    for first_prime in prime.primes(10 ** DIGITS // 3):
        # ensure that it has enough digits
        if first_prime > 10 ** (DIGITS - 1):
            # calculate the other two primes
            second_prime = first_prime + LEAP
            third_prime = first_prime + 2 * LEAP
            # invalid if they're not permutations of eachother
            if not is_int_permutation(first_prime, second_prime) or \
                    not is_int_permutation(first_prime, third_prime):
                continue
            # invalid if they're not actually primes
            if not prime.is_prime(second_prime) or \
                    not prime.is_prime(third_prime):
                continue
            # if this is reached, the three primes make up a possible answer
            yield first_prime, second_prime, third_prime

def is_int_permutation(x, y):
    """Return True iff two integers are permutations of eachother's digits."""
    return sequence.is_permutation(list(str(x)), list(str(y)))
