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
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Veggie Girl")

x = 50
y = 50
height = 60
width = 40
vel = 5
size = [500, 500]

isJump = False
jumpCount = 10

run = True
while run:
    pygame.time.delay(50)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
