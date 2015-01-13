# encoding=utf-8
## SOLVED 2013/12/23
## 4782

# The Fibonacci sequence is defined by the recurrence relation:

# Fn = F_n−1 + F_n−2, where F_1 = 1 and F_2 = 1.

# The 12th term, F_12 = 144, is the first term to contain three digits.

# What is the first term in the Fibonacci sequence to contain 1000 digits?

import math

DIGITS = 1000

def euler():
    # used to calculate fibonacci numbers
    previous_number = 0
    current_number = 1
    # number of fibonacci numbers generated
    index = 0
    while True:
        index += 1
        # return the index if the current number has 1000 digits at least
        if math.log(current_number, 10) >= DIGITS - 1:
            return index
        # generate the next fibonacci number
        previous_number += current_number
        current_number, previous_number = previous_number, current_number
