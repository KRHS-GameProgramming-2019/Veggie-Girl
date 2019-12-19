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

screenLength = 1000
screenWidth = 900
win = pygame.display.set_mode((screenLength, screenWidth))
pygame.display.set_caption("Veggie Girl")

clock = pygame.time.Clock()

veggie = Player([5, 425])
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
                
    win.fill((0, 0, 0))
    win.blit(veggie.image, veggie.rect)
    pygame.display.flip()
    
    


    

pygame.quit()
