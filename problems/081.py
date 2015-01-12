# encoding=utf-8
## SOLVED 2015/01/04
## 427337

# In the 5 by 5 matrix below, the minimal path sum from the top left to the
# bottom right, by only moving to the right and down, is indicated in bold red
# and is equal to 2427.

# [example...]

# Find the minimal path sum, in matrix.txt (right click and "Save Link/Target
# As..."), a 31K text file containing a 80 by 80 matrix, from the top left to
# the bottom right by only moving right and down.

from helpers.file import *

def euler():
  # original matrix, read from the file
  original = list_from_file("data/081.txt", separator = ',')
  # dimensions of the matrix
  height = len(original)
  width = len(original[0])
  # another matrix with the same dimensions, filled with 0s.
  # each element will be the length of the shortest path from the upper left
  # corner to the corresponding tile.
  shortest = [[0 for x in range(width)] for y in range(height)]
  # the top left corner has the same value as in the original matrix
  shortest[0][0] = original[0][0]
  # fill the top and left borders, as there is only one path to get to them
  for y in range(1, height):
    shortest[y][0] = shortest[y - 1][0] + original[y][0]
  for x in range(1, width):
    shortest[0][x] = shortest[0][x - 1] + original[0][x]
  # fill the rest of the grid
  for y in range(1, height):
    for x in range(1, width):
      shortest[y][x] = min(shortest[y - 1][x], shortest[y][x - 1])
      shortest[y][x] += original[y][x]
  # return the length of the shortest path to get to the bottom right corner
  return shortest[height - 1][width - 1]
