import random, os
os.system('cls')
tries=0 

#Today we're learning try and except, functions, elif
#Let's make the menu a function (key word def)
def menu():
    print("####################################")
    print("##    Guess a Number Game Menu    ##")
    print("##                                ##")
    print("##       1. Level 1-10            ##")
    print("##       2. Level 1-50            ##")
    print("##       3. Level 1-100           ##")
    print("##      Select your level         ##")
    print("####################################")

#checking for correct user input 
menu() #calling the function by name
check=True
while check:
    try:
        choice=int(input("Level:  "))
        check = False
    except ValueError:
        print("Please try again, only enter 1-3")
        

if choice == 1:
    myNumber= random.randint(1,10)
elif choice == 2:
    myNumber= random.randint(1,50)
elif choice == 3:
    myNumber= random.randint(1,100)
print(choice)


myNumber=random.randint(1,10)
GameOn=True
while(GameOn):
    userGuess=int(input("Guess a number from 1-10 "))
    if myNumber == userGuess:
        print("You got it!")
        GameOn=False
    else:
        print("good guess")
        tries+1
print("The number was  "+ str(myNumber))
os.system('cls')
menu()