#Peyton Jacobe, 1/21/22

#learning the input() function 
#type casting, branching, looping 

import os, random
from tkinter import Menu 
os.system('cls')

#declare variable for user input 


#guess a number
# myNumber = 9 
print("##################################")
print("#                                #")
print("#    Guess a Number Game Menu    #")
print("#                                #")
print("##################################")
print()
choice = input("""
Select level A, B, or C
A: 1-10
B: 1-50
C: 1-100
Please enter your choice:   """)
myNumber=random.randint(1,10)
GameOn=True
while(GameOn):
    userGuess=int(input("Guess a number from 1-10 "))
    if myNumber == userGuess:
        print("You got it!")
        GameOn=False
    else:
        print("good guess")
print("The number was  "+ str(myNumber))
