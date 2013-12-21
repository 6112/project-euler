#!/usr/bin/python3
## SOLVED 20/12/13
## 137846528820

# Starting in the top left corner of a 2x2 grid, and only being able to move to
# the right and down, there are exactly 6 routes to the bottom right corner.

# How many such routes are there through a 20x20 grid?

GRID_SIZE = 21

def euler ():
    grid = [[0 for y in range (GRID_SIZE)] for x in range (GRID_SIZE)]
    for i in range (GRID_SIZE):
        grid [i][0] = 1
        grid [0][i] = 1
    for y in range (1, GRID_SIZE):
        for x in range (1, GRID_SIZE):
            grid [y][x] = grid [y - 1][x] + grid [y][x - 1]
    return grid [GRID_SIZE - 1][GRID_SIZE - 1]

print (euler ())
