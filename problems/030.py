# encoding utf-8
## SOLVED 2013/12/24
## 443839

# Surprisingly there are only three numbers that can be written as the sum of
# fourth powers of their digits:

# 1634 = 1^4 + 6^4 + 3^4 + 4^4
# 8208 = 8^4 + 2^4 + 0^4 + 8^4
# 9474 = 9^4 + 4^4 + 7^4 + 4^4

# As 1 = 14 is not a sum it is not included.

# The sum of these numbers is 1634 + 8208 + 9474 = 19316.

# Find the sum of all the numbers that can be written as the sum of fifth powers
# of their digits.

POWER = 5

def euler():
    accumulator = 0
    for number in range(2, POWER * 9 ** POWER + 1):
        if is_sum_of_power_digits(number, POWER):
            accumulator += number
    return accumulator

def is_sum_of_power_digits(number, power):
    starting_number = number
    accumulator = 0
    while number > 0:
        digit = number % 10
        accumulator += digit ** power
        number //= 10
    return accumulator == starting_number
