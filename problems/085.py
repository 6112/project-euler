# encoding=utf-8
## SOLVED 2015/01/10
## 2772

# By counting carefully it can be seen that a rectangular grid measuring 3 by 2
# contains eighteen rectangles:

# [example]

# Although there exists no rectangular grid that contains exactly two million 
# rectangles, find the area of the grid with the nearest solution.

MAX = 2000

TARGET = 2000000

def euler():
    best_match = (0, 2000000)
    for height in range(1, MAX + 1):
        for width in range(1, height + 1):
            rectangles = triangular(height) * triangular(width)
            if abs(TARGET - rectangles) < best_match[1]:
                best_match = (height * width, abs(TARGET - rectangles))
    return best_match[0]
    
def triangular(n):
    return n * (n + 1) // 2
    
if __name__ == '__main__':
    print(euler())
