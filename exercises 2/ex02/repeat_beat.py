"""Repeating a beat in a loop."""

__author__ = "730383481"


beat = input("What beat do you want to repeat? ")
repeat = int(input("How many times do you want to repeat it? "))
counter: int = 0
if repeat <= 0:
    print("No beat...")

output = ""
while(counter < repeat):
    counter = counter + 1
    output = output + beat 
print((" " + beat) * int(repeat))