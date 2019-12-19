import sys, math, pygame, random
from Player import *
from Tilesets import *
from Sounds import *
from Levels import *
from Items import *
from Bosses import *
from SaltSpike import *
from Steak import *

pygame.init()

screenLength = 500
screenWidth = 500
win = pygame.display.set_mode((screenLength, screenWidth))
pygame.display.set_caption("Veggie Girl")



clock = pygame.time.Clock()


def redrawGameWindow():
    win.fill((0, 0, 0))
    veggie.draw(win)
    pygame.display.update()

veggie = Player(self, pos)
run = True
while run:
    clock.tick(27)
    for event in pygame.event.get():
        if event == pygame.QUIT:
            run = False
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                veggie.go("left")
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                veggie.go("right")
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                veggie.go("sleft")
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                veggie.go("sright")
                
    if not(veggie.isJump):
        if keys[pygame.K_SPACE]:
            veggie.isJump = True

            veggie.walkCount = 0
    else:
        if veggie.jumpCount >= -10:
            neg = 1
            if veggie.jumpCount < 0:
                neg = -1
            veggie.y -= (veggie.jumpCount ** 2) * 0.3 * neg
            veggie.jumpCount -= 1
        else:
            veggie.isJump = False
            veggie.jumpCount = 10

    redrawGameWindow()
    

pygame.quit()
