#encoding=utf-8
## SOLVED 2014/04/18
## 142857

# It can be seen that the number, 125874, and its double, 251748, contain
# exactly the same digits, but in a different order.

# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x,
# contain the same digits.

import helpers.sequence as sequence

# list of factors for the multiplications that have to be checked
FACTORS = [2, 3, 4, 5, 6]

def euler():
    # set of the digits to use for generating numbers: all the digits except
    # '1', see related hack
    digits = list(set(range(10)) - {1})
    # number of matches found, only take the second one
    matches_count = 0
    # for each permutation of the digits
    for digit_permutation in sequence.permutations(digits):
        # for each truncation in that permutation
        for base_digits in sequence.right_truncations(digit_permutation):
            # add '1' at the beginning of the number, because the number
            # must start with a '1' in order to have the same number of digits
            # when multiplied by 6
            base_digits = [1] + base_digits
            # the base number which will be multiplied
            base = int(''.join(str(digit) for digit in base_digits))
            # found will stay True if all the multiplications by the FACTORS
            # have the same digits
            found = True
            # for each factor, check if it yields the same digits
            for factor in FACTORS:
                found = found and set(str(base)) == set(str(base * factor))
            # if it's a valid answer
            if found:
                # return the second valid answer found
                matches_count += 1
                if matches_count == 2:
                    return base
