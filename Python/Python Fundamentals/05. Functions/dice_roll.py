import random

def roll_dice():
    return random.randint(1, 6) + random.randint(1, 6)

def main():
    first_player = input("Enter first player's name: ")
    second_player = input("Enter second player's name: ")

    print(f"{first_player} rolled {roll_dice()}")
    print(f"{second_player} rolled {roll_dice()}")

main()