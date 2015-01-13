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

import helpers.discreet as discreet

MAX = 100

def euler():
  return discreet.partition(MAX) - 1
