#encoding=utf-8
## SOLVED 10/04/14
## 16695334890

# The number, 1406357289, is a 0 to 9 pandigital number because it is made up of
# each of the digits 0 to 9 in some order, but it also has a rather interesting
# sub-string divisibility property.

# Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note
# the following:

# d2d3d4=406 is divisible by 2
# d3d4d5=063 is divisible by 3
# d4d5d6=635 is divisible by 5
# d5d6d7=357 is divisible by 7
# d6d7d8=572 is divisible by 11
# d7d8d9=728 is divisible by 13
# d8d9d10=289 is divisible by 17

# Find the sum of all 0 to 9 pandigital numbers with this property.

import modules.sequence as sequence

def euler():
    accumulator = 0
    for pandigital in generate_pandigitals():
        accumulator += list_to_int(pandigital)
    return accumulator

def list_to_int(digits):
    accumulator = 0
    for digit in digits:
        accumulator *= 10
        accumulator += int(digit)
    return accumulator

def generate_pandigitals():
    digits = set(range(0, 10))
    for first_digit in digits:
        first_available_digits = set(digits)
        first_available_digits.remove(first_digit)
        for second_digit in first_available_digits:
            second_available_digits = set(first_available_digits)
            second_available_digits.remove(second_digit)
            for third_digit in second_available_digits:
                third_available_digits = set(second_available_digits)
                third_available_digits.remove(third_digit)
                for pandigital in generate_pandigitals_helper([second_digit, third_digit],
                        [2, 3, 5, 7, 11, 13, 17],
                        third_available_digits):
                    yield [first_digit, second_digit, third_digit] + pandigital

def generate_pandigitals_helper(pair, divisors, available):
    divisor = divisors[0]
    for last_digit in available:
        if (pair[0] * 100 + pair[1] * 10 + last_digit) % divisor == 0:
            if len(divisors) == 1:
                yield [last_digit]
            else:
                for pandigital in generate_pandigitals_helper([pair[1], last_digit],
                        divisors[1:], available - {last_digit}):
                    yield [last_digit] + pandigital
