import pygame, sys, math, random

pygame.init()

pygame.mixer.init()
pygame.mixer.music.load("Sounds/631160_Domyeah---Final-Boss.ogg")
    
pygame.mixer.music.play(loops=-1, start=0.0)

size = [900, 700]
screen = pygame.display.set_mode(size)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit();
