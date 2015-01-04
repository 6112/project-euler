# encoding=utf-8
## SOLVED 2014/01/04
## 425185

# In the 5 by 5 matrix below, the minimal path sum from the top left to the
# bottom right, by moving left, right, up, and down, is indicated in bold red
# and is equal to 2297.

# [example...]

# Find the minimal path sum, in matrix.txt (right click and "Save Link/Target
# As..."), a 31K text file containing a 80 by 80 matrix, from the top left to
# the bottom right by moving left, right, up, and down.

from helpers.file import *

from collections import deque

def euler():
  # original matrix, read from the file
  original = list_from_file("data/083.txt", separator = ',')
  # dimensions of the matrix
  height = len(original)
  width = len(original[0])
  # another matrix with the same dimensions, filled with 0s.
  # each element will be the length of the shortest path from the upper left
  # corner to the corresponding tile.
  shortest = [[0 for x in range(width)] for y in range(height)]
  # the top left corner has the same value as in the original matrix
  shortest[0][0] = original[0][0]
  # queue for (y,x) pairs for the tiles to check
  queue = deque([(0, 0)])
  # while there are tiles to check
  while queue:
    (y, x) = queue.popleft()
    # for each neighboring tile (v,u) inside the boundaries
    for (v, u) in neighbors(y, x, height, width):
      # if the shortest path to point (v,u) is unknown, or longer than the
      # length that would be obtained by going through (y,x)
      if shortest[v][u] == 0 or \
         shortest[v][u] > shortest[y][x] + original[v][u]:
        # the new shortest path is the path going through (y,x)
        shortest[v][u] = shortest[y][x] + original[v][u]
        # make a new (or first) check on tile (v,u) at some point
        queue.append((v, u))
  # return the shortest path to the bottom right corner
  return shortest[height - 1][width - 1]

# `yield` for each tile that is directly adjacent to the tile at (y,x).
# tiles outside the boundaries with width `w` and height `h` are not `yield`ed.
#
# the value `yield`ed is a (y,x) pair.
def neighbors(y, x, h, w):
  for d in (-1, 1):
    v = y
    u = x + d
    if in_bounds(u, v, h, w):
      yield (v, u)
    v = y + d
    u = x
    if in_bounds(u, v, h, w):
      yield (v, u)

def in_bounds(y, x, h, w):
  return y >= 0 and x >= 0 and y < h and x < w