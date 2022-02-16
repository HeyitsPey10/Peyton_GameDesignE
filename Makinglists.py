#Peyton Jacobe 2/16/22 

import os, random 
os.system('cls')
fruits=['banana', 'grape', 'strawberry', 'orange', 'apple', 'blackberry', 'papaya', 'watermelon', 'mango', 'durian', 'dragonfruit', 'blueberry', 'tomato', 'lychee', 'cantaloupe', 'honeydew', 'kiwi']
#length of your array 
size=len(fruits)
print(size)
fruits.append('rambutan')
for i in range(size):
    print(fruits[i])
print(fruits[size])
print(fruits[-2])
print(fruits.count('banana'))
list2=[3,6,8,9,10]
fruits.append(list2)
print(fruits)
fruits.insert(2, 'orange')
print(fruits)