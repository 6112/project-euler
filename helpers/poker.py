class PokerHand:
  """Hand in a game of poker: an ordered list of 5 PokerCard 
    objects."""

  def __init__(self, cards):
    """Main constructor. Takes a list of 5 PokerCard objects."""
    def get_symbol_value(card):
      return card.symbol_value
    self.cards = sorted(cards, key = get_symbol_value)

  def symbol_counts(self):
    """Return a dictionary associating each card symbol to the number of
      occurrences of that card in the hand."""
    dictionary = {}
    for card in self.cards:
      if card.symbol in dictionary:
        dictionary[card.symbol] += 1
      else:
        dictionary[card.symbol] = 1
    return dictionary

  def is_royal_flush(self):
    """Return True iff this is a royal flush (a straight flush with an 
      ace)."""
    if not self.is_flush():
      return False
    return self.is_straight() and self.cards[-1].symbol == 'A'

  def is_straight_flush(self):
    """Returns True iff this is a straight flush (both a straight and a 
      flush)."""
    return self.is_straight() and self.is_flush()

  def is_four_of_a_kind(self):
    """Return True iff this hand has 4 cards with the same symbol."""
    counts = self.symbol_counts()
    return 4 in counts.values()

  def is_full_house(self):
    """Return True iff this hand has both three-of-a-kind and 
      two-of-a-kind."""
    counts = self.symbol_counts()
    return 3 in counts.values() and 2 in counts.values()

  def is_flush(self):
    """Return True iff all cards are of the same suit."""
    for card in self.cards:
      if card.suit != self.cards[0].suit:
        return False
    return True

  def is_straight(self):
    """Return True iff all cards are consecutive."""
    for offset,card in enumerate(self.cards):
      if card.symbol_value != self.cards[0].symbol_value + offset:
        return False
    return True

  def is_three_of_a_kind(self):
    """Return True iff there are exactly 3 occurrences of a card."""
    counts = self.symbol_counts()
    return 3 in counts.values()

  def is_two_pairs(self):
    """Return True iff there are exactly 2 occurrences of two cards."""
    counts = self.symbol_counts()
    pair_count = 0
    for count in counts.values():
      if count == 2:
        pair_count += 1
    return pair_count == 2

  def is_one_pair(self):
    """Return True iff there are exactly 2 occurrences of a card."""
    counts = self.symbol_counts()
    return 2 in counts.values()

class PokerCard:
  """Card from a poker game: has a symbol and a suit, both a
    single character."""

  def __init__(self, symbol, suit):
    """Main constructor."""
    self.symbol = symbol.upper()
    self.suit = suit

  @property
  def symbol_value(self):
    """Wrapper for `value_of_symbol' or the `symbol' field."""
    return value_of_symbol(self.symbol)

def value_of_symbol(symbol): 
  """Return an integer representing the "rank" of a card's symbol.

  For instance, '2' maps to 2, and 'J' maps to 11.

  Consecutive cards have consecutive integers."""
  if symbol in '23456789':
    return int(symbol)
  else:
    return ({
        'T': 10,
        'J': 11,
        'Q': 12,
        'K': 13,
        'A': 14
      })[symbol]

      
def read_poker_line(line_string):
  """Return a PokerHand object corresponding to the line from the file
    `poker.txt'."""
  # list of all the cards
  card_names = line_string.split(" ")
  cards = list(PokerCard(card_name[:-1], card_name[-1:]) \
      for card_name in card_names)
  # lists of hands for the players
  player_1_hand_list = cards[:5]
  player_2_hand_list = cards[5:]
  # hands for the players
  player_1_hand = PokerHand(player_1_hand_list)
  player_2_hand = PokerHand(player_2_hand_list)
  # return a tuple with the hands for the two players
  return (player_1_hand, player_2_hand)

def is_winner_player_1(hand_1, hand_2):
  """Return True iff player 1 (hand_1) wins over player 2 (hand_2).

  hand_1 and hand_2 should be PokerHand objects."""
  hands = (hand_1, hand_2)
  symbol_counts = (hand_1.symbol_counts(), hand_2.symbol_counts())
  # royal flush
  if hand_1.is_royal_flush():
    return True
  if hand_2.is_royal_flush():
    return False
  # straight flush 
  if hand_1.is_straight_flush():
    if not hand_2.is_straight_flush():
      return True
    elif hand_1.cards[-1].symbol_value != hand_2.cards[-1].symbol_value:
      return hand_1.cards[-1].symbol_value > hand_2.cards[-1].symbol_value
  elif hand_2.is_straight_flush():
    return False
  # four-of-a-kind
  if hand_1.is_four_of_a_kind(): 
    if not hand_2.is_four_of_a_kind():
      return True
    elif hand_1.cards[1].symbol_value != hand_2.cards[1].symbol_value:
      return hand_1.cards[1].symbol_value > hand_2.cards[1].symbol_value
  elif hand_2.is_four_of_a_kind():
    return False
  # full house
  if hand_1.is_full_house():
    if not hand_2.is_full_house():
      return True
    else:
      twos = []
      threes = []
      for counts in symbol_counts:
        for symbol,count in counts.items():
          if count == 3:
            threes.append(value_of_symbol(symbol))
          if count == 2:
            twos.append(value_of_symbol(symbol))
      if threes[0] > threes[1]:
        return True
      elif threes[0] < threes[1]:
        return False
      else:
        if twos[0] > twos[1]:
          return True
        elif twos[1] > twos[2]:
          return False
  elif hand_2.is_full_house():
    return False
  # flush
  if hand_1.is_flush():
    if not hand_2.is_flush():
      return True
  elif hand_2.is_flush():
    return False
  # straight
  if hand_1.is_straight():
    if not hand_2.is_straight():
      return True
    elif hand_1.cards[-1].symbol_value != hand_2.cards[-1].symbol_value:
      return hand_1.cards[-1].symbol_value > hand_2.cards[-1].symbol_value
  elif hand_2.is_straight():
    return False
  # three of a kind
  if hand_1.is_three_of_a_kind():
    if not hand_2.is_three_of_a_kind():
      return True
    else:
      threes = []
      for counts in symbol_counts:
        for symbol,count in counts.items():
          if count == 3:
            threes.append(value_of_symbol(symbol))
      if threes[0] > threes[1]:
        return True
      elif threes[0] < threes[1]:
        return False
  elif hand_2.is_three_of_a_kind():
    return False
  # two pairs
  if hand_1.is_two_pairs():
    if not hand_2.is_two_pairs():
      return True
    else:
      twos = [[], []]
      i = 0
      for counts in symbol_counts:
        for symbol,count in counts.items():
          if count == 2:
            twos[i].append(value_of_symbol(symbol))
        i += 1
      twos = [sorted(xs) for xs in twos]
      if twos[0][1] > twos[1][1]:
        return True
      elif twos[0][1] < twos[1][1]:
        return False
      elif twos[0][0] > twos[1][0]:
        return True
      elif twos[0][0] < twos[1][0]:
        return False
  elif hand_2.is_two_pairs():
    return False
  # pair
  if hand_1.is_one_pair():
    if not hand_2.is_one_pair():
      return True
    else:
      twos = []
      for counts in symbol_counts:
        for symbol,count in counts.items():
          if count == 2:
            twos.append(value_of_symbol(symbol))
      if twos[0] > twos[1]:
        return True
      if twos[0] < twos[1]:
        return False
  elif hand_2.is_one_pair():
    return False
  # highest card
  for i in range (-1, -6, -1):
    if hand_1.cards[i].symbol_value > hand_2.cards[i].symbol_value:
      return True
    elif hand_1.cards[i].symbol_value < hand_2.cards[i].symbol_value:
      return False
