# encoding=utf-8
## SOLVED 2015/01/10
## 2772

# By counting carefully it can be seen that a rectangular grid measuring 3 by 2
# contains eighteen rectangles:

# [example]

# Although there exists no rectangular grid that contains exactly two million 
# rectangles, find the area of the grid with the nearest solution.

# maximum possible size for a rectangle
MAX = 2000

# the "target" we are trying to reach
TARGET = 2000000

def euler():
    # (area, difference) tuple for the best match
    best_match = (0, 2000000)
    # for each possible width/height
    for height in range(1, MAX + 1):
        for width in range(1, height + 1):
            # the number of sub-rectangles is t(w)*t(h)
            rectangles = triangular(height) * triangular(width)
            # if it is closer to TARGET than previous best match, this is the
            # new best match
            if abs(TARGET - rectangles) < best_match[1]:
                best_match = (height * width, abs(TARGET - rectangles))
    # return the area for the best match
    return best_match[0]
    
# return the nth triangular number
def triangular(n):
    return n * (n + 1) // 2