import sys, math, pygame, random
from Player import *
from Tilesets import *
from Levels import *
from Items import *
from Bosses import *
from SaltSpike import *
from Steak import *

#--------------------Setup---------------------
pygame.init()
clock = pygame.time.Clock()
pygame.mixer.init()
songs = ["Sounds/631160_Domyeah---Final-Boss.ogg",
         "Sounds/772055_Aeolia.ogg",
         "Sounds/638233_Boss-Battle.ogg",
         "Sounds/895672_sum--Twilight-Party-House.ogg",
         "Sounds/753446_Creo---Showdown.ogg",
         "Sounds/330448_Waluigi_Loses_It.ogg",
         "Sounds/514911_Final-Boss.ogg",
         "Sounds/71108_newgrounds_bosa_h.ogg",
         "Sounds/894845_Im-Gay-Intro.ogg",
         "Sounds/DeathSound.ogg"
]
songNum = 0
maxSongNum = len(songs)-1
pygame.mixer.music.load(songs[songNum])
pygame.mixer.music.set_volume(0.4)


screenLength = 900
screenWidth = 800
win = pygame.display.set_mode((screenLength, screenWidth))
pygame.display.set_caption("Veggie Girl")

screens = "menu"
#-----------------Game Loop---------------------
while True:
    #--------------------Menu-----------------
    #------------Menu Setup------------
    pygame.mixer.init()
    image = pygame.image.load("Images/Backgrounds/titlescreen.png")
    imgRect = image.get_rect()
    pygame.mixer.music.load("Sounds/894845_Im-Gay-Intro.ogg")
    pygame.mixer.music.play(loops=-1, start=0.0)


    #------------Menu Loop-----------
    while screens == "menu":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit();
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    screens = "game"
                elif event.key == pygame.K_w:
                    screens = "secret"


                elif event.key == pygame.K_ESCAPE:
                    sys.exit();
        win.blit(image, imgRect)
        pygame.display.flip()

    image = pygame.image.load("Images/Backgrounds/walScreen.png")
    imgRect = image.get_rect()
    pygame.mixer.music.stop()
    pygame.mixer.music.load("Sounds/330448_Waluigi_Loses_It.ogg")
    pygame.mixer.music.play(loops=-1, start=0.0)
    while screens == "secret":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit();
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    screens = "menu"






                elif event.key == pygame.K_ESCAPE:
                    sys.exit();
        win.blit(image, imgRect)
        pygame.display.flip()


    #--------------------Game-----------------
    #--------------Game Setup-------------
    veggie = Player([5, 785])

    pygame.mixer.music.play(loops=-1, start=0.0)
    isPlaying = True

    image = pygame.image.load("Images/Backgrounds/randombg.png")
    imgRect = image.get_rect()
    pygame.mixer.init()
    pygame.mixer.music.load("Sounds/631160_Domyeah---Final-Boss.ogg")

    pygame.mixer.music.play(loops=-1, start=0.0)
    #--------------Game Loop-------------
    while screens == "game":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    veggie.go("left")
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    veggie.go("right")
                elif event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                    veggie.jump()
                elif event.key == pygame.K_ESCAPE:
                    sys.exit();
                            
                            
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
        veggie.wallCollide()

        win.blit(image, imgRect)
        win.blit(veggie.image, veggie.rect)
        pygame.display.flip()
        clock.tick(60)
