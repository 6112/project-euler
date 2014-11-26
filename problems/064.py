# encoding=utf-8
## SOLVED 25/11/14
## 1322

# All square roots are periodic when written as continued fractions.

# [Examples...]

# It can be seen that the sequence is repeating. For conciseness, we use the
# notation √23 = [4;(1,3,1,8)], to indicate that the block (1,3,1,8) repeats
# indefinitely.

# The first ten continued fraction representations of (irrational) square roots
# are:

# √2=[1;(2)], period=1
# √3=[1;(1,2)], period=2
# √5=[2;(4)], period=1
# √6=[2;(2,4)], period=2
# √7=[2;(1,1,1,4)], period=4
# √8=[2;(1,4)], period=2
# √10=[3;(6)], period=1
# √11=[3;(3,6)], period=2
# √12= [3;(2,6)], period=2
# √13=[3;(1,1,1,1,6)], period=5

# Exactly four continued fractions, for N ≤ 13, have an odd period.

# How many continued fractions for N ≤ 10000 have an odd period?

from math import sqrt

def euler():
    solution_count = 0
    for n in range(2, 10001):
        if continued_fraction(n) % 2 == 1:
            solution_count += 1
    return solution_count

# uses the algorithm described on this Wikipedia page:
# http://en.wikipedia.org/wiki/Methods_of_computing_square_roots
# in the "Continued fraction expansion" section
def continued_fraction(n):
    if int(sqrt(n)) == sqrt(n):
        return 0
    length = 0
    m = 0
    d = 1
    a = int(sqrt(n))
    a0 = a
    while a != 2 * a0:
        m = d * a - m
        d = (n - m * m) / d
        a = int((a0 + m) / d)
        length += 1
    return length
