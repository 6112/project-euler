# encoding=utf-8
## SOLVED 25/12/13
## 840

# If p is the perimeter of a right angle triangle with integral length sides,
# {a,b,c}, there are exactly three solutions for p = 120.

# {20,48,52}, {24,45,51}, {30,40,50}

# For which value of p ≤ 1000, is the number of solutions maximised?

from math import sqrt

def euler ():
    triangle_counts = [0 for i in range (1, 1000)]
    for a in range (1, 1000):
        for b in range (1, 1000):
            c = sqrt (a * a + b * b)
            if int (c) == c and a + b + c < 1000:
                triangle_counts [int (a + b + c)] += 1 
    return triangle_counts.index (max (triangle_counts))
