#!/usr/bin/python3
## SOLVED 21/12/13
## 1074

# By starting at the top of the triangle below and moving to adjacent numbers on
# the row below, the maximum total from top to bottom is 23.

#    3
#   7 4
#  2 4 6
# 8 5 9 3

# That is, 3 + 7 + 4 + 9 = 23.

# Find the maximum total from top to bottom of the triangle below:

from modules.file import *

def euler ():
    pyramid = list_from_file ('data/18.txt')
    for y in range (len (pyramid) - 2, -1, -1):
        for x in range (y + 1):
            pyramid [y][x] += max (pyramid [y + 1][x], pyramid [y + 1][x + 1])
    return pyramid [0][0]
