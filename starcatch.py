import pygame
pygame.init()

x = 50
y = 400
width = 50
height = 64
WIDTH= 550
HEIGHT=600
win = pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption("First Game")

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
