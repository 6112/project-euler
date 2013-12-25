def permutations (tokens):
    """Used as an iterator for all the permutations of a sequence.""" 
    if not tokens:
        yield []
        return
    for index, first in enumerate (tokens):
        rest = tokens [: index] + tokens [index + 1:]
        for permutation in permutations (rest):
            yield [first] + permutation

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
        rotation = rotate (tokens)
