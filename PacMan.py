#peytonjacobe
#learning to draw circles, squares, rectangle
#using dictionaries

#circle chases square and tries to eat it. Circle gets bigger when it eats the square

#learning how to draw circles and rectangles

#use keys to move objects

#Using Dictionaries

 

#Objective of the game is for the rect to run away fom the circle, if they collide the circle etas the square,

#circle will  get larger, and a new rect should appear somewhere on the screen

# K_UP                  up circle
# K_DOWN                down circle
# K_RIGHT               right circle
# K_LEFT                left circle
# K_a                   left square
# K_d                   right square
# K_w                   up square
# K_s                   down square
# K_SPACE               jump


import os, random, time, pygame, math

#initialize pygame
pygame.init()

 
#Declare constants, variables, list, dictionaries, any object
#scree size
WIDTH=700
HEIGHT=700

MenuList=['Instructions', 'Settings', 'Level 1', 'Level 2', 'Level 2', 'Level 3', 'Score Board', 'Exit']
SettingList=['Screen Size', 'Font size', 'circle color']
check=True #for the while loop
move=5 #pixels

#square variables
xs=20
ys=20
wbox=30
hbox=30

#circle variables
rad=15
xc=random.randint(rad, WIDTH-rad)
yc=random.randint(rad, HEIGHT-rad)

#main menu variables
wb=30
hb=30
xMs=50
yMs=250

#create screen
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Circle eats Square')

TITLE_FNT=pygame.font.SysFont('Verdana', 70)
MENU_FNT=pygame.font.SysFont('Verdana', 40)
INST_FNT=pygame.font.SysFont('Verdana', 25)

#TITLE
def TitleMenu(Message):
    text=TITLE_FNT.render(Message, 1, (5,31,64))
    screen.fill((255,255,255))
    xt=WIDTH/2-text.get_width()/2
    screen.blit(text,(xt,50))

#Create menu square
squareM=pygame.Rect(xMs,yMs,wb,hb)
def MainMenu(Mlist):
    txty=243
    squareM.y=250
    for i in range(len(Mlist)):
        message=Mlist[i]
        text=INST_FNT.render(message,1,(48,25,52))
        screen.blit(text,(90,txty))
        pygame.draw.rect(screen,sqM_color,squareM)
        squareM.y +=50
        txty+=50
    pygame.display.update()
    pygame.time.delay(10000)


 
#inscribed Square:
ibox=int(rad*math.sqrt(2))
startpoint = (int(xc-ibox/2),int(yc-ibox/2))
print(startpoint[0]-ibox,startpoint[1])
insSquare=pygame.Rect(startpoint[0],startpoint[1],ibox,ibox)

#creating the rect object
square=pygame.Rect(xs,ys,wbox,hbox)


#define colors
colors={'white':[255,255,255], 'red':[255,0,0], 'aqua':[102,153, 255],
'orange':[255,85,0],'purple':[48,25,52],'navy':[5,31,64],'pink':[200,3,75]}

#Get colors
background= colors.get('white')
randColor=''
cr_color=colors.get('white')
sqM_color=colors.get('navy')

def changeColor():
    global randColor
    colorCheck=True
    while colorCheck:
        randColor=random.choice(list(colors))
        if randColor==background:
            print(randColor)
            print(background)
            randColor=random.choice(list(colors))
        else:
            colorCheck=False

 

#Making a rand c f the square

changeColor()
sq_color=colors.get(randColor)


MAX=10
jumpCount=MAX
JUMP=False
while check:
    screen.fill(background)
    TitleMenu('MENU')
    MainMenu(MenuList)
    for case in pygame.event.get():
        if case.type==pygame.QUIT:
            check=False

   


    keys=pygame.key.get_pressed() #this returns a list
    if case.type ==pygame.MOUSEBUTTONDOWN:
        mouse_pos=pygame.mouse.get_pos()
        print(mouse_pos)
        if ((mouse_pos[0] >20 and mouse_pos[0] <60) and (mouse_pos[1] >250 and mouse_pos[1] <290)):
            screen.fill(background)
        TitleMenu('INSTRUCTIONS')

    if keys[pygame.K_a] and square.x >=move:
        square.x -= move #subtract 5 from the x value
    if keys[pygame.K_d] and square.x <WIDTH-wbox:
        square.x += move  
    #Jumping part
    if not JUMP:
        if keys[pygame.K_w]:
            square.y -= move
        if keys[pygame.K_s]:
            square.y += move  
        if keys[pygame.K_SPACE]:
            JUMP=True

    else:
        if jumpCount >=-MAX:
            square.y -= jumpCount*abs(jumpCount)/2
            jumpCount-=1
        else:
            jumpCount=MAX
            JUMP=False

 

#Finish circle
    if keys[pygame.K_LEFT] and xc >=rad+move:
        xc -= move #substract 5 from the x value
        insSquare.x -= move
    if keys[pygame.K_RIGHT] and xc <=WIDTH -(rad+move):
        xc += move #substract 5 from the x value  
        insSquare.x += move
    if keys[pygame.K_DOWN] and yc <=HEIGHT-(rad+move):
        yc += move #substract 5 from the x value
        insSquare.y += move
    if keys[pygame.K_UP] and yc >=rad+move:
        yc -= move #substract 5 from the x value  
        insSquare.y -= move

       

    checkCollide = square.colliderect(insSquare)

    if checkCollide:
        square.x=random.randint(wbox, WIDTH-wbox)
        square.y=random.randint(hbox, HEIGHT-hbox)  
        changeColor()
        sq_color=colors.get(randColor)
        rad +=move
        ibox=int(rad*math.sqrt(2))
        startpoint = (int(xc-ibox/2),int(yc-ibox/2))
        insSquare=pygame.Rect(startpoint[0],startpoint[1],ibox,ibox)

       

    pygame.draw.rect(screen, sq_color, square)
    pygame.draw.rect(screen,cr_color, insSquare )
    pygame.draw.circle(screen, cr_color, (xc,yc), rad)

 

    pygame.display.update()
    pygame.time.delay(10)



