import pygame, os, time
pygame.init()
wind=pygame.display.set_mode((700,700))
pygame.display.set_caption("testing")

#create diff types of fonts

TITLE_FNT=pygame.font.SysFont('comicsans', 80)
MENU_FNT=pygame.font.SysFont('comicsans', 40)
INST_FNT=pygame.font.SysFont('comicsans', 25)
text=TITLE_FNT.render('oops', 1, (255,0,0))
wind.fill((255,255,255))
wind.blit(text,(50,50))
text=INST_FNT.render("write your instructions",1,(0,255,0))
wind.blit(text,(220,220))
pygame.display.update()

pygame.time.delay(10000)