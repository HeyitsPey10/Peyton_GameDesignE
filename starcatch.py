import pygame, os, sys, random, math, datetime
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

win = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("StarCatch")
star1=pygame.image.load('catch the fruit\images\star1.png')
star2=pygame.image.load('catch the fruit\images\star2.png')
star3=pygame.image.load('catch the fruit\images\star3.png')
stars=[star1,star2,star3]
bg = pygame.image.load('images\\useClouds.jpg')

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

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
dy=0
def redrawGameWindow():
    global walkCount,dy
    dx=random.randint(0,width)
    
    win.blit(bg, (0,0))
    win.blit(char, (x,y))
    win.blit(star,(34,dy))
    dy +=10
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
