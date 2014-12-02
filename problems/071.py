# encoding=utf-8
## SOLVED 01/12/14
## 428570

# Consider the fraction, n/d, where n and d are positive integers. If n<d and
# HCF(n,d)=1, it is called a reduced proper fraction.

# If we list the set of reduced proper fractions for d ≤ 8 in ascending order
# of size, we get:

# 1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3,
# 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

# It can be seen that 2/5 is the fraction immediately to the left of 3/7.

# By listing the set of reduced proper fractions for d ≤ 1,000,000 in ascending
# order of size, find the numerator of the fraction immediately to the left of
# 3/7.

HIGHEST_D = 10 ** 6

def euler():
    m = 0
    best_match = (2 / 7, None)
    for d in range(2, HIGHEST_D):
        if d % 7 != 0:
            m += 1
            n = m // 2
            if n / d > best_match[0]:
                best_match = (n / d, n)
    return best_match[1]
