# encoding=utf-8
## SOLVED 2014/11/25
## 272

# The square root of 2 can be written as an infinite continued fraction.

# The infinite continued fraction can be written, √2 = [1;(2)], (2) indicates
# that 2 repeats ad infinitum. In a similar way, √23 = [4;(1,3,1,8)].

# It turns out that the sequence of partial values of continued fractions for
# square roots provide the best rational approximations. Let us consider the
# convergents for √2.

# Hence the sequence of the first ten convergents for √2 are: 1, 3/2, 7/5,
# 17/12, 41/29, 99/70, 239/169, 577/408, 1393/985, 3363/2378, ...

# What is most surprising is that the important mathematical constant,
# e = [2; 1,2,1, 1,4,1, 1,6,1 , ... , 1,2k,1, ...].

# The first ten terms in the sequence of convergents for e are:
# 2, 3, 8/3, 11/4, 19/7, 87/32, 106/39, 193/71, 1264/465, 1457/536, ...

# The sum of digits in the numerator of the 10th convergent is 1+4+5+7=17.

# Find the sum of digits in the numerator of the 100th convergent of the
# continued fraction for e.

# index for the convergent of e that we want to obtain
NTH_CONVERGENT = 100

def euler():
    # numerator and denominator for the continued fraction
    numerator = 0
    denominator = 1
    # for each partial value, starting from the last, until the first
    for i in range(NTH_CONVERGENT - 2, -1, -1):
        # a is the current partial value (either 1, or 2k)
        a = 2 * (i // 3 + 1) if i % 3 == 1 else 1
        # calculate the next fraction using
        # 1 / (a + 1 / d) = d / (ad + n)
        (numerator, denominator) = (denominator, numerator + a * denominator)
    # add the integer 2 to the number (add 2 * denominator to the numerator)
    numerator += 2 * denominator
    return sum(int(c) for c in str(numerator))
