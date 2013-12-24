# encoding=utf-8
## SOLVED 23/12/13
## 983

# A unit fraction contains 1 in the numerator. The decimal representation of the
# unit fractions with denominators 2 to 10 are given:

# 1/2    =   0.5
# 1/3    =   0.(3)
# 1/4    =   0.25
# 1/5    =   0.2
# 1/6    =   0.1(6)
# 1/7    =   0.(142857)
# 1/8    =   0.125
# 1/9    =   0.(1)
# 1/10   =   0.1

# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be
# seen that 1/7 has a 6-digit recurring cycle.

# Find the value of d < 1000 for which 1/d contains the longest recurring cycle
# in its decimal fraction part.

def euler ():
    longest_cycle_length = 0
    longest_cycle_number = 0
    for iterator in range (2, 1000):
        cycle_length = fraction_cycle_length (iterator)
        if cycle_length > longest_cycle_length:
            longest_cycle_length = cycle_length
            longest_cycle_number = iterator
    return longest_cycle_number

def fraction_cycle_length (denominator):
    digits = []
    iterator = 0
    accumulator = 1
    while accumulator != 0:
        if accumulator >= denominator:
            digit = accumulator // denominator
            if not accumulator in digits:
                digits.append (accumulator)
            else:
                return iterator - digits.index (accumulator)
            accumulator -= digit * denominator
            iterator += 1
        else:
            accumulator *= 10
    return 0
