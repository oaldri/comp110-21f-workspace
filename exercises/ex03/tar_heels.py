"""An exercise in remainders and boolean logic."""

__author__ = "730383481"


choice: int = int(input("Choose a number: "))

if (choice % 2 == 0 and choice % 7 == 0):
    print("TAR HEELS")
else:
    if choice % 2 == 0:
        print("TAR")
    else:
        if choice % 7 == 0:
            print("HEELS")
        else:
            if choice % 2 != 0 or choice % 7 != 0: 
                print("CAROLINA")