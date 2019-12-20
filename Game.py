import sys, math, pygame, random
from Player import *
from Tilesets import *
#from Sounds import * # Needs files...also this actually runs a game not just holds a class so you might not need it -Spooner
from Levels import *
from Items import *
from Bosses import *
from SaltSpike import *
from Steak import *

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("Sounds/631160_Domyeah---Final-Boss.ogg")

screenLength = 1000
screenWidth = 900
win = pygame.display.set_mode((screenLength, screenWidth))
pygame.display.set_caption("Veggie Girl")

clock = pygame.time.Clock()

veggie = Player([5, 845])
run = True
pygame.mixer.music.play(loops=-1, start=0.0)

while run:
   
    clock.tick(27)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #added '.type. to the event check so it actually quits -CS
            run = False
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                veggie.go("left")
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                veggie.go("right")
                
            if event.key == pygame.K_SPACE: #just picking sonething, feel free to change -CS
                veggie.jump() # I wrote a special funtion for this, but there is no reason it couldn't be handled by the veggie.go() function.
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                veggie.go("sleft")
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                veggie.go("sright")
                
    veggie.update() # do all the stuff the veggie needs to do on a turn -CS
    
    win.fill((0, 0, 0))
    win.blit(veggie.image, veggie.rect)
    pygame.display.flip()
    
    
sys.exit()
pygame.quit()
