# encoding=utf-8
## SOLVED 2016/02/15
## 7587457

# A natural number, N, that can be written as the sum and product of a given set
# of at least two natural numbers, {a1, a2, ... , ak} is called a product-sum
# number: N = a1 + a2 + ... + ak = a1 × a2 × ... × ak.

# For example, 6 = 1 + 2 + 3 = 1 × 2 × 3.

# For a given set of size, k, we shall call the smallest N with this property a
# minimal product-sum number. The minimal product-sum numbers for sets of size,
# k = 2, 3, 4, 5, and 6 are as follows.

# k=2: 4 = 2 × 2 = 2 + 2
# k=3: 6 = 1 × 2 × 3 = 1 + 2 + 3
# k=4: 8 = 1 × 1 × 2 × 4 = 1 + 1 + 2 + 4
# k=5: 8 = 1 × 1 × 2 × 2 × 2 = 1 + 1 + 2 + 2 + 2
# k=6: 12 = 1 × 1 × 1 × 1 × 2 × 6 = 1 + 1 + 1 + 1 + 2 + 6

# Hence for 2≤k≤6, the sum of all the minimal product-sum numbers is
# 4+6+8+12 = 30; note that 8 is only counted once in the sum.

# In fact, as the complete set of minimal product-sum numbers for 2≤k≤12 is
# {4, 6, 8, 12, 15, 16}, the sum is 61.

# What is the sum of all the minimal product-sum numbers for 2≤k≤12000?

import helpers.prime as prime
import math
import collections

BIG_NUMBER = 999

def euler():
    product_sum_numbers = {}
    for k in range(2, 12001):
        product_sum_numbers[k] = 15000
    for i in range(4, 15000):
        for factors in factorizations(i, 2):
            k = i - sum(factors) + len(factors)
            if k in product_sum_numbers:
                product_sum_numbers[k] = min(product_sum_numbers[k], i)
    numbers = set()
    for k in range(2, 12001):
        numbers.add(product_sum_numbers[k])
    return sum(numbers)

def factorizations(n, smallest):
    if n == 1:
        return [[]]
    m = math.floor(math.sqrt(n))
    fs = []
    for i in range (smallest, m + 1):
        if n % i == 0:
            fs.extend([i] + p for p in factorizations(n // i, i))
    fs.append([n])
    return fs

