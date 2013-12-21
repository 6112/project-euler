#!/usr/bin/python3
## SOLVED 21/12/13
## 1366

# 215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

# What is the sum of the digits of the number 2^1000?

def euler ():
    return sum (int (char) for char in str (2 ** 1000))

print (euler ())
