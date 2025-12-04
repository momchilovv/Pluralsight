import random

computer_choice = random.choice(["rock", "paper", "scissors"])

player_choice = input("Choose rock, paper or scissors:\n")

if computer_choice == player_choice:
    print("Draw")
elif player_choice == "rock" and computer_choice == "scissors":
    print("Win")
elif player_choice == "paper" and computer_choice == "rock":
    print("Win")
elif player_choice == "scissors" and computer_choice == "paper":
    print("Win")
else:
    print("Lost")

print(f"You picked {player_choice} and the computer picked {computer_choice}.")