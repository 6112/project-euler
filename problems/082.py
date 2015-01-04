# encoding=utf-8
## SOLVED 2014/01/04
## 260324

# NOTE: This problem is a more challenging version of Problem 81.

# The minimal path sum in the 5 by 5 matrix below, by starting in any cell in
# the left column and finishing in any cell in the right column, and only moving
# up, down, and right, is indicated in red and bold; the sum is equal to 994.

# Find the minimal path sum, in matrix.txt (right click and "Save Link/Target
# As..."), a 31K text file containing a 80 by 80 matrix, from the left column to
# the right column.

from helpers.file import *

def euler():
  # original matrix, read from the file
  original = list_from_file("data/082.txt", separator = ',')
  # dimensions of the matrix
  height = len(original)
  width = len(original[0])
  # another matrix with the same dimensions, filled with 0.
  # each element will be the length of the shortest path from the left border to
  # the corresponding tile.
  costs = [[0 for x in range(width)] for y in range(height)]
  # the left border is the same as in the original
  for y in range(height):
    costs[y][0] = original[y][0]
  # for each column
  for x in range(1, width):
    # fill the column with the value that it takes to reach each cell from the
    # one immediately to its left
    for y in range(height):
      costs[y][x] = costs[y][x - 1] + original[y][x]
    # for each tile in the column, check if there is actually another, shorter
    # way to reach it (moving up and down from another tile in the same column)
    for y in range(height):
      # for each other starting tile in the same column, calculate the cost for
      # moving from that tile to the "current" tile `y`
      for start in range(height):
        acc = costs[start][x - 1] + original[y][x]
        for i in range(start, y, sg(y - start)):
          acc += original[i][x]
        # if the path is shorter by moving up/down than by coming from the
        # tile immediately to the left, then do that immediately
        if acc < costs[y][x]:
          costs[y][x] = acc
  # return the lowest value in the right border (the shortest path to reach the
  # right border)
  return min(costs[y][width - 1] for y in range(height))

# return the sign of x (1 if positive, -1 if negative).
# sg(0) returns 1.
def sg(x):
    return (1 if x >= 0 else -1)