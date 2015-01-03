# encoding=utf-8
## SOLVED 2013/12/21
## 1366

# 215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

# What is the sum of the digits of the number 2^1000?

def euler ():
    # return the sum of the digits of 2^1000
    return sum (int (char) for char in str (2 ** 1000))
