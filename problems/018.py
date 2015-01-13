# encoding=utf-8
## SOLVED 2013/12/21
## 1074

# By starting at the top of the triangle below and moving to adjacent numbers on
# the row below, the maximum total from top to bottom is 23.

#    3
#   7 4
#  2 4 6
# 8 5 9 3

# That is, 3 + 7 + 4 + 9 = 23.

# Find the maximum total from top to bottom of the triangle below [018.txt]

import helpers.file as fileutils

def euler():
    # read the pyramid from the file
    pyramid = fileutils.list_from_file('data/018.txt')
    # for each row, starting at the second from the bottom and going up
    for y in range(len(pyramid) - 2, -1, -1):
        # for each element of that row
        for x in range(y + 1):
            # add to it the highest of the two directly below it
            pyramid [y][x] += max(pyramid [y + 1][x], pyramid [y + 1][x + 1])
    # return the value at the top of the pyramid
    return pyramid [0][0]
