import sys, math, pygame, random
from Player import *
from Tilesets import *
from Levels import *
from Items import *
from Bosses import *
from SaltSpike import *
from Steak import *

pygame.init()
pygame.mixer.init()
songs = ["Sounds/631160_Domyeah---Final-Boss.ogg",
         "Sounds/772055_Aeolia.ogg",
         "Sounds/638233_Boss-Battle.ogg",
         "Sounds/895672_sum--Twilight-Party-House.ogg",
         "Sounds/753446_Creo---Showdown.ogg",
         "Sounds/514911_Final-Boss.ogg",
         "Sounds/71108_newgrounds_bosa_h.ogg",
         "Sounds/894845_Im-Gay-Intro.ogg",
]
songNum = 0
maxSongNum = len(songs)-1
pygame.mixer.music.load(songs[songNum])

screenLength = 900
screenWidth = 800
win = pygame.display.set_mode((screenLength, screenWidth))
pygame.display.set_caption("Veggie Girl")


		
		
clock = pygame.time.Clock()

veggie = Player([5, 785])
run = True
pygame.mixer.music.play(loops=-1, start=0.0)
isPlaying = True

while run:
   
    clock.tick(27)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            run = False
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                veggie.go("left")
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                veggie.go("right")
                
            if event.key == pygame.K_SPACE: 
                veggie.jump() 
                
            if event.key == pygame.K_m:
                if isPlaying:
                    isPlaying = False
                    pygame.mixer.music.pause()
                else:
                    isPlaying = True
                    pygame.mixer.music.unpause()
                    
            if event.key == pygame.K_1:
                if isPlaying:
                    if songNum >= maxSongNum:
                        songNum = 0
                    else:
                        songNum += 1
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load(songs[songNum])
                    pygame.mixer.music.play(loops=-1, start=0.0)
                    isPlaying = True
                
                
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                veggie.go("sleft")
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                veggie.go("sright")
                
    veggie.update() 

    win.fill((0, 0, 0))
    win.blit(veggie.image, veggie.rect)
    pygame.display.flip()
    
    
sys.exit()
pygame.quit()
