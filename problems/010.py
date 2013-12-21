## SOLVED 19/12/13
## 142913828922

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

from modules.prime import *

HIGHEST_VALUE = 2000000

def euler ():
    return sum (primes (HIGHEST_VALUE))
