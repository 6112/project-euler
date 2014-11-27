# encoding = utf-8
## SOLVED 26/11/14
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

from modules.file import  *

def euler():
  rows = list_from_file("data/067.txt") 
  for y in range(len(rows) - 1, 0, -1):
    for x in range(y):
      rows[y - 1][x] += max(rows[y][x], rows[y][x + 1])
  return rows[0][0]
