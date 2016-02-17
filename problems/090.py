# encoding=utf-8
## SOLVED 2016/02/17
## 1217

# Each of the six faces on a cube has a different digit (0 to 9) written on it;
# the same is done to a second cube. By placing the two cubes side-by-side in
# different positions we can form a variety of 2-digit numbers.

# For example, the square number 64 could be formed:

# (6)(4)

# In fact, by carefully choosing the digits on both cubes it is possible to
# display all of the square numbers below one-hundred: 01, 04, 09, 16, 25, 36,
# 49, 64, and 81.

# For example, one way this can be achieved is by placing {0, 5, 6, 7, 8, 9} on
# one cube and {1, 2, 3, 4, 8, 9} on the other cube.

# However, for this problem we shall allow the 6 or 9 to be turned upside-down
# so that an arrangement like {0, 5, 6, 7, 8, 9} and {1, 2, 3, 4, 6, 7} allows
# for all nine square numbers to be displayed; otherwise it would be impossible
# to obtain 09.

# In determining a distinct arrangement we are interested in the digits on each
# cube, not the order.

# {1, 2, 3, 4, 5, 6} is equivalent to {3, 6, 4, 1, 2, 5}
# {1, 2, 3, 4, 5, 6} is distinct from {1, 2, 3, 4, 5, 9}

# But because we are allowing 6 and 9 to be reversed, the two distinct sets in
# the last example both represent the extended set {1, 2, 3, 4, 5, 6, 9} for the
# purpose of forming 2-digit numbers.

# How many distinct arrangements of the two cubes allow for all of the square
# numbers to be displayed?

def euler():
    digits = list(range(0, 10))
    acc = 0
    for d1 in choose(digits, 6):
        for d2 in choose(digits, 6):
            if check_pair(d1, d2):
                acc += 1
    return acc // 2

# square the number, and return a tuple with each element being a digit from the
# square.
# 9 is replaced with 6.
def square_tuple(i):
    s = "%02d" % (i * i)
    return tuple(map(lambda c: int(c) if c != '9' else 6, s))

# checks if a pair of die can write the squares of all numbers from 1 to 9
def check_pair(d1, d2):
    for i in range(1, 10):
        (a, b) = square_tuple(i)
        works = False
        for c, d in ((a, b),(b,a)):
            if c in d1 and d in d2:
                works = True
        if not works:
            return False
    return True

# generate all the choices of `k` elements from the list `xs`, as sets.
def choose(xs, k):
    if k <= 0:
        yield set()
        return
    if k > len(xs):
        return
    for c in choose(xs[1:], k - 1):
        if xs[0] != 9:
            c.add(xs[0])
        else:
            # treat 9 as if it were 6
            c.add(6)
        yield c
    for c in choose(xs[1:], k):
        yield c
