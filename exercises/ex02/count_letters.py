"""Counting letters in a string."""

__author__ = "730383481"

letter: str = input("what letter do you want to search for?: ")
user_string: str = input("Enter a word: ")

 
count: int = 0 
i: int = 0 
while i < len(user_string):
    if user_string[i] == letter:
        count = count + 1 
    i = i + 1 
print("Count:", count)