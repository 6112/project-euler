# encoding=utf-8
## SOLVED
## 743

# For a number written in Roman numerals to be considered valid there are basic
# rules which must be followed. Even though the rules allow some numbers to be
# expressed in more than one way there is always a "best" way of writing a
# particular number.

# For example, it would appear that there are at least six ways of writing the
# number sixteen:

# IIIIIIIIIIIIIIII
# VIIIIIIIIIII
# VVIIIIII
# XIIIIII
# VVVI
# XVI

# However, according to the rules only XIIIIII and XVI are valid, and the last
# example is considered to be the most efficient, as it uses the least number of
# numerals.

# The 11K text file, roman.txt (right click and 'Save Link/Target As...'),
# contains one thousand numbers written in valid, but not necessarily minimal,
# Roman numerals; see About... Roman Numerals for the definitive rules for this
# problem.

# Find the number of characters saved by writing each of these in their minimal form.

# Note: You can assume that all the Roman numerals in the file contain no more
# than four consecutive identical units.

import re

def euler():
    acc = 0
    with open('data/089.txt') as f:
        for roman in f:
            roman = roman.rstrip()
            decimal = roman_to_decimal(roman)
            converted = decimal_to_roman(decimal)
            acc += len(roman) - len(converted)
    return acc

rx = re.compile('(.)\\1*')
def roman_to_decimal(s):
    numerals = {
        'M': 1000,
        'D': 500,
        'C': 100,
        'L': 50,
        'X': 10,
        'V': 5,
        'I': 1
    }
    def numeral(i):
        return numerals[groups[i][0]]
    def group_length(i):
        return groups[i][1]
    groups = []
    for match in re.finditer(rx, s):
        groups.append((match.group(1), len(match.group(0))))
    acc = 0
    last_group = numeral(0) * group_length(0)
    for i in range(1, len(groups)):
        if numeral(i - 1) < numeral(i):
            acc -= last_group
        else:
            acc += last_group
        last_group = numeral(i) * group_length(i)
    acc += last_group
    return acc

def decimal_to_roman(n):
    acc = ''
    numerals = [('M', 1000),
                ('CM', 900),
                ('D', 500),
                ('CD', 400),
                ('C', 100),
                ('XC', 90),
                ('L', 50),
                ('XL', 40),
                ('X', 10),
                ('IX', 9),
                ('V', 5),
                ('IV', 4),
                ('I', 1)]
    for numeral, value in numerals:
        while n >= value:
            acc += numeral
            n -= value
    return acc
