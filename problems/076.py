# encoding=utf-8
## SOLVED 2015/01/02
## 190569291

# It is possible to write five as a sum in exactly six different ways:

# 4 + 1
# 3 + 2
# 3 + 1 + 1
# 2 + 2 + 1
# 2 + 1 + 1 + 1
# 1 + 1 + 1 + 1 + 1

# How many different ways can one hundred be written as a sum of at least two
# positive integers?

MAX = 100

def euler():
  return chain(MAX + 1)

def chain(n):
  ps = []
  ps.append(0)
  ps.append(1)
  for i in range(2, n + 1):
    ps.append(next_p(i, ps))
  return ps[n] - 1

def next_p(n, ps):
  acc = 0
  for dk in (-1, 1):
    k = dk
    q = pentagonal(k)
    while q < n:
      acc += ((-1) ** (k - 1)) * ps[n - q]
      k += dk
      q = pentagonal(k)
  return int(acc)

def pentagonal(k):
  return int(k * (3 * k - 1) / 2)