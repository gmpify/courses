"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""


# Score categories.
# Change the values as you see fit.
YACHT = 'yatch'
ONES = 'ones'
TWOS = 'twos'
THREES = 'threes'
FOURS = 'fours'
FIVES = 'fives'
SIXES = 'sixes'
FULL_HOUSE = 'full_house'
FOUR_OF_A_KIND = 'four_of_a_kind'
LITTLE_STRAIGHT = 'little_straight'
BIG_STRAIGHT = 'big_straight'
CHOICE = 'choice'


def score(dice, category):
    score = 0
    if category == YACHT:
        if len(set(dice)) == 1:
            score += 50

    elif category == ONES:
        score += dice.count(1) * 1

    elif category == TWOS:
        score += dice.count(2) * 2

    elif category == THREES:
        score += dice.count(3) * 3

    elif category == FOURS:
        score += dice.count(4) * 4

    elif category == FIVES:
        score += dice.count(5) * 5

    elif category == SIXES:
        score += dice.count(6) * 6

    elif category == FULL_HOUSE:
        if len(set(dice)) == 2 and (dice.count(dice[0]) == 2 or dice.count(dice[0]) == 3):
            score = sum(dice)

    elif category == FOUR_OF_A_KIND:
        if (len(set(dice)) == 2 and (dice.count(dice[0]) == 1 or dice.count(dice[0]) == 4)) or len(set(dice)) == 1:
            score += 4 * (dice[0] if (dice.count(dice[0]) == 4 or dice.count(dice[0]) == 5) else dice[1])

    elif category == LITTLE_STRAIGHT:
        if len(set(dice)) == 5 and dice.count(1) == 1 and dice.count(6) == 0:
            score = 30

    elif category == BIG_STRAIGHT:
        if len(set(dice)) == 5 and dice.count(6) == 1 and dice.count(1) == 0:
            score = 30

    elif category == CHOICE:
        score += sum(dice)

    return score
