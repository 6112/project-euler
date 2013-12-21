## SOLVED 19/12/13
## 6857

# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

from modules.prime import *

BIG_NUMBER = 600851475143

def euler ():
    return max (prime_factors (BIG_NUMBER))
