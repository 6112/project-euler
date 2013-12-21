## SOLVED 19/12/13
## 906609

# A palindromic number reads the same both ways. The largest palindrome made
# from the product of two 2-digit numbers is 9009 = 91 x 99.

# Find the largest palindrome made from the product of two 3-digit numbers

def euler ():
    highest_palindrome = 0
    for a in range (100, 1000):
        for b in range (a, 1000):
            product = a * b
            if str (product) == str (product) [::-1]:
                highest_palindrome = max (highest_palindrome, product)
    return highest_palindrome
