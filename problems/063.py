# encoding=utf-8
## SOLVED 18/11/14
## 49

from math import log

def euler():
    # don't count duplicates, so use a set to keep track of numbers found
    found = set()
    # b has to be between 1 and 10
    for b in range(1, 11):
        for n in range(1, 50):
            if (b ** n) not in found and int(n * log(b, 10)) == n - 1:
                found.add(b ** n)
    # return the number of items found
    return len(found)