# encoding=utf-8
## SOLVED 2014/11/30
## 6531031914842725

# Consider the following "magic" 3-gon ring, filled with the numbers 1 to 6,
# and each line adding to nine.

# Working clockwise, and starting from the group of three with the numerically
# lowest external node (4,3,2 in this example), each solution can be described
# uniquely. For example, the above solution can be described by the set: 4,3,2;
# 6,2,1; 5,1,3.

# It is possible to complete the ring with four different totals: 9, 10, 11,
# and 12. There are eight solutions in total.

# Total	Solution Set

# 9	4,2,3; 5,3,1; 6,1,2
# 9	4,3,2; 6,2,1; 5,1,3
# 10	2,3,5; 4,5,1; 6,1,3
# 10	2,5,3; 6,3,1; 4,1,5
# 11	1,4,6; 3,6,2; 5,2,4
# 11	1,6,4; 5,4,2; 3,2,6
# 12	1,5,6; 2,6,4; 3,4,5
# 12	1,6,5; 3,5,4; 2,4,6

# By concatenating each group it is possible to form 9-digit strings; the
# maximum string for a 3-gon ring is 432621513.

# Using the numbers 1 to 10, and depending on arrangements, it is possible to
# form 16- and 17-digit strings. What is the maximum 16-digit string for a
# "magic" 5-gon ring?

from helpers.sequence import n_permutations

# numbers used in the magic pentagon
NUMBERS = list(range(1,11))

# length of the solution's string
SOLUTION_LENGTH = 16

def euler():
    # return value: maximum solution string
    highest = ""
    # for every starting set of 3 numbers
    for start in n_permutations(NUMBERS, 3):
        # numbers that aren't in 'start'
        remaining = set(NUMBERS) - set(start)
        # for each of the numbers that aren't in 'start'
        for x in remaining:
            # try to chain over it
            for c in chain(start, remaining, x):
                # convert to a string
                s = [str(n) for l in c for n in l]
                s = ''.join(s)
                # check if it's a valid solution
                is_valid = len(s) == SOLUTION_LENGTH and sum(c[0]) == sum(c[-1])
                # if valid, set new maximum if appropriate
                if is_valid and s > highest:
                    highest = s
    # return maximum
    return highest

# iterator for all solutions of the pentagon
def chain(start, rem, x):
    for c in chain_helper(start, rem, x):
        # add the second number from 'start' to the end of the chain
        c[-1].append(start[1])
        # add 'start' to the start of the chain
        c = [start] + c
        # check that the last sub-chain actually works in the chain
        if sum(c[0]) != sum(c[-1]):
            continue
        # sort the chain's sub-chains by their numerical value
        c = sorted(c)
        # reverse the order for the last sub-chains, to make them ascending
        # while keeping the first element as the lowest sub-chain
        c[1:] = c[-1:0:-1]
        # the sums must be equal, even in the last element
        yield c

def chain_helper(start, rem, x):
    # no numbers remaining, pass
    if not rem:
        return
    # calculate y for the next sequence of 3 numbers, [y,start[2],x]
    y = start[0] + start[1] - x
    # if y is actually in the remaining numbers
    if y in rem and x != y:
        # args for recursive call
        new_rem = rem - {x, y}
        new_start = [y, start[2], x]
        if len(new_rem) == 1:
            # only 1 element remaining: complete the chain
            a = list(new_rem)[0]
            yield [new_start] + [[a, new_start[2]]]
        else:
            # try to chain recursively
            for new_x in new_rem:
                for c in chain_helper(new_start, new_rem, new_x):
                    yield [new_start] + c
