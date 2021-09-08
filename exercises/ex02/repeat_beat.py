"""Repeating a beat in a loop."""

__author__ = "730383481"


beat = input("What beat do you want to repeat?")
repeat = int(input("How many times do you want to repeat it?"))

if repeat <= 0:
    print("No beat...")

while beat == repeat:
    print(beat)
    repeat = repeat + 1 