import random

roll = random.randint(1, 6)

guess = int(input("Guess the dice roll:\n"))

if roll == guess:
    print(f"Correct! The computer rolled: {roll}")
else:
    print(f"Wrong! The computer rolled: {roll}")