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
  return partition(MAX) - 1

# list of partitions, used by partition(), and indirectly by next_p
ps = [0, 1]
# partition function; see Euler's pentagonal number theorem
#
# N.B.: all calculations are made with modulo DIVISOR
def partition(n):
  n += 1
  i = len(ps)
  while i <= n:
    ps.append(next_p(i, ps))
    i += 1
  return ps[n]

# helper function for partition(): calculate the next partition
#
# N.B.: all calculations are made with modulo DIVISOR
def next_p(n, ps):
  acc = 0
  for dk in (-1, 1):
    k = dk
    q = pentagonal(k)
    while q < n:
      acc += int(((-1) ** (k - 1)) * ps[n - q])
      k += dk
      q = pentagonal(k)
  return acc

# helper function for partition(): calculate the k-th pentagonal number
#
# N.B.: all calculations are made with modulo DIVISOR
def pentagonal(k):
  return int(k * (3 * k - 1) / 2)
