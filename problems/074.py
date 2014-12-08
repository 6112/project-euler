# encoding=utf-8
## SOLVED 7/12/14
## 402

# The number 145 is well known for the property that the sum of the factorial
# of its digits is equal to 145:

# 1! + 4! + 5! = 1 + 24 + 120 = 145

# Perhaps less well known is 169, in that it produces the longest chain of
# numbers that link back to 169; it turns out that there are only three such
# loops that exist:

# 169 → 363601 → 1454 → 169
# 871 → 45361 → 871
# 872 → 45362 → 872

# It is not difficult to prove that EVERY starting number will eventually get
# stuck in a loop. For example,

# 69 → 363600 → 1454 → 169 → 363601 (→ 1454)
# 78 → 45360 → 871 → 45361 (→ 871)
# 540 → 145 (→ 145)

# Starting with 69 produces a chain of five non-repeating terms, but the
# longest non-repeating chain with a starting number below one million is sixty
# terms.

# How many chains, with a starting number below one million, contain exactly
# sixty non-repeating terms?

MAX = 1000000

def euler():
    match_count = 0
    for n in range(1, MAX):
        if chain_length(n) == 60:
            match_count += 1
    return match_count

# cache for the chain_length() function
chain_cache = dict()
def chain_length(n):
    # set, and ordered list, for encountered numbers in the chain
    encountered = set()
    ordered = []
    # used to save data to cache before returning from thi sfunction
    def save(length):
        for i, k in enumerate(ordered):
            chain_cache[k] = length - i
    # repeat this until 'n' is saved in the cache, or until 'n' was encountered
    # before
    while True:
        if n in chain_cache:
            # save data to cache, and return based on what was found in cache
            save(len(encountered) + chain_cache[n])
            return len(encountered) + chain_cache[n]
        if n in encountered:
            break
        # save 'n' to the list of encountered numbers in the chain
        encountered.add(n)
        ordered.append(n)
        # calculate the next term in the chain
        digits = [int(c) for c in str(n)]
        acc = 0
        for d in digits:
            acc += factorial(d)
        n = acc
    # save data to cache
    save(len(encountered))
    # return the length of the chain
    return len(encountered)

# dictionary used for calculating factorials quickly for integers from 0 to 9
factorial_table = dict()
n = 1
for i in range(10):
    factorial_table[i] = n
    n *= i + 1

def factorial(n):
    return factorial_table[n]
