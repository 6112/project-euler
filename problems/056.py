# encoding=utf-8
## SOLVED 20/10/13
## 972

# A googol (10100) is a massive number: one followed by one-hundred zeros;
# 100100 is almost unimaginably large: one followed by two-hundred zeros.
# Despite their size, the sum of the digits in each number is only 1.
 
# Considering natural numbers of the form, ab, where a, b < 100, what is the
# maximum digital sum?

HIGHEST_VALUE = 100

def euler():
  highest_sum = 0
  for a in range(1, HIGHEST_VALUE):
    for b in range(1, HIGHEST_VALUE):
      highest_sum = max(highest_sum, sum([int(c) for c in str(a ** b)]))
  return highest_sum
