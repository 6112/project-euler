#!/usr/bin/python3
## SOLVED 20/12/13
## 70600674

# In the 20×20 grid below, four numbers along a diagonal line have been marked 
# in red.

# [11.txt]

# The product of these numbers is 26 × 63 × 78 × 14 = 1788696.

# What is the greatest product of four adjacent numbers in the same direction
# (up, down, left, right, or diagonally) in the 20×20 grid?

def euler ():
    highest_product = 0
    grid = []
    with open ('11.txt') as grid_file:
        row = 0
        for line_with_spaces in grid_file:
            grid.append ([])
            line = line_with_spaces.rstrip ()
            for char_index in range (0, len (line), 3):
                grid [row].append (int (line [char_index : char_index + 2]))
            row += 1
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

print (euler ())
