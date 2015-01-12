# encoding=utf-8
## SOLVED 2013/12/25
## 840

# If p is the perimeter of a right angle triangle with integral length sides,
# {a,b,c}, there are exactly three solutions for p = 120.

# {20,48,52}, {24,45,51}, {30,40,50}

# For which value of p ≤ 1000, is the number of solutions maximised?

import math

MAX = 1000

def euler ():
    triangle_counts = [0 for i in range (1, MAX)]
    for a in range (1, MAX):
        for b in range (1, MAX):
            c = math.sqrt (a * a + b * b)
            if int (c) == c and a + b + c < MAX:
                triangle_counts [int (a + b + c)] += 1 
    return triangle_counts.index (max (triangle_counts))
