#encoding=utf-8
## SOLVED 2014/04/10
## 162

# The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so
# the first ten triangle numbers are:
 
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

# By converting each letter in a word to a number corresponding to its
# alphabetical position and adding these values we form a word value. For
# example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word
# value is a triangle number then we shall call the word a triangle word.

# Using words.txt (right click and 'Save Link/Target As...'), a 16K text file
# containing nearly two-thousand common English words, how many are triangle
# words?

import helpers.file as fileutils

# arbitrary value for the highest reachable triangle number
MAX = 1000

def euler():
    # set of the triangle numbers until an arbitrary maximum number
    triangles = set()
    # generate triangle numbers
    n = 1
    highest_triangle = 0
    while highest_triangle < MAX:
        highest_triangle = n * (n + 1) // 2
        triangles.add(highest_triangle)
        n += 1
    # read the words and put them into a list of strings
    words = fileutils.flattened_list_from_file('data/042.txt',
            separator = ',', convert_to = str)
    # strip the quote-sign from the strings, leaving only the word
    words = [word.replace('"', '') for word in words]
    # accumulator for the final answer, the number of triangle words
    triangle_word_count = 0
    # count the number of triangle words
    for word in words:
        if word_to_int(word) in triangles:
            triangle_word_count += 1
    # return it
    return triangle_word_count

def word_to_int(word):
    """Returns the sum of the 'letter value' of each letter in the word.

    ('a' = 1, 'b' = 2, 'c' = 3, ...)"""
    return sum(ord(letter) - ord('a') + 1 for letter in word.lower())
