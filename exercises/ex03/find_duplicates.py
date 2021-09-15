"""Finding duplicate letters in a word."""

__author__ = "730383481"

word: str = input("Enter a word: ")
duplicate: bool = False 
i: int = 0 
j: int = 1
while i < len(word):
    while j < len(word):
        if word[i] == word[j]: 
            duplicate = True
            j = len(word)
            i = len(word)
        j += 1
    i += 1
    j = i + 1
print(duplicate)


        