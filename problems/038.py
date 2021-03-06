# encoding=utf-8
## SOLVED 2013/12/25
## 932718654

# Take the number 192 and multiply it by each of 1, 2, and 3:

# 192 × 1 = 192
# 192 × 2 = 384
# 192 × 3 = 576

# By concatenating each product we get the 1 to 9 pandigital, 192384576. We will
# call 192384576 the concatenated product of 192 and (1,2,3)

# The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and
# 5, giving the pandigital, 918273645, which is the concatenated product of 9
# and (1,2,3,4,5).

# What is the largest 1 to 9 pandigital 9-digit number that can be formed as the
# concatenated product of an integer with (1,2, ...  , n) where n > 1?

def euler():
    highest = 0
    for number in range(1, 100000):
        string = str(number)
        for n in range(2, 8):
            if len(string) > 9:
                break
            string += str(number * n)
            if is_pandigital(string):
                if int(string) > highest:
                    highest = int(string)
    return highest

def is_pandigital(sequence):
    return len(sequence) == 9 and \
      set(map(int, sequence)) == set(range(1, 10))
