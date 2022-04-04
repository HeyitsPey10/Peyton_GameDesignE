#Peyton Jacobe, 3/23/22
#Main menu for the game 
#C:\Users\russe\OneDrive\Desktop\Game Design\Peyton_GameDesignE\Cardgame.py
import pygame, os, time

#Variables
WIDTH=700
HEIGHT=700
wb=30
hb=30
xMs=50
yMs=250

#list messages
MenuList=['Instructions', 'Settings', 'Level 1', 'Level 2', 'Level 2', 'Level 3', 'Score Board', 'Exit']
SettingList=['Screen Size', 'Font size', 'circle color']
#GET COLORS
colors={'white':[255,255,255], 'red':[255,0,0], 'aqua':[102,153, 255],
'orange':[255,85,0],'purple':[48,25,52],'navy':[5,31,64],'pink':[200,3,75]}
background= colors.get('white')
randColor=''
sqM_color=colors.get('navy')

#SCREEN
wind=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Circle Eats Square")

#FONTS
TITLE_FNT=pygame.font.SysFont('Verdana', 70)
MENU_FNT=pygame.font.SysFont('Verdana', 40)
INST_FNT=pygame.font.SysFont('Verdana', 25)

#TITLE
text=TITLE_FNT.render('MENU', 1, (5,31,64))
wind.fill((255,255,255))
#Get the width of the text
#x value = width/2 - width of text/2
xt=WIDTH/2-text.get_width()/2
wind.blit(text,(xt,50))

#Create First button


#Create menu square
squareM=pygame.Rect(xMs,yMs,wb,hb)
txty=243
for i in range(7):
    message=MenuList[i]
    text=INST_FNT.render(message,1,(48,25,52))
    wind.blit(text,(90,txty))
    pygame.draw.rect(wind,sqM_color,squareM)
    squareM.y +=50
    txty+=50
pygame.display.update()
pygame.time.delay(10000)