"""Exercise 3 part 1."""

__author__ = "730383481"


choice: int = int(input("Choose a number: "))

if (choice % 2 == 0 and choice % 7 == 0):
    print("TAR HEELS")
else:
    if choice % 2 == 0:
        print("TAR")
    if choice % 7 == 0:
        print("Heels")
    else:
        print("CAROLINA")