# encoding=utf-8
## SOLVED 2015/01/03
## 73162890

# A common security method used for online banking is to ask the user for three
# random characters from a passcode. For example, if the passcode was 531278,
# they may ask for the 2nd, 3rd, and 5th characters; the expected reply would
# be: 317.

# The text file, keylog.txt, contains fifty successful login attempts.

# Given that the three characters are always asked for in order, analyse the
# file so as to determine the shortest possible secret passcode of unknown
# length.

from helpers.file import *

def euler():
  # list of 3-char passwords attempts
  attempts = flattened_list_from_file("data/079.txt")
  attempts = [str(n) for n in attempts]
  # final password, will be concatenated into a string
  password = []
  # characters that are present in the password, but whose position is unknown
  char_pool = set()
  for n in attempts:
    for d in n:
      char_pool.add(d)
  # while there is a character whose position is unknown
  while char_pool:
    # set of all probable "first" character for the password (or simply next
    # character)
    probable_first = set(char_pool)
    # when a character is present as the 2nd or 3rd character in an attempt, it
    # means it cannot possibly be the first character (as there is one before 
    # it)
    for n in attempts:
      for d in n[1:]:
        if d in probable_first:
          probable_first.remove(d)
    # next digit in the password
    (first, ) = probable_first
    # add it to the password
    password.append(first)
    # we now know its position, so remove it from the char pool
    char_pool.remove(first)
    # remove the character from each 3-char attempt, preparing for the next
    # iteration
    for i,n in enumerate(attempts):
      if n and n[0] == first:
        attempts[i] = n[1:]
  # return the password, as a string
  return ''.join(password)
