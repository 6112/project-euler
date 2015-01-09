# encoding=utf-8
## SOLVED 2015/01/03
## 71

# It is possible to write ten as the sum of primes in exactly five different
# ways:

# 7 + 3
# 5 + 5
# 5 + 3 + 2
# 3 + 3 + 2 + 2
# 2 + 2 + 2 + 2 + 2

# What is the first value which can be written as the sum of primes in over five
# thousand different ways?

from helpers.prime import *

MAX = 100

def euler():
  n = 10
  while chain(n, n) < 5000:
    n += 1
  return n

# returns the number of possible ways to write `n` as a sum of primes, where
# each prime is less than or equal to `l`
def chain(n, l):
  # 0 means the previous number was a prime
  if n == 0:
    return 1
  # 1 or a negative value, no way to write it as a prime
  if n < 2:
    return 0
  # otherwise, chain through each possibility: for each prime q, see how many
  # ways there are to write `n-q` as a sum of primes, where all the other
  # primes are less than or equal to `q`
  acc = 0
  for q in primes(l):
    acc += chain(n - q, q)
  return acc
