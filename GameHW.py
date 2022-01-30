import random, os
os.system('cls')



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
        if choice>0 and choice<4:
            check = False
        else:
            print("please enter numbers 1-3")
    except ValueError:
        print("Please try again, only enter 1-3")
        

if choice == 1:
    myNumber= random.randint(1,10)
    level1=10
elif choice == 2:
    myNumber2= random.randint(1,50)
    level2=50
elif choice == 3:
    myNumber3= random.randint(1,100)
    level3=100
print(choice)


myNumber=random.randint(1,10)
GameOn=True
while(GameOn):
    userGuess=int(input("Guess a number from 1-10"+ str(level1)))
    if myNumber == userGuess:
        print("You got it!")
        GameOn=False
    else:
        print("good guess")
print("The number was  "+ str(myNumber))
os.system('cls')
menu()



myNumber2=random.randit(1,50)
GameOn=True
while(GameOn):
    userGuess=int(input("Guess a number from 1-50" + str(50)))
    if myNumber2 == userGuess:
        print("You got it!")
        GameOn=False
    else:
        print("good guess")
print("The number was "+ str(myNumber2))
os.system('cls')
menu()