import sys, math, pygame, random
from Player import *
from EndBlock import *
from Bosses import *
from SaltSpike import *
from SideSpikeL import *
from SideSpikeR import *
from Steak import *
from CobbleWall import *
from LevelLoader import *
from Wall import *
from FallBlock import *
from Steak import *
from Button import *

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
         "Sounds/DeathSound.ogg",
         "Sounds/920514_Anything-is-Possible.ogg",
]
songNum = 0
maxSongNum = len(songs)-1
pygame.mixer.music.load(songs[songNum])
pygame.mixer.music.set_volume(0.4)


lev = 1
world = 1

enemyKinds = ["saltspike",
              "sidespikel",
              "sidespiker",
              "steak",
             ]
platformKinds = ["dirt", 
                "walls",
                "floor",
                "ground", 
                "fallblock", 
                "cobble", 
                ]
endKind = ["end",
            
          ]

screenLength = 900
screenWidth = 800
screenSize = [screenLength, screenWidth]
win = pygame.display.set_mode(screenSize)
pygame.display.set_caption("Veggie Girl")

screens = "menu"
#--------------------Game Loop--------------------#
while True:
    #--------------------Menu-----------------
    #------------Menu Setup------------
    pygame.mixer.init()
    image = pygame.image.load("Images/Backgrounds/titlescreen.png")
    imgRect = image.get_rect()
    pygame.mixer.music.load("Sounds/894845_Im-Gay-Intro.ogg")
    pygame.mixer.music.play(loops=-1, start=0.0)
    startButton=Button("StartButton", [400,255])

    #------------Menu Loop-----------
    while screens == "menu":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit();
            elif event.type == pygame.MOUSEMOTION:
                startButton.update(event.pos, event.buttons)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                startButton.click(event.pos)
            elif event.type == pygame.MOUSEBUTTONUP:
                if startButton.click(event.pos):
                    screens = "game"
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    screens = "game"
                elif event.key == pygame.K_p:
                    screens = "secret"


                elif event.key == pygame.K_ESCAPE:
                    sys.exit();
        win.blit(image, imgRect)
        win.blit(startButton.image, startButton.rect)
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

    #--------------------End Loop--------------------#
    while screens == "end":
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit();
                    
                    #Quit button code please
                    
        win.blit(image, imgRect)
        win.blit(startButton.image, startButton.rect)
        pygame.display.flip()

        image = pygame.image.load("Images/Backgrounds/end2.png")
        imgRect = image.get_rect()
        pygame.mixer.music.stop()






        if event.key == pygame.K_ESCAPE:
            sys.exit();
        win.blit(image, imgRect)
        pygame.display.flip()
    #--------------------  Game  --------------------#
    #-------------------Game Setup-------------------#
    tiles, pos = loadLevel("Levels/W" + str(world) + "L" + str(lev) + ".lvl")
    veggie = Player(pos)

    pygame.mixer.music.play(loops=-1, start=0.0)
    isPlaying = True

    image = pygame.image.load("Images/Backgrounds/GrassLVL.png")
    imgRect = image.get_rect()
    pygame.mixer.init()
    pygame.mixer.music.load("Sounds/920514_Anything-is-Possible.ogg")

    pygame.mixer.music.play(loops=-1, start=0.0)
    
    prevlev = lev
    #--------------Game Loop-------------
    while screens == "game":
        if prevlev != lev:
            tiles, pos = loadLevel("Levels/W" + str(world) + "L" + str(lev) + ".lvl")
            try:        #Try to load background; but don't crash if you don't find it
                image = pygame.image.load("Images/Backgrounds/" + str(world) + "LVL" + str(lev) + ".png")
            except:     #Load default and complain in console if the file wasn't found or able to be loaded
                print("********NO BACKBROUND FOUND************")
                image = pygame.image.load("Images/Backgrounds/GrassLVL.png")
            prevlev = lev
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

        veggie.update(screenSize)
        for tile in tiles:
            if tile.kind in ["floor", "ground", "cobble"]:
                if veggie.platformCollide(tile):
                    print (">>>>>>>>>>>>Hit Floor")
            if tile.kind == "wall":
                if veggie.vineCollide(tile):
                    print (">>>>>>>>>>>>Hit Wall")
            if tile.kind == "fallblock":
                if veggie.fallCollide(tile):
                    print (">>>>>>>>>>>>Hit Fall")
            if tile.kind == "end":
                if veggie.endCollide(tile):
                    print (">>>>>>>>>>>>Hit End")
                    screens = "end"
            elif tile.kind in enemyKinds:
                if veggie.enemyCollide(tile):
                    print("------------------------", pos)
                    veggie = Player(pos)
                    
        if veggie.screenCollide(screenSize) == "Right":
            lev += 1
            veggie.goSide("Right", screenSize)
        if veggie.screenCollide(screenSize) == "Left":
            lev -= 1
            veggie.goSide("Left", screenSize)

        
        win.blit(image, imgRect)
        win.blit(veggie.image, veggie.rect)

        for wall in tiles:
            win.blit(wall.image,wall.rect)
        pygame.display.flip()
        clock.tick(60)
