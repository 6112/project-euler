# encoding=utf-8
## SOLVED 26/12/14
## 161667

# It turns out that 12 cm is the smallest length of wire that can be bent to
# form an integer sided right angle triangle in exactly one way, but there are
# many more examples.

# 12 cm: (3,4,5)
# 24 cm: (6,8,10)
# 30 cm: (5,12,13)
# 36 cm: (9,12,15)
# 40 cm: (8,15,17)
# 48 cm: (12,16,20)

# In contrast, some lengths of wire, like 20 cm, cannot be bent to form an
# integer sided right angle triangle, and other lengths allow more than one
# solution to be found; for example, using 120 cm it is possible to form
# exactly three different integer sided right angle triangles.

# 120 cm: (30,40,50), (20,48,52), (24,45,51)

# Given that L is the length of the wire, for how many values of L ≤ 1,500,000
# can exactly one integer sided right angle triangle be formed?

import helpers.discreet as discreet

LIMIT = 1500000

def euler():
  table = {}
  m = 2
  while 2 * m * m < LIMIT:
    for n in range(1, m):
      if (m - n) % 2 == 1 and discreet.gcd(m, n) == 1:
        a = m * m - n * n
        b = 2 * m * n
        c = m * m + n * n
        l = a + b + c
        for L in range(l, LIMIT, l):
          if L in table:
            table[L] += 1
          else:
            table[L] = 1
    m += 1
  match_count = 0
  for k in table:
    if table[k] == 1:
      match_count += 1
  return match_count
