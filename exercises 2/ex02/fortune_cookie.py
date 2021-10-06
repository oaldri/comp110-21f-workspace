"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730383481"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


print("Your fortune cookie says...")
number = randint(1, 4)
if number == 1:
    print("You will have a great day tomorrow!!")
else: 
    if number == 2:
        print("You will win the lottery!!")
    else:
        if number == 3: 
            print("You will win a car!")
        else:
            if number == 4:
                print("You will recieve an unexpected gift!")
print("Now, go spread positive vibes!")
