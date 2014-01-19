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

HIGHEST_DIVISOR = 1000

def euler ():
    # longest length for a cycle
    longest_cycle_length = 0
    # divisor that generates that cycle length
    longest_cycle_divisor = 0
    # for each divisor
    for divisor in range (2, HIGHEST_DIVISOR):
        # calculate the length of the fraction's cycle
        cycle_length = fraction_cycle_length (divisor)
        # if it's higher than any value seen before
        if cycle_length > longest_cycle_length:
            # keep in memory the cycle length, and which divisor generates it
            longest_cycle_length = cycle_length
            longest_cycle_divisor = divisor
    # return the divisor that generates the longest cycle
    return (longest_cycle_length, longest_cycle_divisor)

def fraction_cycle_length (denominator):
    """Return the number of digits in the cycle part of a fraction.

    For instance, in 1/3 (0.3333...), '3' is the recurring cycle. The length of
    that cycle is 1.

    In 1/7 (0.142857142857142...), '142857' is the recuring cycle. The length of
    the cycle is 6.
    """
    # counter for the number of digits generated
    digit_count = 0
    # accumulator for the current number to be divided
    accumulator = 1
    # values encountered for the accumulator
    accumulators = []
    # while there is a remainder to the division
    while accumulator != 0:
        # if the current accumulator can be divided by the denominator
        if accumulator >= denominator:
            # the digit to add to the number is the result of that division
            digit = accumulator // denominator
            # if we have never had that accumulator before
            if not accumulator in accumulators:
                accumulators.append (accumulator)
            else:
                # if we have already met that accumulator before, return the
                # number of digits between two occurences
                return digit_count - accumulators.index (accumulator)
            # subtract the result of the division from the accumulator
            accumulator -= digit * denominator
            # add a digit to the digit count
            digit_count += 1
        else:
            # the current accumulator cannot be divided by the denominator,
            # multiply it by 10
            accumulator *= 10
    # divides evenly, 0 cycle length
    return 0
