# encoding=utf-8
## SOLVED 20/12/13
## 137846528820

# Starting in the top left corner of a 2x2 grid, and only being able to move to
# the right and down, there are exactly 6 routes to the bottom right corner.

# How many such routes are there through a 20x20 grid?

GRID_SIZE = 21

def euler ():
    # construct the 21x21 grid, whose elements are the number of possible paths
    # to reach that cell
    grid = [[0 for y in range (GRID_SIZE)] for x in range (GRID_SIZE)]
    # initialize the top and left borders with 1 everywhere
    for i in range (GRID_SIZE):
        grid [i][0] = 1
        grid [0][i] = 1
    # for each grid cell
    for y in range (1, GRID_SIZE):
        for x in range (1, GRID_SIZE):
            # this grid is equal to the sum of the one above it, and the one to
            # its left
            grid [y][x] = grid [y - 1][x] + grid [y][x - 1]
    # return the value of the last grid
    return grid [GRID_SIZE - 1][GRID_SIZE - 1]
