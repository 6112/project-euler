# encoding=utf-8
## SOLVED 2013/12/23
## 669171001

# Starting with the number 1 and moving to the right in a clockwise direction a
# 5 by 5 spiral is formed as follows:

# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13

# It can be verified that the sum of the numbers on the diagonals is 101.

# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral
# formed in the same way?

SIZE = 1001

def euler():
    # accumulator for the sum of the numbers on the diagonal
    accumulator = 1
    # current number
    number = 1
    # for each difference between numbers, from 2 to SIZE
    for leap in range(2, SIZE + 1, 2):
        # for each corner
        for i in range(4):
            number += leap
            # add to the accumulator
            accumulator += number
    # return the sum accumulator
    return accumulator
