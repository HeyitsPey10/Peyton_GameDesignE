
import pygame
pygame.init()

win = pygame.display.set_mode((500,480))

pygame.display.set_caption("falling stars")

walkRight = [pygame.image.load('images\R1.png'), pygame.image.load('images\R2.png'), pygame.image.load('images\R3.png'), pygame.image.load('images\R4.png'), pygame.image.load('images\R5.png'), pygame.image.load('images\R6.png'), pygame.image.load('images\R7.png'), pygame.image.load('images\R8.png'), pygame.image.load('images\R9.png')]
walkLeft = [pygame.image.load('images\L1.png'), pygame.image.load('images\L2.png'), pygame.image.load('images\L3.png'), pygame.image.load('images\L4.png'), pygame.image.load('images\L5.png'), pygame.image.load('images\L6.png'), pygame.image.load('images\L7.png'), pygame.image.load('images\L8.png'), pygame.image.load('images\L9.png')]
bg = pygame.image.load('images\\vaporwave.jpg')
char = pygame.image.load('images\standing.png')