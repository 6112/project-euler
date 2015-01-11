#encoding=utf-8
## SOLVED 2014/05/07
## 376

# [...]

# The file, poker.txt, contains one-thousand random hands dealt to two players.
# Each line of the file contains ten cards (separated by a single space): the
# first five are Player 1's cards and the last five are Player 2's cards. You
# can assume that all hands are valid (no invalid characters or repeated
# cards), each player's hand is in no specific order, and in each hand there is
# a clear winner.

# How many hands does Player 1 win?

import helpers.poker as poker

def euler():
  # number of games player 1 wins
  win_count = 0
  # for each line in the file
  with open('data/054.txt') as data_file:
    for line_string in data_file:
      # remove whitespace at the end
      line_string = line_string.rstrip()
      # make two PokerHand objects (wrappers for lists of PokerCard objects)
      hand1, hand2 = poker.read_poker_line(line_string)
      # if player 1 wins this game
      if poker.is_winner_player_1(hand1, hand2):
        win_count += 1
  # return the number of games won by player 1
  return win_count
