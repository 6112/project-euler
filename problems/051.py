#encoding=utf-8
## SOLVED 18/04/14
## 121313

# By replacing the 1st digit of the 2-digit number *3, it turns out that six of
# the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

# By replacing the 3rd and 4th digits of 56**3 with the same digit, this
# 5-digit number is the first example having seven primes among the ten
# generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663,
# 56773, and 56993. Consequently 56003, being the first member of this family,
# is the smallest prime with this property.

# Find the smallest prime which, by replacing part of the number (not
# necessarily adjacent digits) with the same digit, is part of an eight prime
# value family.

import helpers.prime as prime

# number of replacements of digits that have to work
FAMILY_SIZE = 8

def euler():
    # for each "starting" prime number
    for prime_number in prime.primes(200000):
        # list of integers for each digit
        prime_number_digits = list(int(digit) for digit in str(prime_number))
        # set (without duplicates) of the digits in the prime number
        prime_number_digit_set = set(prime_number_digits)
        # for each digit that could be replaced in the prime number
        for base_digit in prime_number_digit_set:
            # number of digit replacements that are actual prime numbers
            prime_count = 0
            # never replace the first digit with a zero
            replacements = range(10) if prime_number_digits[0] != base_digit \
                    else range(1, 10)
            # for each possible digit replacement
            for replacement_digit in replacements:
                # replace the digit base_digit with replacement_digit
                modified_digits = replace(prime_number_digits, base_digit,
                        replacement_digit)
                # convert that list to a number
                modified_number = int(''.join(str(digit) \
                        for digit in modified_digits))
                # if it's a prime, increment the prime count (duh)
                if prime.is_prime(modified_number):
                    prime_count += 1
            # return if the answer if we found it
            if prime_count == FAMILY_SIZE:
                return prime_number

def replace(xs, base, replacement):
    """Replaces every 'base' in 'xs' with 'replacement'. Non destructive.

    Args:
        xs: Initial list of elements.
        base: Element to be replaced in the new list.
        replacement: Element to replace that value with.
    Returns:
        A new list with the replacement applied."""
    return [x if x != base else replacement for x in xs]
