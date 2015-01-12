# encoding=utf-8
## SOLVED 2015/01/10
## 1818

# A spider, S, sits in one corner of a cuboid room, measuring 6 by 5 by 3, and a
# fly, F, sits in the opposite corner. By travelling on the surfaces of the room 
# the shortest "straight line" distance from S to F is 10 and the path is shown
# on the diagram.

# [drawing of the cuboid]

# However, there are up to three "shortest" path candidates for any given cuboid
# and the shortest route doesn't always have integer length.

# It can be shown that there are exactly 2060 distinct cuboids, ignoring 
# rotations, with integer dimensions, up to a maximum size of M by M by M, for
# which the shortest route has integer length when M = 100. This is the least
# value of M for which the number of solutions first exceeds two thousand; the
# number of solutions when M = 99 is 1975.

# Find the least value of M such that the number of solutions first exceeds one
# million.

import math

# when to stop looking for more matches
MAX = 1000000

def euler():
    # number of matches found so far
    matches = 0
    # size of the longest side
    a = 1
    # for each a
    while True:
        # x = b + c, if the prism is of size a by b by c
        for x in range(1, 2 * a + 1):
            # shortest path inside the prism, L^2 = a^2 + (b + c)^2 = a^2 + x^2
            L = math.sqrt(a * a + x * x)
            if int(L) == L:
                # add the number of possible (b,c) combinations that are shorter
                # than a, and that satisfy x = b + c
                matches += count_ways(x, a)
            # value found, return the length of the longest side of the prism
            if matches > MAX:
                return a
        a += 1
    
# return the number of (a,b) sorted integers pairs, such that a <= maximum and
# b <= maximum, and a + b = n.
def count_ways(n, maximum):
    k = n // 2
    if maximum < n:
        k -= (n - maximum - 1)
    return k