# encoding=utf-8
## SOLVED 23/12/13
## 4179871

# A perfect number is a number for which the sum of its proper divisors is
# exactly equal to the number. For example, the sum of the proper divisors of 28
# would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

# A number n is called deficient if the sum of its proper divisors is less than
# n and it is called abundant if this sum exceeds n.
 
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
# number that can be written as the sum of two abundant numbers is 24. By
# mathematical analysis, it can be shown that all integers greater than 28123
# can be written as the sum of two abundant numbers. However, this upper limit
# cannot be reduced any further by analysis even though it is known that the
# greatest number that cannot be expressed as the sum of two abundant numbers is
# less than this limit.
 
# Find the sum of all the positive integers which cannot be written as the sum
# of two abundant numbers.

from modules.prime import *

MAX_VALUE = 28123

def euler ():
    abundants = {}
    for number in range (1, MAX_VALUE):
        if is_abundant (number):
            abundants [number] = True
    accumulator = 0
    for number in range (1, MAX_VALUE):
        is_a_sum = False
        for abundant in abundants:
            if (number - abundant) in abundants:
                is_a_sum = True
                break
        if not is_a_sum:
            accumulator += number
    return accumulator

def is_abundant (number):
    return sum (divisors (number)) - number > number
