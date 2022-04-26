#Peyton Jacobe 
#a) open/create a file
#b) write w
#c) append a 
#d)read r
#e) close

import pygame, os, datetime 
os.system('cls')
date=datetime.datetime.now()
score=123
name='peyton'
print(date.strftime('%Y,%m,%d'))
#print(blahblah('%d/%m/%y'))
scoreLine=str(score)+" "+name+" "+date.strftime("%m/%d/%y")
print(scoreLine)
#writing erases everything in the file
myFile=open('file.txt','w')
myFile.write(scoreLine)

myFile.close()
score=345
name='jay'
print(date.strftime('%m/%d/%y'))
scoreLine=str(score)+'\t'+name+'\t'+date.strftime('%m/%d/%y')
myFile=open('file.txt','a')
myFile.write(scoreLine)
myFile.close()
myFile=open('file.txt','r')
lines=myFile.readline()
print(lines)
lines=myFile.readline()
print(lines)
myFile.close()
