import random

blocks = [
    "Stone",
    "Dirt",
    "Grass Block",
    "Sand",
    "Oak Log",
    "Cobblestone",
    "Oak Plank",
    "Birch Log",
    "Birch Plank",
    "Diamond Block"
]

inputblock = input("input a random block: ").strip()
if inputblock not in blocks:
    print("That's not a valid block name!")
else:
    if random_block == inputblock:
        print("correct!")
    else:
        print("wrong... it was " + random_block)
