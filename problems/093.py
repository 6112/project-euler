# encoding=utf-8
## SOLVED 2017/07/08
## 1258

# By using each of the digits from the set, {1, 2, 3, 4}, exactly once, and
# making use of the four arithmetic operations (+, −, *, /) and
# brackets/parentheses, it is possible to form different positive integer
# targets.

# For example,

# 8 = (4 * (1 + 3)) / 2
# 14 = 4 * (3 + 1 / 2)
# 19 = 4 * (2 + 3) − 1
# 36 = 3 * 4 * (2 + 1)

# Note that concatenations of the digits, like 12 + 34, are not allowed.

# Using the set, {1, 2, 3, 4}, it is possible to obtain thirty-one different
# target numbers of which 36 is the maximum, and each of the numbers 1 to 28 can
# be obtained before encountering the first non-expressible number.

# Find the set of four distinct digits, a < b < c < d, for which the longest set
# of consecutive positive integers, 1 to n, can be obtained, giving your answer
# as a string: abcd.

from collections import defaultdict

from helpers.sequence import take_n

def apply_operator(left, op, right):
    if op == '+':
        return left + right
    if op == '-':
        return left - right
    if op == '*':
        return left * right
    if op == '/':
        return left / right
    raise Exception('Invalid operator.')

def add_obtainable_values(obtainable_values, tokens, token_count):
    operators = '+-*/'
    for xs in take_n(tokens, token_count):
        for i, right in enumerate(xs):
            other_operands = tuple(xs[:i] + xs[i + 1:])
            for left in obtainable_values[other_operands]:
                k = tuple(sorted(list(other_operands) + [right]))
                for op in operators:
                    result = apply_operator(left, op, right)
                    if result:
                        obtainable_values[k].add(result)
                    result = apply_operator(right, op, left)
                    if result:
                        obtainable_values[k].add(result)

def euler():
    tokens = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    obtainable_values = defaultdict(lambda: set())
    for i in  range(10):
        obtainable_values[(i,)] = set([i])
    for i in range(2, 5):
        add_obtainable_values(obtainable_values, tokens, i)
    sequence_lengths = dict()
    for xs in take_n(tokens, 4):
        i = 1
        key = tuple(xs)
        while i in obtainable_values[key]:
            i += 1
        sequence_lengths[key] = i - 1
    max_index, max_value = max(sequence_lengths.items(), key = lambda x: x[1])
    return int(''.join(str(i) for i in max_index))
