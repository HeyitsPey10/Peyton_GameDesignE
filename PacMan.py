#peytonjacobe
#learning to draw circles, squares, rectangle
#using dictionaries

#circle chases square and tries to eat it. Circle gets bigger when it eats the square

import os, random, time, pygame 

pygame.init()

#declare constants, cariables, lists, dictionaries, any object
#screen size
WIDTH=700
HEIGHT=700
check=True #for the while loop
move=5
#square variables
xs=20
ys=20
wbox=30
hbox=30
#circle radius
rad=15
xc=random.randint(rad, WIDTH-rad)
xc=random.randint(rad, HEIGHT-rad)
#creating the rectangle
square=pygame.Rect(xs,ys,wbox,hbox)

#create screen 
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Circle eats square')

#define colors
colors={'white':[255,255,255], 'red':[255,0,0], 'aqua': [102,153,255], 'purple': [48,25,52], 'pink': [200,3,75], 'magenta': [255,0,255], 'orange': [255,85,0], 'navy': [5,31,64]}

#get colors
background= colors.get('pink')
sq_color=colors.get('navy')
cr_color=colors.get('purple')
while check:
    screen.fill(background)
    for case in pygame.event.get():
        if case.type==pygame.QUIT:
            check=False

    
    keys=pygame.key.get_pressed() #this returns a list
    if keys[pygame.K_a] and square.x >=move:
        square.x -= move
    if keys[pygame.K_d] and square.x <WIDTH-wbox:
        square.x += move 
    if keys[pygame.K_w]:
        square.y -= move
    if keys[pygame.K_s]:
        square.y += move   

    
    pygame.draw.rect(screen, sq_color, square)
    pygame.draw.circle(screen, cr_color, (xc,yc), rad)

    pygame.display.update()
    pygame.time.delay(1000)
