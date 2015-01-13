# encoding=utf-8
## SOLVED 2014/01/19
## 7652413

# We shall say that an n-digit number is pandigital if it makes use of all the
# digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is
# also prime.

# What is the largest n-digit pandigital prime that exists?

import helpers.prime as prime
import helpers.sequence as sequence

def euler():
    # highest pandigital prime found so far
    highest_pandigital = 0
    # for number of digits from 4 to 9
    for length in range(4, 9):
        # generate the list of digits from 1 to n
        digits = list(range(1, length + 1))
        # for each permutation of these digits
        for permutation in sequence.permutations(digits):
            number = int(''.join(str(digit) for digit in permutation))
            # check if the number is prime
            if prime.is_prime(number):
                # set the new value of the highest pandigital prime if needed
                highest_pandigital = max(number, highest_pandigital)
    # return the highest pandigital prime found
    return highest_pandigital
