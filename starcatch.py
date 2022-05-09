import pygame, os, random, math, datetime
os.system('cls')
pygame.init()

x = 50
y = 400
width = 50
height = 64
xMs=50
yMs=250
wb=30
hb=30
WIDTH= 550
HEIGHT=600
MAIN=True
INST=False
SETT=False
LEV_I=False
LEV_II=False
LEV_III=False
SCORE=False
TITLE_FNT=pygame.font.SysFont('comicsans', 80)
MENU_FNT=pygame.font.SysFont('comicsans', 40)
INST_FNT=pygame.font.SysFont('comicsans', 30)
MenuList=['Instructions','Settings', "Level I","Level II",'Level III','Scoreboard','Exit']
SettingList=['Screen Size',]
check=True
win = pygame.display.set_mode((WIDTH,HEIGHT))
txty=243

squareM=pygame.Rect(xMs,yMs,wb,hb)

#define colors
colors={'white':[255,255,255], 'red':[255,0,0], 'aqua':[102,153, 255],
'orange':[255,85,0],'purple':[48,25,52],'navy':[5,31,64],'pink':[200,3,75]}

#Get colors
background= colors.get('white')
randColor=''
cr_color=colors.get('aqua')
sqM_color=colors.get('pink')
BLACK=(0,0,0)

def TitleMenu(Message):
    text=TITLE_FNT.render(Message, 1, (255,0,0))
    win.fill((255,255,255))
    #get the width  the text 
    #x value = WIDTH/2 - wText/2
    xt=WIDTH/2-text.get_width()/2
    win.blit(text,(xt,50))

def MainMenu(Mlist):
    txty=243
    squareM.y=250
    for i in range(len(Mlist)):
        message=Mlist[i]
        text=INST_FNT.render(message,1,(51,131,51))
        win.blit(text,(90,txty))
        pygame.draw.rect(win,sqM_color, squareM )
        squareM.y +=50
        txty+=50
    pygame.display.update()
    pygame.time.delay(10)



pygame.display.set_caption("StarCatch")

walkRight = [pygame.image.load('images\\TheBasket.png')]
walkLeft = [pygame.image.load('images\\TheBasket.png')]
bg = pygame.image.load('images\\useClouds.jpg')
bg=pygame.transform.scale(bg,(WIDTH,HEIGHT))
char = pygame.image.load('images\\TheBasket.png')

clock = pygame.time.Clock()


vel = 5
isJump = False
jumpCount = 10
left = False
right = False
walkCount = 0

def redrawGameWindow():
    global walkCount
    win.blit(bg, (0,0))
    win.blit(char, (x,y))
    pygame.display.update()


#mainloop
run = True
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
        left = True
        right = False
    if keys[pygame.K_RIGHT] and x < WIDTH - width - vel:
        x += vel
        right = True
        left = False
        print(x)
    else:
        right = False
        left = False
        walkCount = 0
    if x >= WIDTH - width - vel :
        bg = pygame.image.load('images\\background.jpg')
        x=0
    if not(isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
            right = False
            left = False
            walkCount = 0
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10
            
    redrawGameWindow()

pygame.quit()
