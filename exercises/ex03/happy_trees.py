"""Drawing forests in a loop."""

__author__ = "730527166"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'
depth: int = int(input("Depth: "))
i: int = 0
new_tree = TREE
while i < depth: 
    print(TREE)
    TREE = new_tree + TREE
    i = i + 1
