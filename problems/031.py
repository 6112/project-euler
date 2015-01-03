# encoding=utf-8
## SOLVED 2013/12/24
## 73682

# In England the currency is made up of pound, £, and pence, p, and there are
# eight coins in general circulation:

# 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).

# It is possible to make £2 in the following way:

# 1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

# How many different ways can £2 be made using any number of coins?

COINS = [200, 100, 50, 20, 10, 5, 2, 1]

AMOUNT = 200

def euler ():
    return coin_combination_count (AMOUNT, COINS)

def coin_combination_count (amount, coins):
    if amount == 0:
        return 1
    combination_count = 0
    for coin_index, coin in enumerate (coins):
        for coin_count in range (1, amount // coin + 1):
            new_amount = amount - coin_count * coin
            new_coins = coins [coin_index + 1:]
            combination_count += coin_combination_count (new_amount, new_coins)
    return combination_count
