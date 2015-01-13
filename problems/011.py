# encoding=utf-8
## SOLVED 2013/12/20
## 70600674

# In the 20x20 grid below, four numbers along a diagonal line have been marked 
# in red.

# [11.txt]

# The product of these numbers is 26 x 63 x 78 x 14 = 1788696.

# What is the greatest product of four adjacent numbers in the same direction
# (up, down, left, right, or diagonally) in the 20x20 grid?

import helpers.file as fileutils

def euler():
    # highest product of four adjacent numbers in the same direction
    highest_product = 0
    # read the file to get the grid
    grid = fileutils.list_from_file('data/011.txt')
    # horizontal products
    for row in grid:
        for x in range(len(grid [0]) - 3):
            highest_product = max(highest_product, product(row [x : x + 4]))
    # vertical products
    for x in range(len(grid [0])):
        column = [row [x] for row in grid]
        for y in range(len(grid) - 3):
            highest_product = max(highest_product, 
              product(column [y : y + 4]))
    # diagonal products from top-left to bottom-right
    for y in range(len(grid) - 3):
        for x in range(len(grid [0]) - 3):
            elements = [grid [y + i][x + i] for i in range(4)]
            highest_product = max(highest_product, product(elements))
    # highest products from bottom-left to top-right
    for y in range(len(grid) - 3):
        for x in range(3, len(grid [0])):
            elements = [grid [y + i][x - i] for i in range(4)]
            highest_product = max(highest_product, product(elements))
    # return the highest product
    return highest_product

def product(xs):
    """Return the product of the elements in an iterable."""
    accumulator = 1
    for x in xs:
        accumulator *= x
    return accumulator
