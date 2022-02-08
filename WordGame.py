#Peyton Jacobe, 2/8
#record game with 3 levels


import os, random
os.system('cls')

word=""
guess=""
def selectWord():
    global word
    fruits=['banana', 'grape', 'strawberry', 'orange', 'apple', 'blackberry', 'papaya', 'watermelon', 'mango', 'durian', 'dragonfruit', 'blueberry', 'tomato', 'lychee', 'cantaloupe', 'honeydew', 'kiwi']


    word=random.choice(fruits)

def guessFunction():
    global guess
    check=True
    while check:
        try:
            guess=input('\nenter a letter to guess the word:')
            if guess.isalpha() and len(guess)==1:
                check=False
            else:
                print('only one letter please')
        except ValueError:
            print('only one letter please')

gameOn=True
tries=0
letterGuessed=""
selectWord()
while gameOn:
    guessFunction()
    letterGuessed += guess #letterGuessed=letterGuessed + guess
    if guess not in word:
        tries +=1
        print(tries) #delete when game is done
    countLetter=0
    for letter in word:
        if letter in letterGuessed:
            print(letter, end=" ")
            countLetter +=1
        else:
            print('_', end=' ')
    if tries >6:
        print("\n Sorry, you ran out of tries")
        #playGame() ask if they want to play again 
    if countLetter == len(word):
        print('\nyou got it!')
        
    

