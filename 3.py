#!/usr/bin/python3
## SOLVED 19/12/13
## 6857

from modules.prime import *

BIG_NUMBER = 600851475143

def euler ():
    return max (prime_factors (BIG_NUMBER))

print (euler ())
