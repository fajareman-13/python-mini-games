#rock paper scissors game
import random 
choices = ["rock" , "paper" , "scissors"]
player = input("choose rock , paper or scissors").lower() # lower function to convert text to lower case
computer = random.choice(choices) # choice from function from random library to choose an item from the list
if player not in choices :
    print("Invalid Choice!")
    exit()
elif player == computer:
    print(f"It's a TIE! Both chose {player}")
elif ( player == "rock" and computer == "scissors") or ( player == "scissors" and computer == "paper") or ( player == "paper" and computer == "rock"):
    print(f"You WIN ! {player} beats {computer}")
else:
    print(f"You LOST ! {computer} beats {player}")
