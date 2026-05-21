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

random_block = random.choice(blocks)
inputblock = input("input a random block: ")

if random_block == inputblock:
    print("correct!")
else:
    print("wrong... it was" + random_block)
