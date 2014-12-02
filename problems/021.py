# encoding=utf-8
## SOLVED 21/12/13
## 31626

# Let d(n) be defined as the sum of proper divisors of n (numbers less than n
# which divide evenly into n).

# If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and
# each of a and b are called amicable numbers.

# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55
# and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71
# and 142; so d(284) = 220.

# Evaluate the sum of all the amicable numbers under 10000.

import helpers.prime as prime

HIGHEST_VALUE = 10000

def euler ():
    # accumulator for the sum
    accumulator = 0
    # for each value of a in the given range
    for a in range (1, HIGHEST_VALUE):
        # calculate the b
        b = d (a)
        # if a and b are amicable
        if b != 0 and d (b) == a and a < b:
            # add them to the sum
            accumulator += b + a
    # return the sum accumulator
    return accumulator

def d (number):
    """Return the sum of the divisors of a given number.
    
    Divisors exclude the number itself, i.e.:

    d (2) = 1 = 1
    d (4) = 1 + 2 = 3
    d (6) = 1 + 2 + 3 = 6
    """
    return sum (divisors (number)) - number
