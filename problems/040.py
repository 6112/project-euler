# encoding=utf-8
## SOLVED 2014/01/17
## 210

# An irrational decimal fraction is created by concatenating the positive 
# integers:

# 0.123456789101112131415161718192021...

# It can be seen that the 12th digit of the fractional part is 1.

# If dn represents the nth digit of the fractional part, find the value of the 
# following expression.

# d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

import math

MAX = 1000000

def euler():
    # calculate what the last needed number is
    last_number = 0
    size = 0
    while size < MAX:
        last_number += 1
        size += int(math.log(MAX, 10))
    # construct the string
    string = ''.join(str(number) for number in range(1, MAX + 1))
    # get the characters needed for calculations
    digits = [string [i] for i in [0, 9, 99, 999, 9999, 99999, 999999]]
    # calculate product of these digits
    accumulator = 1
    for digit in digits:
        accumulator *= int(digit)
    # return the product
    return accumulator
