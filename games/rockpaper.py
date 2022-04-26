#make the menu

#use randint() for the computer's choice

#user choice 1,3- picks rock paper or scissors
#if the user gives rock, convert it to 1
#if the user gives paper, convert it to 2
#if the user gives scissors, convert it to 3


 # if computer=2 and userguess=3
#user wins


#Source: https://realpython.com/python-rock-paper-scissors/

import random, os
os.system('cls')

print("*************************************")
print("|                                   |")
print("|             Welcome to            |")
print("|        Rock Paper Scissors!       |")
print("|                                   |")
print("*************************************")

while True:
    user_action = input("Enter a choice (rock, paper, scissors): ")
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock beats scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cut paper! You lose.")
    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors cut paper! You win!")
        else:
            print("Rock beats scissors! You lose.")
    
    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        print("Goodbye!")
        break

       