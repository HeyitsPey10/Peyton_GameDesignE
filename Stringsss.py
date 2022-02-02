#Peyton Jacobe 1/31/22

#Strings are an array of characters. They have many functions

import random, os
os.system('cls')
myName= "Peyton Jacobe"
myStatement=""" If you use this formatting, it will print
it exactly
how you 
type it, spacing and all"""

for elem in myStatement:
    print(elem, end=" ")
guess=random.choice(myName)
print(guess)
words=["Radio", "Clues", "There", "Robot", "Moist"]
word=random.choice(words)
print(word)
check=True
while check:
    letter=input("please give a letter!")
    if len(letter)>1 or not letter.isalpha():
        print("a letter please")
    else:
        check=False
print("ready to play!")
for i in range(len(word)):
    if letter == word[i]:
        print(letter, end= " ")
    else:
        print("_", end=" ")



print ("My last name starts with " +myName[7])
if 'blah' in myStatement:
    print('true')
print('expert' not in myStatement)
# find() will return the index of the character you are looking for (first instance)
INDEX= myName.find(" ")
print(INDEX)
#finding the length of your word
wordLen=len(myName)
print(wordLen) #your last index is length minus 1
#for loop in range 0 to limit 
for i in range(wordLen-1):
    if "a" in myName[i]:
        print(i, end=", ")
print("")
print("done")
# converting everything to lowercase 
myStatement=myStatement.lower()
print(myStatement)



