import random

# spin the reels (the actualy little spinny disk thingies on a slot machine) and return a list of symbols
# (the little funny pictures that you try to match while falling down an infinite loop of money loss)


def spin_reels():
    symbols = ['cherry', 'lemon', 'bell', 'bar', 'seven']
    return [random.choice(symbols) for _ in range(3)]

# calculate the win amount, given a list of symbols


def get_win_amount(reels):
    if reels[0] == reels[1] == reels[2]:
        return 100
    elif reels[0] == reels[1] or reels[1] == reels[2]:
        return 50
    else:
        return 0

# play a single game of the slot machine


def play():
    # spin the reels
    reels = spin_reels()
    # calculates the win amount
    win_amount = get_win_amount(reels)
    # prints out the results
    print(f'The reels are {reels}. You won {win_amount} credits!')


# runs the slot machine
play()

# use "python filename.py" to run
# i would copyright this but its so unimaginably basic that if anyone steals it id be astounded.
# this def could be simplified and made smoother but who cares
