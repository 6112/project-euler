#encoding=utf-8
## SOLVED 2014/04/18
## 4075

# There are exactly ten ways of selecting three from five, 12345:

# 123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

# In combinatorics, we use the notation, 5_C_3 = 10.

# In general,
# n_C_r = n! / (r! * (n - r)!)

# It is not until n = 23, that a value exceeds one-million: 23_C_10 = 1144066.

# How many, not necessarily distinct, values of  n_C_r, for 1 ≤ n ≤ 100, are
# greater than one-million?

# highest value for 'n'
HIGHEST_N = 100

# the minimum value for an answer to be valid
THRESHOLD = 1000000

def euler():
    # number of values above one million
    answer_count = 0
    # for each value of n
    for n in range(1, HIGHEST_N + 1):
        # for each value of r, from 1 to n - 1
        for r in range(1, n):
            # if the number of possibilities is higher than one million
            if factorial(n) / (factorial(r) * factorial(n - r)) > THRESHOLD:
                # increment the number of answers
                answer_count += 1
    # return the number of answers
    return answer_count

# optimizes the factorial() function through memoization
factorial_cache = {0: 1}
def factorial(n):
    """Returns the factorial of n."""
    # use cache if possible
    if n in factorial_cache:
        return factorial_cache[n]
    # otherwise, fill cache recursively, and *then* use it
    else:
        factorial_cache[n] = n * factorial(n - 1)
        return n * factorial(n - 1)
