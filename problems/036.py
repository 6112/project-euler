# encoding=utf-8
## SOLVED 25/12/13
## 872187

# The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

# Find the sum of all numbers, less than one million, which are palindromic in
# base 10 and base 2.

# (Please note that the palindromic number, in either base, may not include
# leading zeros.)

def euler ():
    accumulator = 0
    for number in range (1, 1000000):
        is_valid = is_palindromic (str (number))
        is_valid = is_valid and is_palindromic (to_binary (number))
        if is_valid:
            accumulator += number
    return accumulator

def to_binary (number):
    accumulator = []
    while number > 0:
        accumulator.append (number % 2)
        number //= 2
    return ''.join (map (str, accumulator [::-1]))

def is_palindromic (sequence):
    return sequence == sequence [::-1]
