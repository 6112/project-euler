# encoding=utf-8
## SOLVED 2014/01/03
## 55374

# Let p(n) represent the number of different ways in which n coins can be
# separated into piles. For example, five coins can separated into piles in
# exactly seven different ways, so p(5)=7.

# OOOOO
# OOOO   O
# OOO   OO
# OOO   O   O
# OO   OO   O
# OO   O   O   O
# O   O   O   O   O

# Find the least value of n for which p(n) is divisible by one million.

DIVISOR = 1000000

def euler():
  n = 2
  while partition(n) % DIVISOR != 0:
    n += 1
  return n

ps = [0, 1]
def partition(n):
  n += 1
  i = len(ps)
  while i <= n:
    ps.append(next_p(i, ps) % DIVISOR)
    i += 1
  return ps[n]

def next_p(n, ps):
  acc = 0
  for dk in (-1, 1):
    k = dk
    q = pentagonal(k)
    while q < n:
      acc += int(((-1) ** (k - 1)) * ps[n - q])
      k += dk
      q = pentagonal(k)
  return acc % DIVISOR

def pentagonal(k):
  return int(k * (3 * k - 1) / 2) % DIVISOR