"""Drawing forests in a loop."""

__author__ = "730383481"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'
depth: int = int(input("Depth: "))
i = 0
row: int = 1 
while (i < depth):
    j: int = 0
    trees: str = TREE
    while(j < i):
        trees = trees + TREE
        j += 1
    i += 1
    print(trees)
