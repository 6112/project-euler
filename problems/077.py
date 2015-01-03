# encoding=utf-8
## SOLVED 2014/01/03
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

solutions = [[]]

def euler():
  n = 10
  while chain(n, n) < 5000:
    n += 1
  return n

def chain(n, l):
  if n == 0:
    return 1
  if n < 2:
    return 0
  acc = 0
  for q in primes(l):
    acc += chain(n - q, q)
  return acc