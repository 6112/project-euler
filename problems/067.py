# encoding=utf-8
## SOLVED 30/11/14
## 7273

# By starting at the top of the triangle below and moving to adjacent numbers
# on the row below, the maximum total from top to bottom is 23.

# 3
# 7 4
# 2 4 6
# 8 5 9 3

# That is, 3 + 7 + 4 + 9 = 23.

# Find the maximum total from top to bottom in triangle.txt (right click and
# 'Save Link/Target As...'), a 15K text file containing a triangle with
# one-hundred rows.

# NOTE: This is a much more difficult version of Problem 18. It is not possible
# to try every route to solve this problem, as there are 299 altogether! If you
# could check one trillion (1012) routes every second it would take over twenty
# billion years to check them all. There is an efficient algorithm to solve it.
# ;o)

import modules.file as fileutils

def euler ():
    # read the pyramid from the file
    pyramid = fileutils.list_from_file ('data/067.txt')
    # for each row, starting at the second from the bottom and going up
    for y in range (len (pyramid) - 2, -1, -1):
        # for each element of that row
        for x in range (y + 1):
            # add to it the highest of the two directly below it
            pyramid [y][x] += max (pyramid [y + 1][x], pyramid [y + 1][x + 1])
    # return the value at the top of the pyramid
    return pyramid [0][0]
