#encoding=utf-8
## SOLVED 2014/05/07
## 249

# If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.

# Not all numbers produce palindromes so quickly. For example,

# 349 + 943 = 1292,
# 1292 + 2921 = 4213
# 4213 + 3124 = 7337

# That is, 349 took three iterations to arrive at a palindrome.

# Although no one has proved it yet, it is thought that some numbers, like 196,
# never produce a palindrome. A number that never forms a palindrome through
# the reverse and add process is called a Lychrel number. Due to the
# theoretical nature of these numbers, and for the purpose of this problem, we
# shall assume that a number is Lychrel until proven otherwise. In addition you
# are given that for every number below ten-thousand, it will either (i) become
# a palindrome in less than fifty iterations, or, (ii) no one, with all the
# computing power that exists, has managed so far to map it to a palindrome. In
# fact, 10677 is the first number to be shown to require over fifty iterations
# before producing a palindrome: 4668731596684224866951378664 (53 iterations,
# 28-digits).

# Surprisingly, there are palindromic numbers that are themselves Lychrel
# numbers; the first example is 4994.

# How many Lychrel numbers are there below ten-thousand?

# NOTE: Wording was modified slightly on 24 April 2007 to emphasise the
# theoretical nature of Lychrel numbers.

HIGHEST_VALUE = 10000

HIGHEST_ITERATION_COUNT = 50

def euler():
  # number of lychrel numbers fount
  lychrel_count = 0
  # check every integer in a given range
  for n in range(1, HIGHEST_VALUE):
    if is_lychrel(n):
      lychrel_count += 1
  # return the number of lychrel numbers found
  return lychrel_count

def is_lychrel(n):
  """Return True iff the given integer is a (supposed) Lychrel number."""
  # try a given number of iterations
  for i in range(HIGHEST_ITERATION_COUNT):
    # add the reverse number
    n += int("".join(reversed(str(n))))
    # if the result is palindromic, it's not a lychrel number
    if is_palindromic(n):
      return False
  return True

def is_palindromic(n):
  """Return True iff the given integer is palindromic."""
  xs = str(n)
  return xs == "".join(reversed(xs))
