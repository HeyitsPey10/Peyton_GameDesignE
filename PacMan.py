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

MAX=10
jumpCount=MAX
JUMP=False
while check:
    screen.fill(background)
    for case in pygame.event.get():
        if case.type==pygame.QUIT:
            check=False

    
    keys=pygame.key.get_pressed() #this returns a list
    if keys[pygame.K_a] and square.x >=move:
        square.x -= move
    if keys[pygame.K_d] and square.x <WIDTH- (wbox + move):
        square.x += move 
    #jumping part
        if not JUMP: 
        if keys[pygame.K_w] and square.y >= move:
            square.y -= move
        if keys[pygame.K_s] and square.y < HEIGHT - (hbox + move):
            square.y += move
        if keys[pygame.K_SPACE]:
            JUMP=True

    else:
        if jumpCount >=-MAX:
            square.y -= jumpCount*abs(jumpCount)/2 
            jumpCount -=1
        else:
            jumpCount=MAX
            JUMP=False


#finished circle
    if keys[pygame.K_LEFT] and xc >= radius+ move:
        xc -= move
    if keys[pygame.K_RIGHT] and xc < WIDTH - (radius+move):
        xc += move 
    if keys[pygame.K_UP] and yc >=radius+move:
        yc -= move
    if keys[pygame.K_DOWN] and yc < HEIGHT - (radius+move):
        yc += move
     
    checkCollide = square.collidepoint((xc,yc))
    if checkCollide:
        square.x=random.randint(wbox, WIDTH-wbox)
        square.y=random.randint(hbox, HEIGHT-hbox)
        rad +=move


    pygame.draw.rect(screen, sq_color, square)
    pygame.draw.circle(screen, cr_color, (xc,yc), rad)
    pygame.display.update()
    pygame.time.delay(1000)
