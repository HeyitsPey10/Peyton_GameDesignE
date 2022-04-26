import os, random, time, pygame, math, datetime
os.system('cls')
#initialize pygame
pygame.init()

#create screen
WIDTH= 500
HEIGHT=700
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('level 2')
bg=pygame.image.load('images\\background.jpg')
screen.blit(bg,(0,0))
pygame.display.update()
pygame.time.delay(3000)