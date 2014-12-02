def permutations (tokens):
    """Used as an iterator for all the permutations of a sequence.""" 
    if not tokens:
        yield []
        return
    encountered = set ()
    for index, first in enumerate (tokens):
        if first not in encountered:
            rest = tokens [: index] + tokens [index + 1:]
            encountered.add(first)
            for permutation in permutations (rest):
                yield [first] + permutation

def n_permutations(tokens, n):
    """Used as an iterator for all n-permutations of a sequence."""
    if not tokens:
        yield []
        return
    if n == 0:
        yield []
        return
    encountered = set()
    for index, first in enumerate(tokens):
        if first not in encountered:
            rest = tokens[: index] + tokens[index + 1 :]
            encountered.add(first)
            for perm in n_permutations(rest, n - 1):
                yield [first] + perm

def take_n(tokens, n):
    """Used as an iterator for all possible combinations of n elements from
    tokens."""
    if not tokens:
        yield []
        return
    if n == 0:
        yield []
        return
    encountered = set()
    for index, first in enumerate(tokens):
        if first not in encountered:
            rest = tokens[index + 1 :]
            encountered.add(first)
            if n == 1:
                yield [first]
            else:
                for perm in take_n(rest, n - 1):
                    if perm:
                        yield [first] + perm

def is_permutation(xs, ys):
    """Returns True iff the two lists are permutations of eachother."""
    return sorted(xs) == sorted(ys)

def left_truncations (tokens):
    """Used as an iterator for all truncations of a sequence, from the left.
    For instance, left_truncations('123') yields '123', '12', and '1'."""
    while tokens:
        yield tokens
        tokens = tokens [: -1]

def right_truncations (tokens):
    """Used as an iterator for all truncations of a sequence, from the right.
    For instance, right_truncations('123' yields '123', '23', and '3'."""
    while tokens:
        yield tokens
        tokens = tokens [1 :]

def rotate (tokens):
    """Returns a rotated sequence from the given sequence. All elements are
    moved one position to the right, and the last element is placed at the
    beginning."""
    return tokens [-1 :] + tokens [: -1]

def rotations (tokens):
    """Used as an iterator for all rotations of a sequence, as per the rotate()
    function."""
    rotation = tokens
    for iterator in range (len (tokens)):
        yield rotation
        rotation = rotate (rotation)
