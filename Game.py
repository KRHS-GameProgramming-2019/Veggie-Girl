import pygame, sys, math, random
from Player import *
from Items import *
from Levels import *
from Bosses import *
from SaltSpike import *
from Sounds import *
from Steak import *
from Tilesets import *
pygame.init()



# set these to as follows when ready (1000, 900)
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Veggie Girl")
# set to width being 900 and length being 1000
screenWidth = 500
screenLength = 500
x = 5
y = 435
height = 60
width = 40
vel = 5
isJump = False
jumpCount = 10
left = False
right = False
walkCount = 0
clock = pygame.time.Clock()

def redrawGameWindow():
    global walkCount
    if walkCount  +1 >= 3:
        walkCount = 0
    if left:
        win.blit(walkLeft [walkCount//3], (x,y))
        walkCount += 1
    elif right:
        win.blit(walkRight [walkCount//3], (x, y))
        walkCount += 1
    else:
        win.blit (char, (x, y))
        
    pygame.display.update()
    #to use a picture instead use win.blit (name of image(0, 0))
    win.fill((0, 0, 0))
    pygame.display.update()
    

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
    elif keys[pygame.K_RIGHT] and x < screenLength - width - vel:
        x += vel
        right = True
        left = False
    else:
        right = False
        left = False
        walkCount = 0
        
    if not (isJump):
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
            y -= (jumpCount ** 2) * 0.2 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10
            
    redrawGameWindow()
    drawPlayer()


pygame.quit()
    
    
