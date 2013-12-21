## SOLVED 21/12/13
## 648

# n! means n x (n - 1) x ... x 3 x 2 x 1

# For example, 10! = 10 x 9 x ... x 3 x 2 x 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

# Find the sum of the digits in the number 100!

NUMBER = 100

def euler ():
    return sum (map (int, str (factorial (NUMBER))))

def factorial (number):
    accumulator = 1
    for n in range (1, number + 1):
        accumulator *= n
    return accumulator