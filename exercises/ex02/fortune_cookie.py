"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730322189"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint

print("Your fortune cookie says...")

fortune = randint(1, 4)

if fortune == 1:
    print("You will find yourself in a predicament soon.")
else:
    if fortune == 2:
        print("Your love life is about to be shaken up.")
    else:
        if fortune == 3:
            print("You will be happy and successful!")
        else:
            if fortune == 4:
                print("You're going to have an amazing day!")

print("Now, go spread positive vibes!")