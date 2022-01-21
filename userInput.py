#Peyton Jacobe, 1/21/22

#learning the input() function 
#type casting, branching, looping 

import os, random 
os.system('cls')

#declare variable for user input 


#guess a number
# myNumber = 9 
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
