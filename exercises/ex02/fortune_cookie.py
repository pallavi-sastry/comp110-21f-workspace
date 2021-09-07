"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730527166"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...
print("Your fortune cookie says... ")

random: int = randint(1, 4)

if random == 1: 
    print("You will find true happiness within yourself!")
else:
    if random == 2: 
        print("Tomorrow you will meet the love of your life!")
    else:
        if random == 3: 
            print("This year you will earn a lot of money!!")
        else: 
            print("There is prosperity in your future!")

print("Now, go spread positive vibes!")