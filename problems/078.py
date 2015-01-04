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
  # this is valid since partition(n) returns a value with a modulo applied
  while partition(n) != 0:
    n += 1
  return n

# list of partitions, used by partition(), and indirectly by next_p
ps = [0, 1]
# partition function; see Euler's pentagonal number theorem
#
# N.B.: all calculations are made with modulo DIVISOR
def partition(n):
  n += 1
  i = len(ps)
  while i <= n:
    ps.append(next_p(i, ps) % DIVISOR)
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
  return acc % DIVISOR

# helper function for partition(): calculate the k-th pentagonal number
#
# N.B.: all calculations are made with modulo DIVISOR
def pentagonal(k):
  return int(k * (3 * k - 1) / 2) % DIVISOR