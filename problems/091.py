# encoding=utf-8
## SOLVED 2017/07/08
## 14234

# The points P (x1, y1) and Q (x2, y2) are plotted at integer co-ordinates and
# are joined to the origin, O(0,0), to form ΔOPQ.

# There are exactly fourteen triangles containing a right angle that can be
# formed when each co-ordinate lies between 0 and 2 inclusive; that is, 0 ≤ x1,
# y1, x2, y2 ≤ 2.

# Given that 0 ≤ x1, y1, x2, y2 ≤ 50, how many right triangles can be formed?

from helpers.discreet import gcd

N = 50

def euler():
    # there are 3*N**2 triangles that have one of those 3 shapes:
    # o--o   o  o
    # | /   /|  |\
    # |/   / |  | \
    # o   o--o  o--o
    acc = 3 * N ** 2
    # The other triangles have a first point with direction vector d:
    # d = (a, b) = (x, y) / gcd(x, y)
    #
    # And the second line is perpendicular to d. So it has a direction vector
    # of either u or v, and fits within the dimensions of the grid:
    # u = (+b, -a)
    # v = (-b, +a)
    #
    # So for each point (x, y) with x!=0 and y!=0, we just count how many
    # multiples of u or v can fit in the grid, starting at origin point (x, y).
    for y in range(1, N + 1):
        for x in range(1, N + 1):
            divisor = int(gcd(x, y))
            (a, b) = (x // divisor, y // divisor)
            left_triangles = min(y // a, (N - x) // b)
            right_triangles = min((N - y) // a, x // b)
            acc += left_triangles
            acc += right_triangles
    return acc
