# encoding=utf-8
## SOLVED 24/12/13
## 100

# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in
# attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is
# correct, is obtained by cancelling the 9s.

# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

# There are exactly four non-trivial examples of this type of fraction, less
# than one in value, and containing two digits in the numerator and denominator.

# If the product of these four fractions is given in its lowest common terms,
# find the value of the denominator.

from fractions import *

def euler ():
    accumulator = Fraction (1, 1)
    for digit_1 in range (1, 10):
        for digit_2 in range (1, 10):
            for digit_3 in range (1, 10):
                if digit_1 != digit_2 or digit_1 != digit_3:
                    numerator = digit_1 * 10 + digit_2
                    denominator = digit_2 * 10 + digit_3
                    original_fraction = Fraction (numerator, denominator)
                    numerator = digit_1
                    denominator = digit_3
                    reduced_fraction = Fraction (numerator, denominator)
                    if original_fraction == reduced_fraction:
                        accumulator *= original_fraction
    return accumulator.denominator
