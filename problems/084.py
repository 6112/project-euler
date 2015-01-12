# encoding=utf-8
## SOLVED 2015/01/09
## 101524

# In the game, Monopoly, the standard board is set up in the following way:

# [drawing of a monopoly board]

# A player starts on the GO square and adds the scores on two 6-sided dice to
# determine the number of squares they advance in a clockwise direction.
# Without any further rules we would expect to visit each square with equal
# probability: 2.5%. However, landing on G2J (Go To Jail), CC (community
# chest), and CH (chance) changes this distribution.

# In addition to G2J, and one card from each of CC and CH, that orders the
# player to go directly to jail, if a player rolls three consecutive doubles,
# they do not advance the result of their 3rd roll. Instead they proceed
# directly to jail.

# At the beginning of the game, the CC and CH cards are shuffled. When a player
# lands on CC or CH they take a card from the top of the respective pile and,
# after following the instructions, it is returned to the bottom of the pile.
# There are sixteen cards in each pile, but for the purpose of this problem we
# are only concerned with cards that order a movement; any instruction not
# concerned with movement will be ignored and the player will remain on the
# CC/CH square.

    # Community Chest (2/16 cards):
        # Advance to GO
        # Go to JAIL
    # Chance (10/16 cards):
        # Advance to GO
        # Go to JAIL
        # Go to C1
        # Go to E3
        # Go to H2
        # Go to R1
        # Go to next R (railway company)
        # Go to next R
        # Go to next U (utility company)
        # Go back 3 squares.

# The heart of this problem concerns the likelihood of visiting a particular
# square. That is, the probability of finishing at that square after a roll.
# For this reason it should be clear that, with the exception of G2J for which
# the probability of finishing on it is zero, the CH squares will have the
# lowest probabilities, as 5/8 request a movement to another square, and it is
# the final square that the player finishes at on each roll that we are
# interested in. We shall make no distinction between "Just Visiting" and being
# sent to JAIL, and we shall also ignore the rule about requiring a double to
# "get out of jail", assuming that they pay to get out on their next turn.

# By starting at GO and numbering the squares sequentially from 00 to 39 we can
# concatenate these two-digit numbers to produce strings that correspond with
# sets of squares.

# Statistically it can be shown that the three most popular squares, in order,
# are JAIL (6.24%) = Square 10, E3 (3.18%) = Square 24, and GO (3.09%) = Square
# 00. So these three most popular squares can be listed with the six-digit
# modal string: 102400.

# If, instead of using two 6-sided dice, two 4-sided dice are used, find the
# six-digit modal string.

# number of tiles on the grid
GRID_SIZE = 40 

# number of sides on the die
DICE = 4

def euler():
    # probability for each tile
    grid = [(1 / GRID_SIZE) for i in range(GRID_SIZE)]
    for n in range(100):
        # copy of the grid, for next iteration
        offgrid = [0 for i in range(GRID_SIZE)]
        # weigh each tile into the new probability
        for i in range(GRID_SIZE):
            weigh(i, offgrid, grid)
        # next grid is the current offgrid
        grid = offgrid
    # sort and reverse the tiles, and put them in a list of 
    # (probability, index) pairs
    sorted_tiles = list(reversed(sorted(zip(grid, range(GRID_SIZE)))))
    # return the 6-digit signature
    signature = ''.join('{:02d}'.format(i) for (prob, i) in sorted_tiles[:3])
    return signature

# weigh the tiles that can be reached from tile i, and add some probabilities
# to reach each target tile in offgrid
def weigh(src, offgrid, grid):
    # for each first dice value
    for d1 in range(1, DICE + 1):
        # for each second dice value
        for d2 in range(1, DICE + 1):
            # destination tile
            dst = (src + d1 + d2) % GRID_SIZE
            # regular tile, weigh it normally
            if dst not in special_cases:
                offgrid[dst] += grid[src] * (1 / DICE / DICE)
            # special tile (CC, CH, G2J), use the information from the hashtable
            else:
                case = special_cases[dst]
                # weigh each new destination tile (that you can "warp" to)
                for warp in case:
                    offgrid[warp] += grid[src] * case[warp] * (1 / DICE / DICE)

# list of special cases that might make the character jump to another tile than
# the one they landed on
special_cases = dict()

# add the Go To Jail tile to the special cases
special_cases[30] = {10: 1}

# list of community chest card tiles (by index)
cc_sources = [2, 17, 33]
# add the community chest tiles to the special cases
for src in cc_sources:
    pairs = {
        src: 14 / 16, # no-teleport
        0: 1 / 16,  # GO
        10: 1 / 16  # JAIL
    }
    special_cases[src] = pairs

# list of chance card tiles (by index)
ch_sources = [7, 22, 36]

# railroad company tiles
railroads = [5, 15, 25, 35]

# utility company tiles
utilities = [12, 28]

# add the chance tiles to the special cases
for src in ch_sources:
    pairs = {
        src: 6 / 16,  # no-teleport
        0: 1 / 16,  # GO
        10: 1 / 16, # JAIL
        11: 1 / 16, # C1
        24: 1 / 16, # E3
        39: 1 / 16, # H2
        5: 1 / 16,  # R1
        ((src - 3) % GRID_SIZE): 1 / 16 # back 3 squares
    }
    # railroad company
    dst = src + 1
    while dst not in railroads:
        dst = (dst + 1) % GRID_SIZE
    if dst in pairs:
        pairs[dst] += 2 / 16
    else:
        pairs[dst] = 2 / 16
    # utility company
    dst = src + 1
    while dst not in utilities:
        dst = (dst + 1) % GRID_SIZE
    pairs[dst] = 1 / 16
    special_cases[src] = pairs
