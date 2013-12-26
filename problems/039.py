# encoding=utf-8
## SOLVED 25/12/13
## 840

# If p is the perimeter of a right angle triangle with integral length sides,
# {a,b,c}, there are exactly three solutions for p = 120.

# {20,48,52}, {24,45,51}, {30,40,50}

# For which value of p ≤ 1000, is the number of solutions maximised?

from math import sqrt

def euler ():
    highest_count = 0
    highest_perimeter = 0
    for perimeter in range (1, 1000):
        count = integral_triangles_count (perimeter)
        if count > highest_count:
            highest_perimeter = perimeter
            highest_count = count
    return highest_perimeter

def integral_triangles_count (perimeter):
    count = 0
    cache = {}
    print (perimeter)
    for a in range (1, perimeter // 2):
        for b in range (1, perimeter - 2 * a):
            c = sqrt (a * a + b * b)
            if not c in cache and a + b + c == perimeter and int (c) == c:
                count += 1
                cache [c] = True
    return count
