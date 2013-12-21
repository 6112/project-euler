#!/usr/bin/python3
## SOLVED 20/12/13
## 70600674

# In the 20x20 grid below, four numbers along a diagonal line have been marked 
# in red.

# [11.txt]

# The product of these numbers is 26 x 63 x 78 x 14 = 1788696.

# What is the greatest product of four adjacent numbers in the same direction
# (up, down, left, right, or diagonally) in the 20x20 grid?

from modules.file import *

def euler ():
    highest_product = 0
    grid = list_from_file ('data/11.txt')
    for row in grid:
        for x in range (len (grid [0]) - 3):
            highest_product = max (highest_product, product (row [x : x + 4]))
    for x in range (len (grid [0])):
        column = [row [x] for row in grid]
        for y in range (len (grid) - 3):
            highest_product = max (highest_product, product (column [y : y + 4]))
    for y in range (len (grid) - 3):
        for x in range (len (grid [0]) - 3):
            elements = [grid [y + i][x + i] for i in range (4)]
            highest_product = max (highest_product, product (elements))
    for y in range (len (grid) - 3):
        for x in range (3, len (grid [0])):
            elements = [grid [y + i][x - i] for i in range (4)]
            highest_product = max (highest_product, product (elements))
    return highest_product

def product (xs):
    accumulator = 1
    for x in xs:
        accumulator *= x
    return accumulator
