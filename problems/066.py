# encoding=utf-8
## SOLVED 2014/11/29
## 661

# Consider quadratic Diophantine equations of the form:

# x^2 – Dy^2 = 1

# For example, when D=13, the minimal solution in x is 649^2 – 13×180^2 = 1.

# It can be assumed that there are no solutions in positive integers when D is
# square.

# By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the
# following:

# 3^2 – 2×2^2 = 1
# 2^2 – 3×1^2 = 1
# 9^2 – 5×4^2 = 1
# 5^2 – 6×2^2 = 1
# 8^2 – 7×3^2 = 1

# Hence, by considering minimal solutions in x for D ≤ 7, the largest x is
# obtained when D=5.

# Find the value of D ≤ 1000 in minimal solutions of x for which the largest
# value of x is obtained.

from math import sqrt

LIMIT = 1000

# see http://mathworld.wolfram.com/PellEquation.html
def euler():
    highest_x = 0
    highest_D = 0
    for D in range(2, LIMIT + 1):
        fract = continued_fraction(D)
        if fract[1]: # if not a square
            # length of the repeating partials
            r = len(fract[1])
            # list for int(sqrt(D)), followed by partials
            a = [fract[0]] + fract[1]
            # p[n]/q[n] is the nth convergent fraction for sqrt(D)
            ps = [a[0], a[0] * a[1] + 1]
            qs = [1, a[1]]
            for n in range(1, 2 * r + 2):
                a_n = a[1 + (n % r)]
                ps.append(a_n * ps[n] + ps[n-1])
                qs.append(a_n * qs[n] + qs[n-1])
                # the solution x/y will always be a convergent for sqrt(D)
                x = ps[n + 1]
                y = qs[n + 1]
                if x * x - D * y * y == 1:
                    if x > highest_x:
                        highest_x = x
                        highest_D = D
                    break
    return highest_D

def continued_fraction(S):
    if is_square(S):
        return (int(sqrt(S)), [])
    xs = []
    m = m0 = 0
    d = d0 = 1
    a = a0 = int(sqrt(S))
    while a != 2 * a0:
        m = d * a - m
        d = (S - m * m) / d
        a = int((a0 + m) / d)
        xs.append(a)
    return (a0, xs)

def is_square(n):
    return int(sqrt(n)) == sqrt(n)
