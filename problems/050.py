#encoding=utf-8
## SOLVED 2014/04/17
## 997651

# The prime 41, can be written as the sum of six consecutive primes:

# 41 = 2 + 3 + 5 + 7 + 11 + 13

# This is the longest sum of consecutive primes that adds to a prime below
# one-hundred.

# The longest sum of consecutive primes below one-thousand that adds to a
# prime, contains 21 terms, and is equal to 953.

# Which prime, below one-million, can be written as the sum of the most
# consecutive primes?

import helpers.prime as prime

# highest value for the resulting prime
HIGHEST_PRIME = 1000000

def euler():
    # highest number of consecutive primes that add up to a prime
    highest_chain_length = 1
    # highest resulting sum that was found
    highest_chain = 2
    # for each prime
    for prime_number in prime.primes(HIGHEST_PRIME):
        # exit when it can't possibly be the start of a new chain
        if prime_number > HIGHEST_PRIME // highest_chain_length:
            break
        # start a chain from this prime number
        accumulator = prime_number
        # length of the current chain
        chain_length = 1
        # for each prime starting from here
        for chain_prime in prime.primes(HIGHEST_PRIME):
            # exit when outside the bounds
            if accumulator > HIGHEST_PRIME:
                break
            # skip the primes below the "prime_number" start
            if chain_prime > prime_number:
                # if it's a prime and the chain length is longer than the
                # longest chain so far
                if prime.is_prime(accumulator) and \
                        chain_length > highest_chain_length:
                    highest_chain_length = chain_length
                    highest_chain = accumulator
                # increase chain length and add the next prime
                chain_length += 1
                accumulator += chain_prime
    return highest_chain
